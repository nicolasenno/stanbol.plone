jQuery(document).ready(function() {
	(function($) {
	
		if (typeof($().pyproxy) != 'function') {
		    /* jquery.pyproxy javascript file has not been set correctly.*/
		    return;
		}
		
		$("#fieldsetlegend-categorization").click(function() {
			alert("Categorisation clicked !");
			// get TinyMCE content
			//$("#text_ifr").contents().find("#content").html();
			// appends data to keywords textarea
			//$("#subject_keywords").append();
		});
		
	});
	
});

var EnhanceTags = function() {
	//$.pyproxy_call();
}