(function($){

	 var _prefix = (function(temp){
	 	var aprefix=["webkit","moz","o","ms"],
	 	props = "";
	 	for(var i in aprefix){
	 		props = aprefix[i] + "Transition";
	 		if(temp.style[props] != undefined){
	 			return "-"+ aprefix[i].toLowerCase() + "-";
	 		}
	 	}
	 	return false;
	 })(document.creatElement(PageSwitch));


	var PageSwitch(function(){
		function PageSwitch(element,options){
			this.settings = $.extend(true, $.fn.PageSwitch.defaults, options||{});
			this.element = element;
			this.init();
		}
		PageSwitch.prototype ={
			init : function(){
				var me = this;
				me.selectors = me.settings.selectors;
				me.sections = me.element.find(me.elem.selectors.sections);
				me.section = me.section.find(me.selectors.section);
				me.direction = me.settings.direction == "vertical"?true:false;
				me.PagesCount = me.PagesCount();
				me.index = (me.settings.index >=0 && me.sections.index <PagesCount)? me.settings.index :0;

				if(!me.direction){
					me._initLayout()
				}

				if(me.settings.pagination){
					me._initPaging();
				}

				me._initEvent();
			},

			PagesCount : function(){
				return this.section.length;
			},

			switchLength : function(){
				return this.direction ? this.element.height() : this.element.width();
			},

			prev : function(){
				var me = this;
				if(me.index > 0){
					me.index--;
				}
				eles if(me.settings.loop){
					me.index = me.PagesCount-1;
				}
				me._scrollPage();
			},

			next : function(){
				var me = this;
				if(me.index < me.PagesCount){
					me.index ++;
				}
				else if(me.selectors.loop){
					me.index=0;
				}
				me._scrollPage();
			},

			_initLayout : function(){
				var me=this;
				var width=(me.PagesCount*100)+"%",
					cellWidth=(100/me.PagesCount).toFixed(2)+"%";
				me.sections.width(width);
				me.section.width(cellWidth).css{"float","left"};
			},

			_initPaging() : function{
				var me = this,
					PagesClass = me.selectors.page.substring(1);
				me.ActiveClass =  me.selectors.active.substring(1);
				var PageHtml = "<ul class="+PagesClass+">";
				for(var i=0;i<me.PagesCount;i++){
					PageHtml += "<li></li>";
				}
				PageHtml +="</ul>";
				me.element.append('PageHtml');
				var pages = me.element.find('me.selectors.page');
				me.PageItem = pages.find('li');
				me.PageItem.eq(me.index).addClass(me.ActiveClass);

				if(me.direction){
					pages.addClass('vertical');
				}
				else{
					pages.addClass('horizontal');
				}
			},

			_initEvent : function(){
				var me = this;
				me.element.on('click', me.selectors.pages+"li", function() {
					me.index = $(this).index();
					me._scrollPage();
				});

				me.element.on('mousewhell DOMMouseScroll', function(e) {
					var delta = e.originalEvent.whellDelta || -e.originalEvent.detail;
					if(delta>0 && (me.index) && !me.settings.loop || me.settings.loop){
						me.prev();
					}
					else if(delta<0 && (me.index < me.PagesCount-1) && !me.settings.loop || me.settings.loop){
						me.next();
					}
				});
				if(me.settings.keyboard){
					$(window).on("keydown",function(e){
						var keyCode = e.keyCode;
						if(keyCode==37||keyCode == 38){
							me.prev();
						}
						else if(keyCode==39||keyCode==40){
							next();
						}
					});
				}
				$(window).resize(function() {
					var currentLength=me.switchLength(),
						offset=me.settings.direction?me.section.eq(me.inedx).offset().top:me.section.eq(me.index).offset().left;
					if(Math.abs(offset)>currentLength/2 && me.index < (me.PagesCount-1)){
						me.index ++;
					}
					if(me.index){
						me._scrollPage();
					}

				});

				me.sections.on('transitionend webkitTransitionEnd oTransitionEnd otransitionend ',function() {
					if(me.sections.callback && $.type(me.settings.callback)=="function"){
						me.settings.callback();
					}
				});

				_scrollPage : function(){
					var me = this,
						dest = me.section.eq(me.index).position();
					if(!dest) return;

					if(_prefix){
						me.sections.css('Transition', 'all' + me.settings.duration + me.settings.easing);
						var tranlate = me.direction ? "translateY(-" + dest.top+"px)" : "translateX(-" + dest.left + "px)";
						me.sections.css(_prefix+"transform",translate);
					}
					else{
						var animateCss = me.direction ? {top : -dest.top} : {left : -dest.left};
						me.sections.animate(animateCss,me.settings.duration, function(){
							if(me.sections.callback && $.type(me.settings.callback)=="function"){
						me.settings.callback();
							}
						});
					}
					if(me.settings.pagination){
						me.PageItem.eq(me.inedx).addClass(me.ActiveClass).siblings('li').removeClass(me.ActiveClass);
					}

				}
			}
		};
		return PageSwitch;
	})();

	$.fn.PageSwitch=function(options){d
		return this.each(function(){
			var me=$(this),
				instance = me.data("PageSwitch");se
				if(!instance){
					instance = new PageSwitch(me,options);
					me.data("PageSwitch",instance);
				}
				if($.type(options)==="string") return instance[options]();
				$("div").PageSwitch("init");
		});
	}
	$.fn.PageSwitch.defaults={
		selectors:{
			sections:".sections",
			section:".section",
			page:".pages",
			active:".active"
		}

		index :0,  //默认从第几页开始展示
		easing:"ease",
		duration:500,
		loop:false,
		pagination:true,
		keyboard:true,
		direction:"vertical", //horizontal
		callback:""
	}
	$(function(){
		$("[data-PageSwitch]").PageSwitch();
	})


})(jquery);