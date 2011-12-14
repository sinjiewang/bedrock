import l10n_utils


def index(request):
    return l10n_utils.render(request, "mozorg/index.html")

def channel(request):
    data = {}

    if 'mobile_first' in request.GET:
        data['mobile_first'] = True

    return l10n_utils.render(request, "mozorg/channel.html", data)

def button(request):
    return l10n_utils.render(request, "mozorg/button.html")

def new(request):
    return l10n_utils.render(request, "mozorg/new.html")