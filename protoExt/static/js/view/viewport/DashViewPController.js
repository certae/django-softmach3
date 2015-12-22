(Ext.cmd.derive(
                "Admin.view.main.ViewportController",
                Ext.app.ViewController,
                {
                    listen : {
                        controller : {
                            "#" : {
                                unmatchedroute : "onRouteChange"
                            }
                        }
                    },
                    routes : {
                        ":node" : "onRouteChange"
                    },
                    setCurrentView : function(a){
                        a = (a || "").toLowerCase();
                        var j = this, l = j.getReferences(), c = l.mainCardPanel, g = c.getLayout(), d = l.navigationTreeList, n = j
                                .getViewModel(), h = n.getData(), m = d.getStore(), e = m.findNode(
                                "routeId", a), k = e ? e.get("view") : null, i = h.currentView, b = c
                                .child("component[routeId=" + a + "]"), f;
                        if (i && i.isWindow) {
                            i.destroy()
                        }
                        i = g.getActiveItem();
                        if (!b) {
                            f = Ext.create("Admin.view." + (k || "pages.Error404Window"), {
                                hideMode : "offsets",
                                routeId : a
                            })
                        }
                        if (!f || !f.isWindow) {
                            if (b) {
                                if (b !== i) {
                                    g.setActiveItem(b)
                                }
                                f = b
                            } else {
                                Ext.suspendLayouts();
                                g.setActiveItem(c.add(f));
                                Ext.resumeLayouts(true)
                            }
                        }
                        d.setSelection(e);
                        if (f.isFocusable(true)) {
                            f.focus()
                        }
                        h.currentView = f
                    },
                    onNavigationTreeSelectionChange : function(a, b){
                        if (b && b.get("view")) {
                            this.redirectTo(b.get("routeId"))
                        }
                    },
                    onToggleNavigationSize : function(){
                        var e = this, d = e.getReferences(), f = d.navigationTreeList, c = d.mainContainerWrap, a = !f
                                .getMicro(), b = a ? 64 : 250;
                        if (Ext.isIE9m || !Ext.os.is.Desktop) {
                            Ext.suspendLayouts();
                            d.senchaLogo.setWidth(b);
                            f.setWidth(b);
                            f.setMicro(a);
                            Ext.resumeLayouts();
                            c.layout.animatePolicy = c.layout.animate = null;
                            c.updateLayout()
                        } else {
                            if (!a) {
                                f.setMicro(false)
                            }
                            d.senchaLogo.animate({
                                dynamic : true,
                                to : {
                                    width : b
                                }
                            });
                            f.width = b;
                            c.updateLayout({
                                isRoot : true
                            });
                            if (a) {
                                f.on({
                                    afterlayoutanimation : function(){
                                        f.setMicro(true)
                                    },
                                    single : true
                                })
                            }
                        }
                    },
                    onMainViewRender : function(){
                        if (!window.location.hash) {
                            this.redirectTo("dashboard")
                        }
                    },
                    onRouteChange : function(a){
                        this.setCurrentView(a)
                    },
                    onSearchRouteChange : function(){
                        this.setCurrentView("search")
                    },
                    onEmailRouteChange : function(){
                        this.setCurrentView("email")
                    }
                }, 0, 0, 0, 0, [ "controller.mainviewport" ], 0, [
                    Admin.view.main,
                    "ViewportController" ], 0)
);
