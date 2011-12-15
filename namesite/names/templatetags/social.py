# <div id="fb-root"></div>
# <script src="http://connect.facebook.net/en_US/all.js#appId=214917201889104&amp;xfbml=1">
# </script>
# <fb:like href="http://randomname.alwaysdata.com" send="false" layout="box_count" width="50" show_faces="false" colorscheme="dark" font="">
# </fb:like>

# <!-- Placera denna tagg i <head> eller precis fore din </body>-tagg -->
# <script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>

# <!-- Placera denna tagg dar du vill att +1-knappen ska visas -->
# <g:plusone size="tall" href="http://randomname.alwaysdata.net"></g:plusone>

from django import template

register = template.Library()

class SocialNode(template.Node):
    def __init__(self, href=None):
        self.tag_template = None # override this!
        self.href = href

    def get_href(self):
        raise NotImplementedError()

    def render(self, context):
        return self.tag_template % self.get_href()

class GplusNode(SocialNode):
    def __init__(self, href=None):
        self.href = href
        self.tag_template = """
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
<div class="social social-gplus">
<g:plusone size="tall" %s></g:plusone>
</div>
"""
    def get_href(self):
        if self.href is not None:
            return "href=\"%s\"" % self.href
        else:
            return ""

class FBNode(SocialNode):
    def __init__(self, href=None):
        self.href = href
        self.tag_template = """
<script src="http://connect.facebook.net/en_US/all.js#appId=214917201889104&amp;xfbml=1"></script>
<div class="social social-facebook">
<div id="fb-root"></div>
<fb:like %s send="false" layout="box_count" width="50" show_faces="false" colorscheme="dark" font=""></fb:like>
</div>
"""
    def get_href(self):
        if self.href is not None:
            return "href=\"%s\"" % self.href
        else:
            return "href=\"\""

def do_social(parser, token):
    nodes = {'gplus': GplusNode, 'facebook': FBNode}
    config = {}
    contents = token.split_contents()
    tag_name = contents[0]
    href = '""'
    if len(contents) > 1:
        href = contents[1]
    if not (href[0] == '"' and href[-1] == '"'):
        raise template.TemplateSyntaxError("%s tag arguments must be surrounded by double quotes (\")" % (tag_name))
    href = href[1:-1]
    return nodes[tag_name](href)

register.tag('gplus', do_social)
register.tag('facebook', do_social)

