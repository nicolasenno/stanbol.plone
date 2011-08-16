jQuery(document).ready(function() {
	(function($) {
	
		if (typeof($().pyproxy) != 'function') {
		    /* jquery.pyproxy javascript file has not been set correctly.*/
		    return;
		}
		
    //var text_container = $("#content", $("#text_ifr").contents());
	
    $("#sparql_submitter").click(function() {
      var data = { text : $("#sparql_query").val()};
      $.pyproxy_call('/jq_sparql', data);
    });
    $(".prettyprint").change(function() {
      prettyPrint();
    });
		$("#fieldsetlegend-categorization").click(function() {

      var content = $("#content", $("#text_ifr").contents()).html();
      if(content===null) {
        var content = $("#text").val();
      }
      var data = { text : extractText(content)};
			$.pyproxy_call('/jq_enhance_tags', data);
			// get TinyMCE content
			//$("#text_ifr").contents().find("#content").html();
			// appends data to keywords textarea
			//$("#subject_keywords").append();
		});
    VIE2.logLevels=[];    
    
      VIE2.connectors['stanbol'].options({            
        "enhancer_url" : "/Plone/front-page/engineproxy",            
        "entityhub_url" : "/Plone/entityhubproxy"        
      });        
      $('article.active-enhancement').remove();                
      // make the content area editable       
      //$('#content').hallo({            
      //  plugins: {              
      //    'halloformat': {}            
      //  },            
      //  editable: true        
      //});        
      
      //$('.mce_editable').annotate({
      $("#parent-fieldname-text").annotate({
        connector: VIE2.connectors['stanbol'],            
        debug: true,            
        decline: function(event, ui){                
         console.info('decline event', event, ui);            
        },            
        select: function(event, ui){                
          console.info('select event', event, ui);            
        },            
        remove: function(event, ui){                
          console.info('remove event', event, ui);            
        }        
      });                
      $('.saverButton').button();
      $('.enhanceButton').button({enhState: 'passiv'}).click(function(){            
        // Button with two states            
        var oldState = $(this).button('option', 'enhState');            
        var newState = oldState === 'passiv' ? 'active' : 'passiv';            
        $('.enhanceButton').button('option', 'enhState', newState);            
        if($(this).button('option', 'enhState') === 'active'){                
          // annotate.enable()                
          try {                    
            $("#parent-fieldname-text").annotate('enable', function(success){                        
              if(success){                            
                $('.enhanceButton').button('enable').button('option', 'label', 'Done');     
              } else {                            
                $('.enhanceButton').button('enable').button('option', 'label', 'error, see the log.. Try to enhance again!');    
              } 
            });
            $('.enhanceButton').button('disable').button('option', 'label', 'in progress...')
          } 
          catch (e) { 
            alert(e); 
          }  
        } 
        else {
          // annotate.disable()                
          $("#parent-fieldname-text").annotate('disable');                
          $('.enhanceButton').button('option', 'label', 'Enhance!');            
        }        
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
            .replace(/[;:.,\"\'\-]/g, '') //remove ;
	    .replace(/(<([^>]+)>)/ig,""); // remove html tags
};
