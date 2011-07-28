jQuery(document).ready(function() {
	(function($) {
	
		if (typeof($().pyproxy) != 'function') {
		    /* jquery.pyproxy javascript file has not been set correctly.*/
		    return;
		}
		
	
		$("#fieldsetlegend-categorization").click(function() {
      var data = { text : extractText($('#text_ifr').contents().find("#content").html())};
			$.pyproxy_call('/jq_engine_proxy', data);
			// get TinyMCE content
			//$("#text_ifr").contents().find("#content").html();
			// appends data to keywords textarea
			//$("#subject_keywords").append();
		});

	})(jQuery)
});

var EnhanceTags = function() {
	//$.pyproxy_call();
}

var extractText = function (obj) {
        return obj
            .replace(/\s+/g, ' ') //collapse multiple whitespaces
            .replace(/\0\b\n\r\f\t/g, '').trim() // remove non-letter symbols
	    .replace(/(<([^>]+)>)/ig,""); // remove html tags
};
