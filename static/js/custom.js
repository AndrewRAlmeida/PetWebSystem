$(document).ready(function()
{
	"use strict";

	var header = $('.header');
	var hamburgerBar = $('.hamburger_bar');
	var hamburger = $('.hamburger');

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();

		setTimeout(function()
		{
			$(window).trigger('resize.px.parallax');
		}, 375);
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});
	initMenu();
	function setHeader()
	{
		if($(window).scrollTop() > 91)
		{
			header.addClass('scrolled');
			hamburgerBar.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
			hamburgerBar.removeClass('scrolled');
		}
	}
	function initMenu()
	{
		if($('.menu').length)
		{
			var menu = $('.menu');
			hamburger.on('click', function()
			{
				hamburger.toggleClass('active');
				menu.toggleClass('active');
			});
		}
	}

	$('.owl-carousel.banner-home').owlCarousel({
		items:1,
		// lazyLoad:true,
		loop:true,
		nav:true,
		margin:0,
		autoHeight:true,
		navClass: [
			'owl-prev me-auto',
			'owl-next ms-auto'
		],
		navContainerClass: 'owl-nav d-flex w-100',
		navText: [
			'<span aria-label="' + 'Previous' + '"><i class="fa fa-angle-left"></i></span>',
			'<span aria-label="' + 'Next' + '"><i class="fa fa-angle-right"></i></span>'
		],
	});
});