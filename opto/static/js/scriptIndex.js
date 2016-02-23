$(document).ready(function() {

    var controller = new ScrollMagic.Controller({
        globalSceneOptions:{
            triggerHook: 'onCenter'
        }
    });

    //creating a timeline to add tweens.
    var tl = new TimelineMax();
        tl.staggerFrom('.tween', 1, {opacity: 0, scale: 0.7, }, 0.1)
        tl.staggerTo('.titleMaj', 0.5, {color: "#00c0b5",repeat: 1, yoyo:true},0.166667)
        tl.fromTo("#titre1", 0.8, {}, {y:10}, 1)
        tl.fromTo("#plus", 0.5, {y:20, x:50, opacity: 0, scale: 0}, {y:20, x:50, opacity: 1, scale: 1 }, 1)
        tl.fromTo(".tween2", 0.8, {}, {x:10}, 1);

    var scene1 = new ScrollMagic.Scene({
        triggerElement: '#1st_section',
        offset: 300

    })
    .setTween(tl)
    .addTo(controller)
    .addIndicators();

    var tl2 = new TimelineMax();
        tl2.fromTo(".parallax-panel", 1, {y:20, opacity: 0}, {y:20, opacity: 1});

    var scene2 = new ScrollMagic.Scene({
        triggerElement: '#2nd_section',
        duration: 600,
        offset:1000
    })
    .setTween(tl2)
    .addIndicators()
    .setPin('.scene2')
    .addTo(controller)

    //creating a timeline to add tweens.
    var tl3 = new TimelineMax();
        tl3.staggerFrom('.tween2', 1, {opacity: 0, scale: 0.7, }, 0.1)
        tl3.staggerTo('.titleMaj2', 0.5, {color: "#00c0b5",repeat: 1, yoyo:true},0.166667)
        tl3.fromTo("#titre2", 0.8, {}, {y:10}, 1)
        tl3.fromTo("#plus2", 1.5, {y:20, x:50, opacity: 0, scale: 0}, {y:20, x:50, opacity: 1, scale: 1 }, 1)
        tl3.fromTo(".tween4", 0.8, {}, {x:10}, 1);

    var scene3 = new ScrollMagic.Scene({
        triggerElement: '#3rd_section',
        offset: 2000,

    })
    .setTween(tl3)
    .addTo(controller)
    .addIndicators();
});
