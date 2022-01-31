from app import config
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

settings = config.get_settings()
templates = Jinja2Templates(directory=str(settings.templates_dir))


def render(request, template_name, context={}, status_code: int = 200, cookies: dict = {}):
    ctx = context.copy()
    ctx.update({"request": request})
    t = templates.get_template(template_name)
    html_str = t.render(ctx)
    response = HTMLResponse(html_str, status_code=status_code)
    response.set_cookie(key='darkmode', value=1)
    if len(cookies.keys()) > 0:
        # set httponly token
        for k, v in cookies.items():
            response.set_cookie(key=k, value=v, httponly=True)
    # delete cookies
    # for key in request.items():
    #     response.delete_cookie(key)

    return response
