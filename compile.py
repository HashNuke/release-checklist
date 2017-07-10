#!/usr/bin/env python3
import markdown2

input_markdown = open("README.md" , "r").read()
content_html = markdown2.markdown(input_markdown)

template = open("template.html", "r").read()
output = template.replace("CONTENTS", content_html)

file = open("index.html", "w")
file.write(output)
