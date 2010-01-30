var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));

var pageTracker = '1';
var trackHandler = '2';
_trackView=null;

function trackOnComplete() {
	// we have to wait till json request returns, to know whether current view is 'normal' or 'shopjet'
	if(_trackView==null) {
		setTimeout(function() {
				 trackOnComplete();
				}, 300);
		return;		
	}
	else {
		track();
	}
}


function track()
{
    try {
        pageTracker = _gat._getTracker("UA-12629178-1");
        pageTracker._trackPageview();

    } catch(er) {}
	
	 // track whether current page is normal / shopjet
	 console.log("View mode:"+_trackView);
	 pageTracker._trackEvent('view', _trackView);

	 // the user clicked on "Purchase" button from 'normal' page (this is overriden in showproduct.html in case of 'shopjet' page)
    trackHandler = function() {
        pageTracker._trackEvent('get', 'normal');
    };
    $('input.standartFont').bind('click', trackHandler);
	
}

$(document).ready(trackOnComplete); 

