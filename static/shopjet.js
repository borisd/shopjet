
function emit_html(data) {
    document.write(data);
}

var host;
if (document.domain == '127.0.0.1')
    host = 'http://127.0.0.1:8000';
else
    host = 'http://static.shopjet.co.il';
	
emit_html(unescape("%3Cscript src='" + host + "/static/jquery-1.3.2.min.js' type='text/javascript'%3E%3C/script%3E"));
emit_html(unescape("%3Cscript src='" + host + "/static/jquery.qtip-1.0.0-rc3.min.js' type='text/javascript'%3E%3C/script%3E"));
emit_html(unescape("%3Cscript src='" + host + "/static/querystring.js' type='text/javascript'%3E%3C/script%3E"));
emit_html(unescape("%3Clink  href='" + host + "/static/style.css' type='text/css' rel='stylesheet' charset='UTF-8'/%3E"))
emit_html(unescape("%3Cscript src='" + host + "/static/shopjet_main.js' type='text/javascript'%3E%3C/script%3E"));
emit_html(unescape("%3Cscript src='" + host + "/static/shopjet_check.js' type='text/javascript'%3E%3C/script%3E"));
emit_html(unescape("%3Cdiv id='shopjet'%3E%3C/div%3E"));

