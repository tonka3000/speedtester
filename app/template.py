import os, jinja2

# pylint: disable=C0103

__dir = os.path.dirname(os.path.abspath(__file__))

def render_template(template, variables={}):
    '''
    render the given template
    '''
    templateLoader = jinja2.FileSystemLoader(searchpath=os.path.join(__dir, "../templates"))
    templateEnv = jinja2.Environment(loader=templateLoader, undefined=jinja2.StrictUndefined)

    TEMPLATE_FILE = "./" + template
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(variables)
    return outputText
