var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));

function track()
{
    try {
        var pageTracker = _gat._getTracker("UA-12629178-1");
        pageTracker._trackPageview();

    } catch(er) {}
}

$(document).ready(track); 

