from django import template
from django.conf import settings

register = template.Library()

class AnalyticsNode(template.Node):

    tag_template = """
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '%s']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
"""

    def __init__(self, account):
        self.account = account

    def render(self, context):
        return self.tag_template % (self.account)

def do_analytics(parser, token):
    account = None

    try:
        tag_name, account = token.split_contents()
    except ValueError:
        pass # okay, look in settings instead

    if account is None:
        try:
            account = settings.ANALYTICS_ACCOUNT
        except AttributeError:
            raise template.TemplateSyntaxError("%s tag needs an account name parameter or ANALYTICS_ACCOUNT defined in settings.py" % (token.contents.split()[0]))

    return AnalyticsNode(account)

register.tag('analytics', do_analytics)
