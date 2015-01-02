from blog import app
import mistune
app.jinja_env.filters['markdown'] = mistune.markdown

@app.template_filter()
def dateformat(date, format):
    if not date:
        return None
    return date.strftime(format)