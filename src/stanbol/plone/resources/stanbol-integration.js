jQuery(document).ready(function() {
	(function($) {
	
		if (typeof($().pyproxy) != 'function') {
		    /* jquery.pyproxy javascript file has not been set correctly.*/
		    return;
		}
		
    //var text_container = $("#content", $("#text_ifr").contents());
	
		$("#fieldsetlegend-categorization").click(function() {
      var data = { text : extractText($("#content", $("#text_ifr").contents()).html())};
			$.pyproxy_call('/jq_enhance_tags', data);
			// get TinyMCE content
			//$("#text_ifr").contents().find("#content").html();
			// appends data to keywords textarea
			//$("#subject_keywords").append();
		});
    $("#content").append('<button class="enhanceButton"><span>Enhance !</span></button>');
    VIE2.logLevels=[];    
    $($("#text_ifr").contents()).ready(function(){        
      VIE2.connectors['stanbol'].options({            
        "enhancer_url" : "/Plone/front-page/engineproxy",            
        "entityhub_url" : "/entityhub"        
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
      $("#content", $("#text_ifr").contents()).annotate({
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
      $('.enhanceButton').button({enhState: 'passiv'}).click(function(){            
        // Button with two states            
        var oldState = $(this).button('option', 'enhState');            
        var newState = oldState === 'passiv' ? 'active' : 'passiv';            
        $('.enhanceButton').button('option', 'enhState', newState);            
        if($(this).button('option', 'enhState') === 'active'){                
          // annotate.enable()                
          try {                    
            $("#content", $("#text_ifr").contents()).annotate('enable', function(success){                        
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
          $("#content", $("#text_ifr").contents()).annotate('disable');                
          $('.enhanceButton').button('option', 'label', 'Enhance!');            
        }        
      });    
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
