import pathlib
import subprocess
import sys
import tempfile
import unittest

import lint_md


class EmphasisLintTests(unittest.TestCase):
    def lint(self, text, rules=None):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "article.md"
            path.write_text(text, encoding="utf-8")
            return lint_md.lint_file(path, rules or {"emphasis-flanking"})

    def test_broken_and_valid_emphasis(self):
        broken = (
            "주요 이론은 **단절 이론(disconnection theory)**이다.",
            "- *28개(82.4%)*에서 관여",
            '둘째, **"LLM은 연장"**이라는 비유',
            "*97% (20턴 기준)*로",
            "*하네스·린트·테스트· *로",
            "*상품★*이",
        )
        valid = (
            "두 모드 모두 *사람*이 필요하다.",
            "- **1.** **자연어를 도구 호출로** — 변환한다.",
            "***굵고 기울임***과 *다른* 강조",
            "<strong>단절 이론(disconnection theory)</strong>이다.",
        )
        for text in broken:
            with self.subTest(text=text):
                self.assertTrue(any(row[1] == "ERROR" for row in self.lint(text)))
        for text in valid:
            with self.subTest(text=text):
                self.assertEqual([], self.lint(text))

    def test_non_text_and_literal_stars_are_ignored(self):
        text = r'''---
summary: "*내용)*은"
---
- 목록
***
* * *
\*글자\*와 `*code)*`, $a*b$, \(a*b\), <span title="*x">텍스트</span>
[링크](https://example.com/a*b) ![그림](https://example.com/*)
```
*코드)*다
```
$$
a*b
$$
\[
a*b
\]
'''
        self.assertEqual([], self.lint(text))

    def test_original_line_numbers_and_old_aliases(self):
        text = "---\ntitle: test\n---\n\n*깨짐)*이다\n"
        for name in ("emphasis-flanking", "bold-cjk", "italic-cjk-star"):
            with self.subTest(name=name):
                result = self.lint(text, {name})
                self.assertEqual(5, result[0][0])
                self.assertEqual("ERROR", result[0][1])

    def test_multiple_of_three_and_nested_delimiters(self):
        for text in ("***foo***", "foo***bar***baz", "*foo **bar** baz*"):
            with self.subTest(text=text):
                self.assertEqual([], self.lint(text))
        self.assertTrue(self.lint("*foo**bar*"))

    def test_cli_old_rule_names(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "article.md"
            path.write_text("*28개(82.4%)*에서\n", encoding="utf-8")
            script = pathlib.Path(lint_md.__file__)
            for name in ("bold-cjk", "italic-cjk-star"):
                with self.subTest(name=name):
                    result = subprocess.run(
                        [sys.executable, str(script), "--rules", name, str(path)],
                        capture_output=True, text=True, timeout=60,
                    )
                    self.assertEqual(1, result.returncode)
                    self.assertIn("emphasis-flanking", result.stdout)

    def test_multiline_paragraph(self):
        self.assertEqual([], self.lint("여기 *강조가\n이어진다*는 문장이다.\n"))


if __name__ == "__main__":
    unittest.main()
