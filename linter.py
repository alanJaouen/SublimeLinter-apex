# or NodeLinter, PythonLinter, ComposerLinter, RubyLinter
from SublimeLinter.lint import Linter


class sfdx_scanner(Linter):
    cmd = 'stylelint --formatter json --stdin-filename ${file}'
    cmd = "sfdx scanner:run --category='Code Style,Best Practices,Security' --format=csv -t ${file}"
    regex = r'^"\d+","[^"]+","(?:(?P<error>1)|(?P<warning>[^1]))","(?P<line>\d+)","(?P<col>\d+)","(?P<code>[^"]+)","(?P<message>[^"]+)"'

    multiline = True
    defaults = {
        'selector': 'source.apex'
    }
