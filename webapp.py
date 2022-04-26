import justpy as jp


def app():
    wp = jp.QuasarPage()
    #creating object for each element
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs course review analysis")
    return wp

jp.justpy(app)