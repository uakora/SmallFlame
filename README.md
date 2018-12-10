# SmallFlame
web small flame


        function set_popover($dom, title, content) {
            $dom.popover({
                //title: title,
                html: true,
                content: content,
                trigger: "manual",
            }).on("mouseenter", function () {
                var _this = this;
                $(this).popover("show");
                $(this).siblings(".popover").on("mouseleave", function () {
                    $(_this).popover('hide');
                });
            }).on("mouseleave", function () {
                var _this = this;
                setTimeout(function () {
                    if (!$(".popover:hover").length) {
                        $(_this).popover("hide")
                    }
                }, 100);
            });
        }
