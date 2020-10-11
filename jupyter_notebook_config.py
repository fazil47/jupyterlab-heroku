# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="sha1:6301485123be:287f2b43a566a8e00c2cd71abc2d76a6eb207028"
c.NotebookApp.token=""
