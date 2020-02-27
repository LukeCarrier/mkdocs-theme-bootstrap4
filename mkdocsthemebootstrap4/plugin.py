import mkdocs


class Bootstrap4Blockquotes(mkdocs.plugins.BasePlugin):
    def on_post_page(self, output_content, page, config):
        return output_content \
            .replace("<blockquote>", "<blockquote class=\"blockquote\">")

class Bootstrap4Tables(mkdocs.plugins.BasePlugin):
    def on_post_page(self, output_content, page, config):
        return output_content \
            .replace("<table>", "<table class=\"table\">") \
            .replace("<th>", "<th scope=\"col\">")
