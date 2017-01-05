# markdown2dita

## Introduction

`markdown2dita` is a lightweight tool written in pure python to convert 
content written in markdown to dita-ot.

It relies heavily on the [mistune](https://github.com/lepture/mistune) library
(which is fantastic to work with!) to parse the markdown.

## Installation

`markdown2dita` should work for all python2 versions 2.6+ and for all python3 
versions 3.3+.

### Via pip

`markdown2dita` can be installed via the pip package manager:

```
pip install markdown2dita
```

### Local installation (for development)

`markdown2dita` can be used locally as follows:

1. Clone the repository:
   ```
   git clone https://github.com/mattcarabine/markdown2dita.git
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage

`markdown2dita` is designed to be used either as a python package or a simple
command line tool.

### From the CLI

The CLI tool takes markdown as input either from a file or `stdin` and outputs 
the equivalent dita to either a file or `stdout`.

#### Usage instructions

```
usage: markdown2dita [-h] [-i INPUT_FILE] [-o OUTPUT_FILE]

markdown2dita - a markdown to dita-ot CLI conversion tool.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        input markdown file to be converted.If omitted, input
                        is taken from stdin.
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        output file for the converted dita content.If omitted,
                        output is sent to stdout.
```

#### Examples

##### Reading an input file
The below example demonstrates how to convert a given input file `test.md`:

```
markdown2dita -i test.md
```

##### Reading from stdin
The below example demonstrates how to use `markdown2dita` to convert markdown
provided via `stdin` to dita:

```
echo '**My** `markdown` *string*' | markdown2dita
```

##### Outputting to a file
The below example demonstrates how to send the dita output to a given file:

```
markdown2dita -o test.dita
```

### From a python program

`markdown2dita` attempts to be API-compatible with `mistune` as much as 
possible, meaning that all code written for mistune can use `markdown2dita` as
a pop-in replacement instead to generate dita rather than html.

A simple API that renders markdown formatted text as dita:

```
import markdown2dita

markdown2dita.markdown('I am using **markdown2dita markdown converter**')
```

If you care about performance, it is better to re-use the `Markdown` instance:

```
import markdown2dita

markdown = markdown2dita.Markdown()
markdown('I am using **markdown2dita markdown converter**')
```

Much like `mistune` you can do things like override the renderer, however I 
would not recommend doing so as this tool simply aims to be a dita converter.

If you wish to alter the output of the markdown conversion then I recommend 
checking out [mistune](https://github.com/lepture/mistune) itself.

## Known limitations

Certain elements from markdown do not exist in dita, below is a list of them 
along with an explanation of how the converter handles them:

- **block quote (`>`)**: dita-ot does not have the capability for block quotes, 
therefore the converter will output these as codeblocks instead which create a
similar graphic effect
- **strikethrough (`~strikethrough~`)**: dita-ot does not have the capability to 
display strikethroughs, the converter will just include the struck through text
as plain text.
- **inline html**: dita-ot does not really support inline html, the converter 
will just send the plain html through.
- **footnotes**: footnotes are completely ignored by the converter.
- **hrule**: dita-ot does not support horizontal rules, the converter ignores
any in the input text.
- **headings**: dita-ot only supports a single level of heading. Therefore each
section is split on `H2` and above (where the heading is the section title).
This can be configured by passing the option `title_level` to the markdown
initializer. For example, to set all headings H4 and above to be the section 
titles:
    ```
    import markdown2dita
    
    markdown = markdown2dita.Markdown(title_level=4)
    markdown(text)
    ```