jQuery(document).ready(function() {
	(function($) {
	
		if (typeof($().pyproxy) != 'function') {
		    /* jquery.pyproxy javascript file has not been set correctly.*/
		    return;
		}
		
	
		$("#fieldsetlegend-categorization").click(function() {
			alert("Categorization clicked !");
			$.pyproxy_call('/jq_engine_proxy', '#text_ifr');
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