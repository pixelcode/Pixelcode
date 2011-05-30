var config =
{
	// html elements requiring js support
	js_support: '.success-stories, .slider-nav, #partners, #nav, .testimonials, #twitter_div, .flickr-feed, table',
	
	// main navigation
	nav:
	{
		elements: '#nav ul li',
		speed: 500,
		effect: 'slide'
	},
	
	// form inputs using tip values
	form_tips: 'input[name=search], input[name=name], input[name=email], textarea[name=message]',
	
	// form inputs using validation
	form_validate: 'input[name=name], input[name=email], textarea[name=message]',
	
	// nivo slider containers
	nivo:
	{
		elements: 'div.nivo-slider',
		options:
		{
			effect: 'random',
			slices: 15,
			animSpeed: 500,
			pauseTime: 3000,
			startSlide: 0,
			directionNav: true,
			directionNavHide: true,
			controlNav: true,
			controlNavThumbs: false,
			controlNavThumbsFromRel: false,
			controlNavThumbsSearch: '.jpg',
			controlNavThumbsReplace: '_thumb.jpg',
			keyboardNav: true,
			pauseOnHover: true,
			manualAdvance: false,
			captionOpacity: 0.8,
			beforeChange: function(){},
			afterChange: function(){},
			slideshowEnd: function(){}
		}
	},
	
	// tooltips
	tooltips_standalone: '#partners ul.items li, .flickr-feed a.frame',
	
	// tooltips standalone
	tooltips: 'div.main a.frame, , div.social ul li, ul.social-2 li',
	
	// elements with shadows that will be bordered in browsers that not support box-shadow property
	border_shadow: '.tooltip span, .box, .frame, .button, .comments li > div, #nav ul ul',
	
	// lightbox galleries
	lightbox: 'ul.gallery li > a',
	
	// default tips for form inputs
	formdata:
	{
		name: 'Name...',
		email: 'Email...',
		message: 'Message...',
		search: 'Search...'
	},
	
	// success stories options
	success_stories:
	{
		speed: 500,
		fade: false,
		easing: 'swing'
	},
	
	// testimonials slider
	testimonials:
	{
		speed: 500,
		fade: true,
		easing: 'swing'
	},
	
	// partners
	partners:
	{
		slide: 2,
		speed: 500,
		fade: false,
		easing: 'swing'
	}
};
