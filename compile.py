#!/usr/bin/env python3
import mistune

input_markdown = open("README.md" , "r").read()
content_html = mistune.markdown(input_markdown)

template = open("template.html", "r").read()
output = template.replace("CONTENTS", content_html)

file = open("index.html", "w")
file.write(output)
