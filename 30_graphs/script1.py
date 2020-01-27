from flask import Flask, render_template

app = Flask(__name__)


@app.route('/plot/')
def plot():
    from pandas_datareader import data as pdr
    import datetime
    from bokeh.plotting import figure # , show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2015, 11, 1)
    end = datetime.datetime(2016, 3, 10)

    goog = pdr.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

    def stat(cl, op):
        if cl > op:
            value = "inc"
        elif op > cl:
            value = "dec"
        else:
            value = "eq"
        return value

    goog["Status"] = [stat(c, o) for c, o in zip(goog.Close, goog.Open)]

    # add mean and range cols to df

    goog["Mean"] = (goog.Open + goog.Close) / 2
    goog["Range"] = (goog.Open - goog.Close)

    # plot params

    # get datestamps
    plt_gr = goog.index[goog.Status == 'inc']
    plt_rd = goog.index[goog.Status == 'dec']

    # get glyph centers (mean)
    plt_gr_y = goog.Mean[goog.Status == 'inc']
    plt_rd_y = goog.Mean[goog.Status == 'dec']

    # set width to 1/2 of x interval
    plt_wt = (goog.index[1] - goog.index[0]) / 2

    # get glyph heights (range)
    plt_gr_h = goog.Range[goog.Status == 'inc']
    plt_rd_h = goog.Range[goog.Status == 'dec']

    gn = '#99ff99'
    rd = '#ffb399'

    # plot setup

    plt = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
    plt.title.text = "Candlestick Chart"
    plt.grid.grid_line_alpha = 0.75

    # add range line segments
    plt.segment(goog.index, goog.High, goog.index, goog.Low, color='black')

    # plots for gains
    plt.rect(x=plt_gr, y=plt_gr_y, width=plt_wt, height=abs(plt_gr_h), fill_color=gn, line_color='black')
    # plots for losses
    plt.rect(x=plt_rd, y=plt_rd_y, width=plt_wt, height=abs(plt_rd_h), fill_color=rd, line_color='black')

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html",
                           script1=script1,
                           div1=div1,
                           cdn_css=cdn_css,
                           cdn_js=cdn_js)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
