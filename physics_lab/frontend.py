import plotly.graph_objects as go


# Frontend
def draw_func_1(arr_t, arr_x, arr_y, string1, string2, string3, string4, string5):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arr_t, y=arr_x, name=string1))
    fig.add_trace(go.Scatter(x=arr_t, y=arr_y, name=string2))
    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      title=string3,
                      xaxis_title=string4,
                      yaxis_title=string5,
                      font=dict(
                          family="Courier New, monospace",
                          size=20,
                          color="Black"
                      ),
                      margin=dict(l=0, r=0, t=45, b=0))
    fig.show()


# Frontend
def draw_func_2(arr_x, arr_y, string1, string2, string3, string4):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arr_x, y=arr_y, name=string1))
    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      title=string2,
                      xaxis_title=string3,
                      yaxis_title=string4,
                      font=dict(
                          family="Courier New, monospace",
                          size=20,
                          color="Black"
                      ),
                      margin=dict(l=0, r=0, t=45, b=0))

    fig.add_trace(go.Scatter(x=arr_x, y=arr_y))
    fig.show()