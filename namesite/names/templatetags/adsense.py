from django import template

register = template.Library()

# <script type="text/javascript"><!--
# google_ad_client = "ca-pub-3542806687645384";
# /* laszlo_nu utvalda sidor */
# google_ad_slot = "3858207963";
# google_ad_width = 468;
# google_ad_height = 60;
# //-->
# </script>
# <script type="text/javascript"
# src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
# </script>

class AdsenseNode(template.Node):

    tag_template = """
<script type="text/javascript"><!--
google_ad_client = "%s";
google_ad_slot = "%s";
google_ad_width = %s;
google_ad_height = %s;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
"""

    def __init__(self, settings):
        self.settings = []
        for setting in ['client', 'slot', 'width', 'height']:
            if setting not in settings:
                raise template.TemplateSyntaxError("%s is not defined (use %s:value)" % (setting, setting))
            else:
                self.settings.append(settings[setting])

    def render(self, context):
        return self.tag_template % tuple(self.settings)

def do_adsense(parser, token):
    config = {}
    contents = token.split_contents()
    tag_name = contents[0]
    settings = contents[1:]
    for s in settings:
        try:
            k, v = s.split(":")
            config[k] = v
        except ValueError:
            raise template.TemplateSyntaxError("%s is not on the format key:value" % (s))
    return AdsenseNode(config)

register.tag('adsense', do_adsense)
