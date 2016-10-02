
// -----------
Ext.create("Admin.data.Simulated", Ext.Base,
        {
            onClassExtended : function(a, d){
                var c = d.$className.toLowerCase().replace(/\./g, "/").replace(/^admin\/data/,
                        "~api"), e = {
                    type : "json",
                    data : d.data
                }, b = {};
                b[c] = e;
                Ext.ux.ajax.SimManager.register(b)
            }
        }, 0, 0, 0, 0, 0, 0, [ Admin.data, "Simulated" ], function(){
            Ext.ux.ajax.SimManager.init({
                defaultSimlet : null
            })
        });

// -----------
Ext.create("Admin.data.Pie", Admin.data.Simulated, {
    data : [ {
        xvalue : "Drama",
        yvalue : 10
    }, {
        xvalue : "Fantasy",
        yvalue : 10
    }, {
        xvalue : "Action",
        yvalue : 12
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data, "Pie" ], 0);

// -----------
Ext.create("Admin.data.Radial", Admin.data.Simulated, {
    data : [ {
        xvalue : "A",
        yvalue : 417
    }, {
        xvalue : "B",
        yvalue : 676
    }, {
        xvalue : "C",
        yvalue : 606
    }, {
        xvalue : "D",
        yvalue : 124
    }, {
        xvalue : "E",
        yvalue : 473
    }, {
        xvalue : "F",
        yvalue : 108
    }, {
        xvalue : "G",
        yvalue : 847
    }, {
        xvalue : "H",
        yvalue : 947
    }, {
        xvalue : "I",
        yvalue : 694
    }, {
        xvalue : "J",
        yvalue : 603
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data, "Radial" ], 0);

// -----------
Ext.create("Admin.data.Subscriptions", Admin.data.Simulated, {
    data : [ {
        id : 1,
        name : "Steve Horton",
        subscription : "Enterprise"
    }, {
        id : 2,
        name : "Scott Calabrese",
        subscription : "Trial"
    }, {
        id : 3,
        name : "Taresa Doe",
        subscription : "Premium"
    }, {
        id : 4,
        name : "Lucy Doe",
        subscription : "Trial"
    }, {
        id : 5,
        name : "Charles Boyle",
        subscription : "Enterprise"
    }, {
        id : 6,
        name : "Charles Doe",
        subscription : "Enterprise"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data, "Subscriptions" ], 0);


// -----------
Ext.create(
                "Admin.data.UserNotifications",
                Admin.data.Simulated,
                {
                    data : [
                        {
                            _id : 642,
                            name : "Marion Williams",
                            content : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            date : "9/13/2005",
                            time : "9:72 PM"
                        },
                        {
                            _id : 351,
                            name : "Nora Watson",
                            content : "Lorem ipsum dolor sit amet. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                            date : "10/28/2003",
                            time : "0:69 PM"
                        },
                        {
                            _id : 553,
                            name : "Ray Williams",
                            content : "laborum",
                            date : "10/15/2008",
                            time : "2:30 PM"
                        },
                        {
                            _id : 232,
                            name : "Marion Brooks",
                            content : "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            date : "8/19/2009",
                            time : "9:49 PM"
                        },
                        {
                            _id : 775,
                            name : "Nettie Stewart",
                            content : "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                            date : "9/12/2011",
                            time : "2:71 PM"
                        },
                        {
                            _id : 247,
                            name : "Beatrice Carter",
                            content : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containin.",
                            date : "9/18/2007",
                            time : "1:48 PM"
                        } ]
                }, 0, 0, 0, 0, 0, 0, [ Admin.data, "UserNotifications" ], 0);

// -----------
Ext.create(
                "Admin.data.UserSharedItems",
                Admin.data.Simulated,
                {
                    data : [
                        {
                            _id : 306,
                            parent_id : 306,
                            name : "Homer Jackson",
                            source : "id",
                            date : "8/16/2009",
                            isActive : "aut",
                            time : "5:02 PM",
                            content : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                        },
                        {
                            _id : 750,
                            parent_id : 331,
                            name : "Dora Bailey",
                            source : "et",
                            date : "7/16/2007",
                            isActive : "cum",
                            time : "6:95 PM",
                            content : "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
                        },
                        {
                            _id : 948,
                            parent_id : 898,
                            name : "Mae Edwards",
                            source : "et",
                            date : "7/24/2003",
                            isActive : "et",
                            time : "9:46 PM",
                            content : "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
                        },
                        {
                            _id : 162,
                            parent_id : 525,
                            name : "Allen Morris",
                            source : "nobis",
                            date : "6/16/2008",
                            isActive : "ut",
                            time : "4:57 PM",
                            content : "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
                        },
                        {
                            _id : 252,
                            parent_id : 252,
                            name : "Ben Wright",
                            source : "quod",
                            date : "9/24/2003",
                            isActive : "culpa",
                            time : "2:03 PM",
                            content : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                        },
                        {
                            _id : 840,
                            parent_id : 840,
                            name : "Jim Sanchez",
                            source : "cumque",
                            date : "8/17/2007",
                            isActive : "laborum",
                            time : "1:42 PM",
                            content : "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."
                        } ]
                }, 0, 0, 0, 0, 0, 0, [ Admin.data, "UserSharedItems" ], 0);

// -----------
Ext.create("Admin.data.dashboard.Counce", Admin.data.Simulated, {
    data : [ {
        xvalue : 0,
        y1value : 15,
        y2value : 15
    }, {
        xvalue : 5,
        y1value : 20,
        y2value : 20
    }, {
        xvalue : 10,
        y1value : 15,
        y2value : 15
    }, {
        xvalue : 15,
        y1value : 16,
        y2value : 16
    }, {
        xvalue : 20,
        y1value : 14,
        y2value : 14
    }, {
        xvalue : 25,
        y1value : 18,
        y2value : 18
    }, {
        xvalue : 30,
        y1value : 10,
        y2value : 10
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.dashboard, "Counce" ], 0);

// -----------
Ext.create("Admin.data.dashboard.Full", Admin.data.Simulated, {
    data : [ {
        xvalue : 250,
        y1value : 94,
        y2value : 40
    }, {
        xvalue : 500,
        y1value : 78,
        y2value : 46
    }, {
        xvalue : 750,
        y1value : 60,
        y2value : 53
    }, {
        xvalue : 1250,
        y1value : 51,
        y2value : 48
    }, {
        xvalue : 1500,
        y1value : 60,
        y2value : 36
    }, {
        xvalue : 1750,
        y1value : 68,
        y2value : 26
    }, {
        xvalue : 2250,
        y1value : 59,
        y2value : 37
    }, {
        xvalue : 2500,
        y1value : 40,
        y2value : 58
    }, {
        xvalue : 2750,
        y1value : 24,
        y2value : 78
    }, {
        xvalue : 3250,
        y1value : 36,
        y2value : 85
    }, {
        xvalue : 3500,
        y1value : 65,
        y2value : 70
    }, {
        xvalue : 3750,
        y1value : 94,
        y2value : 55
    }, {
        xvalue : 4250,
        y1value : 103,
        y2value : 61
    }, {
        xvalue : 4500,
        y1value : 83,
        y2value : 82
    }, {
        xvalue : 4750,
        y1value : 61,
        y2value : 102
    }, {
        xvalue : 5250,
        y1value : 55,
        y2value : 95
    }, {
        xvalue : 5500,
        y1value : 70,
        y2value : 67
    }, {
        xvalue : 5750,
        y1value : 84,
        y2value : 39
    }, {
        xvalue : 6250,
        y1value : 78,
        y2value : 31
    }, {
        xvalue : 6500,
        y1value : 58,
        y2value : 49
    }, {
        xvalue : 6750,
        y1value : 38,
        y2value : 69
    }, {
        xvalue : 7250,
        y1value : 41,
        y2value : 74
    }, {
        xvalue : 7500,
        y1value : 65,
        y2value : 60
    }, {
        xvalue : 7750,
        y1value : 89,
        y2value : 46
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.dashboard, "Full" ], 0);

// -----------
Ext.create("Admin.data.dashboard.Tasks", Admin.data.Simulated, {
    data : [ {
        id : 1,
        task : "Upgrade to SSD harddisks",
        done : true
    }, {
        id : 2,
        task : "Pay server invoice",
        done : true
    }, {
        id : 3,
        task : "Upgrade to SSD harddisks",
        done : false
    }, {
        id : 4,
        task : "Pay server invoice",
        done : false
    }, {
        id : 5,
        task : "Upgrade to SSD harddisks",
        done : false
    }, {
        id : 6,
        task : "Pay server invoice",
        done : false
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.dashboard, "Tasks" ], 0);

// -----------
Ext.create("Admin.data.dashboard.Visitor", Admin.data.Simulated, {
    data : [ {
        xvalue : 0,
        y1value : 10,
        y2value : 10
    }, {
        xvalue : 5,
        y1value : 15,
        y2value : 15
    }, {
        xvalue : 10,
        y1value : 20,
        y2value : 20
    }, {
        xvalue : 15,
        y1value : 15,
        y2value : 15
    }, {
        xvalue : 20,
        y1value : 20,
        y2value : 20
    }, {
        xvalue : 25,
        y1value : 15,
        y2value : 15
    }, {
        xvalue : 30,
        y1value : 20,
        y2value : 20
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.dashboard, "Visitor" ], 0);

// -----------
Ext.create("Admin.data.email.Friends", Admin.data.Simulated, {
    data : [ {
        id : 0,
        online : true,
        name : "Torres Tran"
    }, {
        id : 1,
        online : false,
        name : "Oneill Franklin"
    }, {
        id : 2,
        online : false,
        name : "Branch Allison"
    }, {
        id : 3,
        online : true,
        name : "Hines Moon"
    }, {
        id : 4,
        online : true,
        name : "Molina Wilkerson"
    }, {
        id : 5,
        online : true,
        name : "Suzette Powell"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.email, "Friends" ], 0);

// -----------
Ext.create(
                "Admin.data.email.Inbox",
                Admin.data.Simulated,
                {
                    data : [
                        {
                            id : 0,
                            read : false,
                            user_id : 4,
                            title : "Cillum ad ad ut velit.",
                            contents : "Cupidatat ex sit excepteur deserunt et qui nisi voluptate minim dolor id laborum dolor culpa. Eiusmod excepteur consequat aliquip irure magna. Occaecat duis officia Lorem ut exercitation irure laboris pariatur esse consectetur. Nulla consequat magna id et est excepteur mollit cillum cupidatat tempor ea laboris ut. Fugiat ea et occaecat laboris consequat dolor cupidatat velit Lorem minim. Deserunt fugiat reprehenderit qui proident sunt.\r\n",
                            from : "Estela Gibbs",
                            received_on : "Thu Sep 25 2014 09:57:57 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img1.jpg", "img2.jpg" ]
                        },
                        {
                            id : 1,
                            read : true,
                            user_id : 7,
                            title : "Consequat officia dolor sit labore aliquip elit enim sunt id magna.",
                            contents : "Quis mollit pariatur consectetur deserunt minim aliqua excepteur incididunt excepteur. Laboris dolor deserunt incididunt et elit incididunt occaecat ullamco sunt. Ad excepteur amet tempor amet voluptate reprehenderit et in.\r\n",
                            from : "Constance Flores",
                            received_on : "Sat Aug 16 2014 17:41:31 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : false
                        },
                        {
                            id : 2,
                            read : true,
                            user_id : 1,
                            title : "Occaecat quis laborum qui cupidatat culpa ullamco fugiat incididunt.",
                            contents : "Pariatur occaecat non eiusmod mollit. Id mollit dolore do mollit culpa deserunt Lorem occaecat consequat dolor do irure anim. Anim tempor ut non id dolor do est aliquip officia aliqua nulla sint elit occaecat. Eu laborum veniam aute magna velit consequat exercitation incididunt amet ut velit. In duis aliqua dolor culpa sit eu nostrud ex laboris aute laborum. Adipisicing magna in laborum enim ut qui ut nulla tempor sint magna cupidatat sint est.\r\n",
                            from : "Tammi Merrill",
                            received_on : "Mon Oct 20 2014 21:06:29 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : false
                        },
                        {
                            id : 3,
                            read : false,
                            user_id : 8,
                            title : "Dolor exercitation ea labore ipsum deserunt eu deserunt pariatur labore occaecat nisi exercitation.",
                            contents : "Exercitation id laborum ullamco do et. Id mollit anim labore ea cupidatat esse excepteur cillum labore dolor amet adipisicing sint. Qui fugiat dolor incididunt velit ipsum exercitation minim do ad adipisicing quis ut eu. Voluptate dolore officia irure est.\r\n",
                            from : "Hannah Robertson",
                            received_on : "Fri Feb 14 2014 16:00:34 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img1.jpg", "img2.jpg", "img4.jpg" ]
                        },
                        {
                            id : 4,
                            read : false,
                            user_id : 4,
                            title : "Adipisicing occaecat ut magna minim dolor sint aute ipsum sit enim excepteur excepteur ea nostrud.",
                            contents : "Eiusmod duis irure nostrud elit esse nostrud. In sit elit labore velit velit occaecat ad ea sit. Esse nulla proident nulla non adipisicing sit nisi pariatur.\r\n",
                            from : "Rhea Clemons",
                            received_on : "Tue Nov 25 2014 18:35:05 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img1.jpg", "img2.jpg" ]
                        },
                        {
                            id : 5,
                            read : false,
                            user_id : 9,
                            title : "Esse consectetur exercitation officia eiusmod sint ex nisi.",
                            contents : "Veniam et magna aute ea quis deserunt ad fugiat. Duis adipisicing ad dolor proident laboris ut irure do aute. Elit do anim in excepteur. Amet non dolore sit culpa culpa. Ea esse laboris occaecat consectetur non ut ex mollit ullamco cupidatat ex Lorem labore id. Ea voluptate eiusmod sit cupidatat et minim id nisi Lorem ut duis.\r\n",
                            from : "Petty Caldwell",
                            received_on : "Sat Oct 18 2014 17:09:49 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : false
                        },
                        {
                            id : 6,
                            read : true,
                            user_id : 3,
                            title : "Officia Lorem ullamco id deserunt dolor magna nostrud.",
                            contents : "Lorem ut nisi pariatur sunt sunt eiusmod. Voluptate est deserunt magna laborum eiusmod adipisicing consequat ad ullamco incididunt irure quis cupidatat velit. Voluptate adipisicing officia enim proident Lorem proident Lorem duis. Consequat elit enim nostrud Lorem proident. Exercitation velit incididunt consequat nisi nisi ullamco consequat. Quis non sint laboris irure fugiat culpa ipsum. Veniam aliqua cillum occaecat in aliqua labore id magna labore sit est est.\r\n",
                            from : "Daniel Lawrence",
                            received_on : "Fri Sep 12 2014 03:17:35 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : true,
                            attachments : [ "img3.jpg", "img1.jpg" ]
                        },
                        {
                            id : 7,
                            read : false,
                            user_id : 5,
                            title : "Pariatur ea culpa ut veniam aliqua ea occaecat.",
                            contents : "Aute exercitation nisi adipisicing adipisicing dolor aliqua velit amet. Labore minim commodo ex fugiat nulla excepteur aliquip pariatur magna id anim. Commodo irure eiusmod ex quis. Irure anim velit culpa irure culpa deserunt nostrud enim nostrud deserunt.\r\n",
                            from : "Newman Atkins",
                            received_on : "Thu May 15 2014 23:01:39 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img3.jpg", "img2.jpg" ]
                        },
                        {
                            id : 8,
                            read : true,
                            user_id : 19,
                            title : "Officia nostrud ipsum enim fugiat laborum ut ullamco non laborum sint sunt.",
                            contents : "In excepteur ex ad non esse minim commodo laborum. Veniam nisi amet ea esse magna sint labore deserunt duis ut cillum cupidatat ad ex. Nulla ut est cillum in. Commodo voluptate et Lorem eu exercitation. Esse dolore laborum ipsum duis veniam proident occaecat commodo culpa magna. Consectetur ea voluptate sint do incididunt non sunt officia velit.\r\n",
                            from : "Marcella Wade",
                            received_on : "Tue Feb 11 2014 04:24:27 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : false
                        },
                        {
                            id : 9,
                            read : false,
                            user_id : 20,
                            title : "Exercitation cupidatat elit ut sunt.",
                            contents : "Lorem dolor sunt fugiat tempor labore. Id veniam laborum veniam cillum consequat velit in elit consectetur. Do sunt tempor incididunt commodo qui nulla. Incididunt duis consectetur aliquip deserunt cillum. Proident occaecat fugiat deserunt minim ipsum commodo excepteur laboris irure excepteur tempor Lorem ex. Mollit anim mollit et do tempor voluptate duis magna deserunt ullamco incididunt. Minim aute ipsum commodo sit culpa voluptate adipisicing pariatur.\r\n",
                            from : "Jessica Warren",
                            received_on : "Wed Jan 14 2015 09:03:51 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img3.jpg", "img2.jpg", "img1.jpg" ]
                        },
                        {
                            id : 10,
                            read : true,
                            user_id : 18,
                            title : "Eiusmod voluptate dolor ex excepteur esse cillum aliquip mollit.",
                            contents : "Occaecat aliqua dolore ipsum voluptate tempor nisi veniam ad ex consequat est cillum adipisicing esse. Mollit excepteur ex officia dolor. Est officia reprehenderit do labore mollit eiusmod esse aliquip laborum cillum quis.\r\n",
                            from : "Nanette Gutierrez",
                            received_on : "Thu Jan 01 2015 01:29:22 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img4.jpg", "img1.jpg" ]
                        },
                        {
                            id : 11,
                            read : false,
                            user_id : 17,
                            title : "Et amet dolore veniam ullamco minim excepteur duis fugiat.",
                            contents : "Nulla et commodo et tempor irure nulla elit officia. In aliqua aute veniam ex. Qui eu ut amet do voluptate fugiat exercitation adipisicing est incididunt adipisicing. Ipsum deserunt voluptate cupidatat velit occaecat laboris ut et Lorem velit deserunt ut ut occaecat.\r\n",
                            from : "Adam Gullner",
                            received_on : "Fri May 02 2014 07:49:56 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : false
                        },
                        {
                            id : 12,
                            read : true,
                            user_id : 16,
                            title : "Incididunt in nulla dolor commodo aliqua pariatur amet sit Lorem.",
                            contents : "Officia eiusmod exercitation excepteur magna eiusmod do occaecat Lorem duis proident. Culpa Lorem est culpa ad elit sit commodo aute. Exercitation ea aute proident reprehenderit dolore. Laboris nisi reprehenderit minim dolore et sunt cillum amet consectetur amet eiusmod.\r\n",
                            from : "Chakra Gibson",
                            received_on : "Sun Nov 09 2014 20:00:57 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img2.jpg", "img4.jpg" ]
                        },
                        {
                            id : 13,
                            read : false,
                            user_id : 15,
                            title : "Ad amet aute officia non culpa ullamco non pariatur sit excepteur consequat nulla minim tempor.",
                            contents : "Consectetur labore nulla est do qui qui ad incididunt labore tempor enim proident consectetur. Est elit officia ex elit veniam excepteur mollit mollit nisi qui labore commodo reprehenderit. Nisi ipsum voluptate eiusmod sint aute ad proident anim duis ut non adipisicing anim. Nulla mollit aliqua occaecat minim proident adipisicing esse est irure.\r\n",
                            from : "Jonathan Soul",
                            received_on : "Sun Apr 13 2014 18:40:44 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : true,
                            attachments : [ "img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg" ]
                        },
                        {
                            id : 14,
                            read : false,
                            user_id : 6,
                            title : "Occaecat fugiat officia anim aute do laboris amet velit.",
                            contents : "Aute in pariatur veniam ad anim dolore quis deserunt voluptate pariatur do ut nisi. Elit duis est enim labore fugiat laborum quis culpa elit qui reprehenderit. Minim exercitation ullamco sunt aute id. Fugiat nisi in duis officia minim pariatur eu excepteur dolore ullamco. Aliqua Lorem sunt sunt mollit aliquip ut.\r\n",
                            from : "Shawn Leon",
                            received_on : "Thu Feb 20 2014 02:04:24 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : false
                        },
                        {
                            id : 15,
                            read : true,
                            user_id : 2,
                            title : "Occaecat minim in minim do et fugiat ipsum magna deserunt.",
                            contents : "Laboris esse aliqua adipisicing qui proident pariatur enim aute sunt labore. Esse labore adipisicing eu enim sunt ea ea. Cillum deserunt amet sit irure tempor qui ipsum aliqua ad ipsum et mollit sunt dolore. Magna ipsum ex mollit sit. Dolore Lorem proident pariatur incididunt dolor deserunt incididunt velit.\r\n",
                            from : "Goff Smith",
                            received_on : "Fri Jun 27 2014 11:14:54 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img2.jpg" ]
                        },
                        {
                            id : 16,
                            read : false,
                            user_id : 10,
                            title : "Eu non pariatur tempor ad ipsum.",
                            contents : "Fugiat sit culpa do eu irure reprehenderit quis nulla ut eiusmod officia esse est. Nisi exercitation adipisicing laborum non anim. Dolor adipisicing ex cillum laborum ullamco enim exercitation eiusmod Lorem duis aliqua. Culpa minim excepteur culpa irure officia duis ullamco enim amet qui do anim cillum commodo.\r\n",
                            from : "Mcgowan Berg",
                            received_on : "Thu Feb 27 2014 19:30:42 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img1.jpg" ]
                        },
                        {
                            id : 17,
                            read : true,
                            user_id : 11,
                            title : "Et culpa mollit aute proident elit.",
                            contents : "Ut proident labore ipsum tempor fugiat reprehenderit nostrud quis fugiat Lorem ullamco. Cupidatat eu aliqua eu proident cillum nisi qui do tempor esse aliqua reprehenderit cupidatat velit. Officia officia commodo fugiat sit ipsum id aliqua magna cillum cupidatat est. Enim minim Lorem adipisicing et nulla incididunt nisi consequat aute nostrud. Pariatur laborum adipisicing excepteur exercitation. Adipisicing nisi ut laborum consectetur veniam magna. Amet aute officia exercitation sunt consequat dolor.\r\n",
                            from : "Luz Mccullough",
                            received_on : "Sun Feb 08 2015 05:40:31 GMT+0000 (UTC)",
                            favorite : false,
                            has_attachments : false
                        },
                        {
                            id : 18,
                            read : true,
                            user_id : 12,
                            title : "Sunt labore qui velit nulla officia laboris do.",
                            contents : "Amet dolor adipisicing sint eiusmod culpa cillum velit nisi anim excepteur duis Lorem amet aute. Incididunt est esse ipsum aute mollit nulla nisi sint aliquip nulla tempor Lorem. Commodo pariatur magna sint sint.\r\n",
                            from : "Hebert Nielsen",
                            received_on : "Fri Jul 18 2014 05:56:32 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img3.jpg", "img2.jpg" ]
                        },
                        {
                            id : 19,
                            read : false,
                            user_id : 14,
                            title : "Sit laboris dolore esse excepteur dolore labore ea quis cupidatat amet elit cillum tempor et.",
                            contents : "Proident eiusmod culpa ad cillum enim aute in adipisicing aliquip officia id. Ad reprehenderit dolor sit est. Quis irure velit velit id nisi eu incididunt quis laboris. Exercitation ea dolore minim id. Quis eu pariatur proident veniam. Eiusmod amet cillum ullamco ad adipisicing dolore est laboris quis adipisicing sunt reprehenderit.\r\n",
                            from : "Francisca Clayton",
                            received_on : "Fri Jan 09 2015 11:47:46 GMT+0000 (UTC)",
                            favorite : true,
                            has_attachments : true,
                            attachments : [ "img4.jpg", "img2.jpg" ]
                        } ]
                }, 0, 0, 0, 0, 0, 0, [ Admin.data.email, "Inbox" ], 0);

// -----------
Ext.create("Admin.data.marketshare.MultiYear", Admin.data.Simulated, {
    data : [ {
        xvalue : 1997,
        y1value : 281,
        y2value : 72,
        y3value : 269,
        y4value : 762
    }, {
        xvalue : 1981,
        y1value : 518,
        y2value : 999,
        y3value : 43,
        y4value : 310
    }, {
        xvalue : 1985,
        y1value : 38,
        y2value : 311,
        y3value : 942,
        y4value : 77
    }, {
        xvalue : 1984,
        y1value : 936,
        y2value : 415,
        y3value : 562,
        y4value : 412
    }, {
        xvalue : 1979,
        y1value : 978,
        y2value : 331,
        y3value : 927,
        y4value : 114
    }, {
        xvalue : 1982,
        y1value : 196,
        y2value : 240,
        y3value : 72,
        y4value : 888
    }, {
        xvalue : 1992,
        y1value : 481,
        y2value : 375,
        y3value : 139,
        y4value : 762
    }, {
        xvalue : 19895,
        y1value : 623,
        y2value : 999,
        y3value : 260,
        y4value : 310
    }, {
        xvalue : 1988,
        y1value : 328,
        y2value : 451,
        y3value : 542,
        y4value : 77
    }, {
        xvalue : 1980,
        y1value : 456,
        y2value : 615,
        y3value : 342,
        y4value : 412
    }, {
        xvalue : 1990,
        y1value : 788,
        y2value : 531,
        y3value : 489,
        y4value : 114
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.marketshare, "MultiYear" ], 0);

// -----------
Ext.create("Admin.data.marketshare.OneEntity", Admin.data.Simulated, {
    data : [ {
        xvalue : 2011,
        yvalue : 0.1,
        y1value : 0.2,
        y2value : 0.3,
        y3value : 0.1,
        y4value : 0,
        y5value : 1
    }, {
        xvalue : 2012,
        yvalue : 0.2,
        y1value : 0.4,
        y2value : 0.2,
        y3value : 0.2,
        y4value : 0,
        y5value : 1
    }, {
        xvalue : 2013,
        yvalue : 0.3,
        y1value : 0.2,
        y2value : 0.4,
        y3value : 0.3,
        y4value : 0,
        y5value : 1
    }, {
        xvalue : 2014,
        yvalue : 0.2,
        y1value : 0.4,
        y2value : 0.1,
        y3value : 0.2,
        y4value : 0,
        y5value : 1
    }, {
        xvalue : 2015,
        yvalue : 0.4,
        y1value : 0.3,
        y2value : 0.4,
        y3value : 0.4,
        y4value : 0,
        y5value : 1
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.marketshare, "OneEntity" ], 0);

// -----------
Ext.create("Admin.data.marketshare.OneYear", Admin.data.Simulated, {
    data : [ {
        xvalue : 2004,
        yvalue : 239
    }, {
        xvalue : 2005,
        yvalue : 402
    }, {
        xvalue : 2006,
        yvalue : 706
    }, {
        xvalue : 2007,
        yvalue : 432
    }, {
        xvalue : 2008,
        yvalue : 200
    }, {
        xvalue : 2009,
        yvalue : 763
    }, {
        xvalue : 2010,
        yvalue : 550
    }, {
        xvalue : 2011,
        yvalue : 630
    }, {
        xvalue : 2012,
        yvalue : 278
    }, {
        xvalue : 2013,
        yvalue : 312
    }, {
        xvalue : 2014,
        yvalue : 600
    }, {
        xvalue : 2015,
        yvalue : 283
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.marketshare, "OneYear" ], 0);

// -----------
Ext.create("Admin.data.marketshare.Yearwise", Admin.data.Simulated, {
    data : [ {
        xvalue : 2011,
        y1value : 517.27,
        y2value : 520.3,
        y3value : 291.41,
        y4value : 420.24
    }, {
        xvalue : 2012,
        y1value : 389.38,
        y2value : 632.31,
        y3value : 882.9,
        y4value : 771.08
    }, {
        xvalue : 2013,
        y1value : 287.24,
        y2value : 440.78,
        y3value : 549.99,
        y4value : 627.71
    }, {
        xvalue : 2014,
        y1value : 505.25,
        y2value : 631.07,
        y3value : 570.43,
        y4value : 583.67
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.marketshare, "Yearwise" ], 0);

// -----------
Ext.create("Admin.data.qg.Area", Admin.data.Simulated, {
    data : [ {
        xvalue : 0,
        yvalue : 100
    }, {
        xvalue : 10,
        yvalue : 141
    }, {
        xvalue : 20,
        yvalue : 120
    }, {
        xvalue : 30,
        yvalue : 156
    }, {
        xvalue : 40,
        yvalue : 130
    }, {
        xvalue : 50,
        yvalue : 160
    }, {
        xvalue : 60,
        yvalue : 120
    }, {
        xvalue : 70,
        yvalue : 135
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.qg, "Area" ], 0);

// -----------
Ext.create("Admin.data.qg.Bar", Admin.data.Simulated, {
    data : [ {
        xvalue : 0,
        yvalue : 600
    }, {
        xvalue : 10,
        yvalue : 748
    }, {
        xvalue : 20,
        yvalue : 569
    }, {
        xvalue : 30,
        yvalue : 850
    }, {
        xvalue : 40,
        yvalue : 500
    }, {
        xvalue : 50,
        yvalue : 753
    }, {
        xvalue : 60,
        yvalue : 707
    }, {
        xvalue : 70,
        yvalue : 640
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.qg, "Bar" ], 0);

// -----------
Ext.create("Admin.data.qg.Line", Admin.data.Simulated, {
    data : [ {
        xvalue : 0,
        yvalue : 250
    }, {
        xvalue : 10,
        yvalue : 300
    }, {
        xvalue : 20,
        yvalue : 270
    }, {
        xvalue : 30,
        yvalue : 370
    }, {
        xvalue : 40,
        yvalue : 400
    }, {
        xvalue : 50,
        yvalue : 350
    }, {
        xvalue : 60,
        yvalue : 410
    }, {
        xvalue : 70,
        yvalue : 450
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.qg, "Line" ], 0);

// -----------
Ext.create("Admin.data.qg.Pie", Admin.data.Simulated, {
    data : [ {
        xvalue : "Research",
        yvalue : 68
    }, {
        xvalue : "Finance",
        yvalue : 20
    }, {
        xvalue : "Marketing",
        yvalue : 12
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.qg, "Pie" ], 0);

// -----------
Ext.create(
                "Admin.data.search.Results",
                Admin.data.Simulated,
                {
                    data : [
                        {
                            id : 0,
                            content : "Exercitation sint id consectetur magna anim ut. Id consectetur excepteur aute est fugiat id pariatur incididunt. Sit qui labore minim laboris ullamco. Magna ad ut duis consectetur exercitation veniam laborum consequat. Laboris enim voluptate cupidatat sint quis sit esse id et ut labore mollit.\r\n",
                            title : "1. Ipsum incididunt amet pariatur nostrud anim ullamco id ullamco quis duis id reprehenderit cupidatat.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.et.com"
                        },
                        {
                            id : 1,
                            content : "Anim qui enim culpa non officia quis. Aliquip culpa consequat aute velit aliqua ex dolor elit laboris. Magna aute ut eiusmod officia sit commodo Lorem consectetur magna deserunt laborum dolor occaecat. Nisi voluptate et nostrud mollit consequat fugiat duis cupidatat esse occaecat ad est. Id mollit Lorem occaecat ea magna qui nisi sint incididunt. Incididunt nisi est nulla sit in ipsum velit duis. Sint enim sunt cillum consectetur voluptate velit cillum ullamco aute consequat tempor nostrud id.\r\n",
                            title : "Enim dolore et excepteur culpa nostrud.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.exercitation.com"
                        },
                        {
                            id : 2,
                            content : "Exercitation commodo qui minim eu sint laboris ut Lorem Lorem qui qui. Elit dolore ut minim ut esse aute et. Laborum qui minim fugiat ipsum adipisicing fugiat sunt. Fugiat fugiat est officia tempor veniam reprehenderit sunt nostrud dolor culpa adipisicing. Est excepteur et id amet tempor Lorem ut elit tempor adipisicing est elit proident ad.\r\n",
                            title : "Ullamco ea amet Lorem id nostrud eu ea cillum dolor.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.sint.com"
                        },
                        {
                            id : 3,
                            content : "Sunt elit officia dolor dolore tempor adipisicing dolor. Aliquip non incididunt nisi sunt commodo dolore et aliquip laborum qui nisi fugiat. Tempor sint esse ea officia duis eiusmod et magna non duis non pariatur id aute. Laboris tempor minim eu eiusmod in nisi eiusmod anim adipisicing cillum ex do adipisicing culpa. Nulla adipisicing consequat consectetur cupidatat. Sit velit id aute consequat qui Lorem. Laborum aute nulla consectetur in.\r\n",
                            title : "Proident occaecat irure irure laborum proident laborum aliquip velit enim cupidatat anim.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.reprehenderit.com"
                        },
                        {
                            id : 4,
                            content : "Ullamco ex excepteur laboris consequat eiusmod ad duis dolor commodo dolore elit ipsum laborum. Laborum ex duis irure qui reprehenderit eiusmod eiusmod. Aliqua anim sint nisi et cupidatat.\r\n",
                            title : "Officia incididunt ea proident consectetur aliquip tempor aliqua.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.aliqua.com"
                        },
                        {
                            id : 5,
                            content : "In occaecat consequat ullamco magna et duis eiusmod ullamco nostrud deserunt minim sit deserunt. Consequat nisi laboris ut tempor anim culpa tempor Lorem anim. Nisi eu Lorem magna occaecat ut reprehenderit qui dolore id excepteur quis. Qui do excepteur aliqua occaecat occaecat. Minim anim eu duis culpa do nostrud pariatur veniam amet mollit Lorem.\r\n",
                            title : "Culpa cillum eiusmod voluptate commodo incididunt proident officia id duis non.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.labore.com"
                        },
                        {
                            id : 6,
                            content : "Adipisicing voluptate ex cillum magna qui. Fugiat exercitation fugiat elit est voluptate labore proident sit occaecat ipsum. Elit deserunt ut cupidatat pariatur. Nisi ullamco veniam Lorem nostrud deserunt ipsum qui elit ipsum tempor commodo eiusmod. Tempor voluptate sunt tempor duis. Lorem aute nulla consequat qui ex eiusmod non in nisi. Id amet excepteur enim anim laborum id reprehenderit est.\r\n",
                            title : "Exercitation amet incididunt ipsum duis tempor deserunt deserunt esse Lorem officia anim enim.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.proident.com"
                        },
                        {
                            id : 7,
                            content : "Lorem tempor consectetur proident elit dolor. Commodo ex culpa nostrud labore occaecat dolor proident consequat eiusmod quis. Consequat do velit sit voluptate. Incididunt dolore aliqua officia minim consequat officia pariatur do reprehenderit consectetur ut ad. Ullamco elit dolor ut velit tempor eu incididunt. Commodo sit duis anim cillum velit magna nostrud. Amet sit aliquip veniam aute ea mollit amet cillum culpa et irure id.\r\n",
                            title : "Irure non dolore aliqua laboris.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.consequat.com"
                        },
                        {
                            id : 8,
                            content : "Do amet non aute amet. Magna ut dolore nisi nulla voluptate. Exercitation ullamco velit enim elit pariatur quis aliquip duis mollit ullamco cupidatat proident sint sit.\r\n",
                            title : "Sunt irure culpa consequat aute culpa ad culpa fugiat veniam cupidatat.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ea.com"
                        },
                        {
                            id : 9,
                            content : "Qui consectetur laborum laboris excepteur sit magna enim. Tempor nisi esse fugiat aute veniam sint aliquip dolor. Consequat minim cupidatat aliqua fugiat mollit nulla exercitation. Incididunt deserunt qui labore anim. Laborum in officia ea velit nisi excepteur ex excepteur consequat est quis adipisicing Lorem. Nulla aute ex proident duis cupidatat aute quis sit.\r\n",
                            title : "Officia aliqua sit cupidatat sint ad do tempor.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.dolore.com"
                        },
                        {
                            id : 10,
                            content : "Ut proident anim anim sint. Consequat mollit aliquip nisi qui veniam nulla quis eu eu sit enim tempor. Proident qui esse aliquip laborum do quis nulla consectetur sunt excepteur. Aute irure tempor velit aliquip id officia nulla. Aliquip officia est in culpa eu excepteur duis. Ullamco Lorem anim ipsum elit nisi aliqua et voluptate aliqua commodo duis tempor aute.\r\n",
                            title : "Dolor officia cillum pariatur mollit excepteur ex ut nostrud commodo pariatur id ullamco velit.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.anim.com"
                        },
                        {
                            id : 11,
                            content : "Ipsum exercitation elit anim occaecat duis. Cillum exercitation cillum officia sit. Incididunt ut occaecat ipsum ad magna deserunt quis excepteur elit tempor sit commodo magna. Mollit ipsum ipsum officia eu exercitation consectetur ex proident.\r\n",
                            title : "Tempor quis sit ipsum cillum.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.sunt.com"
                        },
                        {
                            id : 12,
                            content : "Id minim excepteur incididunt in mollit tempor enim. Ullamco est ut eiusmod aliqua id. Laboris cillum duis et reprehenderit voluptate aute aliqua sit exercitation aute Lorem. Consectetur pariatur amet ut dolore sint et commodo est minim ex veniam qui minim.\r\n",
                            title : "Nisi ad minim velit nulla commodo in aute.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ut.com"
                        },
                        {
                            id : 13,
                            content : "Cupidatat est sint commodo id esse sunt nostrud eiusmod aliqua. Occaecat elit est est fugiat ut commodo eu ut et non velit ex ut ut. Labore fugiat amet cillum dolore reprehenderit eu quis fugiat velit laboris esse exercitation eu. Proident veniam laboris nulla sint reprehenderit non non consequat non. Ea voluptate laboris cupidatat aute commodo proident mollit aliquip. Elit ullamco ea deserunt officia consequat minim labore.\r\n",
                            title : "Amet laboris cupidatat eu cupidatat aliquip labore nostrud anim culpa non in ipsum cillum aute.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.magna.com"
                        },
                        {
                            id : 14,
                            content : "Ullamco est exercitation amet amet est sint amet. Amet adipisicing aliquip non officia deserunt eu non aute ut do ullamco nisi. Et eu minim incididunt ad id enim id sunt excepteur non adipisicing duis adipisicing sunt. Fugiat nostrud ad sit duis nulla nostrud dolor magna cillum irure. Adipisicing pariatur ea elit proident velit. Consequat aute amet irure non.\r\n",
                            title : "Dolor culpa laboris aute aliqua aliquip dolore cupidatat nisi cillum.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.Lorem.com"
                        },
                        {
                            id : 15,
                            content : "In enim sunt enim quis ea minim culpa Lorem fugiat nulla. Eu reprehenderit nostrud qui cupidatat deserunt. Elit eu magna dolor commodo velit elit proident quis occaecat consectetur velit. Pariatur consectetur fugiat est sint irure quis nisi non. Do sit officia amet commodo. Aliquip est laboris sint occaecat ut. Voluptate ut adipisicing ipsum minim officia consequat minim excepteur sint fugiat occaecat.\r\n",
                            title : "Voluptate nulla fugiat excepteur culpa sint magna exercitation voluptate ullamco enim.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.nulla.com"
                        },
                        {
                            id : 16,
                            content : "Lorem incididunt anim Lorem velit veniam cupidatat adipisicing amet laborum qui esse tempor. Magna sit minim sint elit pariatur incididunt officia incididunt laborum culpa. Deserunt dolor laborum aliquip velit non. Adipisicing exercitation sint proident labore occaecat aliquip velit sit in culpa. Deserunt culpa culpa id elit tempor consequat ex sit nostrud et ullamco duis ad eiusmod. Dolor laboris eiusmod exercitation pariatur sunt mollit cillum minim ea.\r\n",
                            title : "Non exercitation non sint qui dolor magna ut est consectetur do occaecat cillum culpa.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.tempor.com"
                        },
                        {
                            id : 17,
                            content : "Excepteur culpa voluptate amet anim veniam nostrud magna. Consectetur deserunt id non fugiat voluptate proident consectetur elit anim excepteur. Velit veniam sit anim tempor.\r\n",
                            title : "Sunt aute culpa occaecat tempor ipsum excepteur id elit reprehenderit tempor dolor.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.occaecat.com"
                        },
                        {
                            id : 18,
                            content : "Deserunt fugiat aute proident veniam nostrud Lorem aliquip officia amet dolor mollit irure eu. Anim consectetur labore et pariatur quis voluptate pariatur incididunt irure adipisicing aliqua officia. Anim mollit consectetur est ipsum consequat quis anim adipisicing excepteur eiusmod cillum. Amet ex labore aliquip ipsum commodo veniam laborum. Quis enim sint occaecat aute occaecat qui non tempor est. Veniam mollit elit Lorem duis et cupidatat incididunt aliqua Lorem minim.\r\n",
                            title : "Irure adipisicing aliqua culpa elit ipsum quis est non.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.minim.com"
                        },
                        {
                            id : 19,
                            content : "Sit est nisi non veniam duis sit labore ad ex laboris ad in minim. Deserunt sit adipisicing id sint sit est labore nisi mollit commodo. Sit incididunt esse Lorem veniam aute enim proident excepteur dolor laboris voluptate.\r\n",
                            title : "Eu aliquip est reprehenderit quis qui ea fugiat magna eu in magna qui deserunt aliquip.",
                            thumbnail : "images/sample.jpg",
                            url : "www.nisi.com"
                        },
                        {
                            id : 20,
                            content : "In aliqua nostrud ad aliqua labore sit nisi. Enim esse quis proident minim voluptate sunt qui in sint veniam consequat qui aute proident. Deserunt esse adipisicing velit irure dolor qui. Commodo reprehenderit laborum enim voluptate laboris.\r\n",
                            title : "Deserunt in culpa in velit.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.duis.com"
                        },
                        {
                            id : 21,
                            content : "Est laboris amet sit consectetur dolore. Aliquip eiusmod sunt et consectetur proident pariatur deserunt labore. Cupidatat cupidatat consectetur ut consectetur reprehenderit laboris aliqua minim non mollit. Eu qui tempor labore cupidatat nulla sunt et adipisicing culpa enim irure irure. Dolore magna deserunt fugiat eu magna proident ipsum minim eu. Voluptate voluptate labore irure velit.\r\n",
                            title : "Consectetur sunt consectetur aute nostrud non occaecat laboris est fugiat ad aute nulla.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ea.com"
                        },
                        {
                            id : 22,
                            content : "Eiusmod consectetur occaecat laboris Lorem ut do fugiat fugiat veniam. Proident magna eu deserunt consequat deserunt nulla consectetur veniam culpa irure consectetur dolor sint. Nisi minim culpa laborum tempor labore sit do laborum et aliqua magna mollit quis do. Reprehenderit adipisicing consequat quis minim sunt proident ex in sit nulla. Nisi sit nostrud aliqua ea aliqua qui laborum deserunt nulla eu. Proident anim pariatur Lorem nisi et aliqua.\r\n",
                            title : "Velit laboris adipisicing dolor et id do cupidatat labore.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ullamco.com"
                        },
                        {
                            id : 23,
                            content : "Tempor aute reprehenderit laboris elit. Proident consectetur mollit deserunt esse ex mollit ut voluptate veniam ipsum officia. Ipsum cupidatat sit excepteur dolor quis veniam fugiat.\r\n",
                            title : "Veniam exercitation magna nulla exercitation.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ut.com"
                        },
                        {
                            id : 24,
                            content : "Anim reprehenderit aute id mollit magna magna mollit amet. Cillum ipsum occaecat dolor incididunt exercitation occaecat ut fugiat. In quis qui sit sint commodo non consequat enim aute eu duis est duis. Dolore velit ullamco officia do duis sit laborum culpa ullamco consectetur elit veniam tempor. Nostrud irure do eu enim cupidatat do deserunt Lorem eu voluptate deserunt. Consequat consectetur exercitation cillum velit mollit laboris culpa reprehenderit officia dolore eu commodo ullamco ad. Labore incididunt incididunt mollit commodo.\r\n",
                            title : "Excepteur nulla non velit ex quis minim culpa tempor proident voluptate consectetur.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.aliquip.com"
                        },
                        {
                            id : 25,
                            content : "Irure consequat enim irure officia elit ea aliqua nisi dolore incididunt amet. Incididunt duis exercitation qui velit officia dolore dolor reprehenderit ea et laborum velit qui dolor. Exercitation ea et nulla qui amet mollit nisi minim nostrud duis sit ut.\r\n",
                            title : "Reprehenderit eu ipsum adipisicing duis sint consequat.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.fugiat.com"
                        },
                        {
                            id : 26,
                            content : "In in consequat nisi fugiat et cupidatat irure. Sit qui occaecat enim officia voluptate aute esse nisi qui. Ex occaecat id dolor irure quis labore magna id veniam ex sint velit amet nisi. Magna ad nisi laborum occaecat proident. Incididunt officia ex commodo non reprehenderit. Voluptate cupidatat irure sunt duis sunt est magna ut fugiat. Adipisicing aliquip ut exercitation velit sit veniam.\r\n",
                            title : "Magna incididunt aliquip eiusmod dolor irure Lorem esse esse magna id nulla culpa magna.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.sit.com"
                        },
                        {
                            id : 27,
                            content : "Consectetur culpa sunt irure nisi sint. Aliquip qui exercitation fugiat est exercitation excepteur tempor incididunt qui et. Non ullamco irure excepteur dolor enim non consequat anim quis cupidatat incididunt commodo. Veniam dolore laborum laborum occaecat officia ullamco ea minim est dolor. Irure anim sint anim ullamco. Ex veniam incididunt laboris laborum sint quis consequat.\r\n",
                            title : "Aliquip veniam deserunt tempor commodo est sunt nostrud velit non occaecat eu qui laboris nostrud.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.elit.com"
                        },
                        {
                            id : 28,
                            content : "Ad ea minim mollit dolor ullamco nostrud. Aute consectetur eiusmod officia magna exercitation deserunt sit. Ad minim mollit labore ipsum ipsum minim pariatur elit deserunt. Officia incididunt sit excepteur minim eiusmod culpa eiusmod proident non excepteur fugiat. Laboris mollit exercitation fugiat laborum in ipsum aliquip. Ipsum elit ullamco enim anim pariatur in in velit ad labore magna.\r\n",
                            title : "Reprehenderit Lorem anim qui minim duis et Lorem minim occaecat.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.amet.com"
                        },
                        {
                            id : 29,
                            content : "Lorem aliquip Lorem et cupidatat officia excepteur. Incididunt reprehenderit magna quis laboris quis. Reprehenderit proident sunt esse anim eu quis eu quis do ut in qui labore consectetur. Deserunt quis sit aliqua anim duis sunt eu officia et ipsum nulla. Sunt do mollit exercitation tempor Lorem qui Lorem adipisicing velit non laborum adipisicing cillum enim. Laboris cillum consectetur voluptate fugiat tempor qui laboris aliqua duis adipisicing nostrud occaecat cillum sint.\r\n",
                            title : "Do reprehenderit exercitation Lorem fugiat sit voluptate est.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.elit.com"
                        },
                        {
                            id : 30,
                            content : "Et anim excepteur excepteur duis nulla ipsum esse. Minim proident elit consequat minim. Pariatur mollit dolor nisi pariatur magna commodo labore adipisicing mollit minim consequat nostrud voluptate. Amet Lorem est minim ut nulla nulla proident aute et id amet Lorem. Laboris ex sint irure reprehenderit eu non et id. Veniam quis dolor laboris dolor non culpa irure dolore quis duis esse ullamco in.\r\n",
                            title : "Ullamco consectetur voluptate labore tempor cillum excepteur amet minim eiusmod anim laboris et ut dolor.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.veniam.com"
                        },
                        {
                            id : 31,
                            content : "Sit sint dolor laborum elit ullamco elit enim qui id anim nulla. Ea qui fugiat consectetur laboris. Dolor veniam veniam qui commodo Lorem esse culpa adipisicing. In amet sint culpa amet nulla ad ipsum do Lorem velit dolor consectetur et.\r\n",
                            title : "Laboris ea aute eiusmod ex et minim esse sint sunt.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.laborum.com"
                        },
                        {
                            id : 32,
                            content : "Laboris velit deserunt deserunt consectetur velit deserunt voluptate consectetur sit. Adipisicing ad eiusmod esse reprehenderit cupidatat magna aliqua fugiat do. Sunt officia sint nulla qui voluptate commodo dolore voluptate laboris eiusmod incididunt sint sint. Sint quis consequat labore voluptate. Eiusmod eu fugiat dolor quis. Labore consequat anim officia culpa veniam eiusmod anim minim consequat enim pariatur qui sint.\r\n",
                            title : "Ad consectetur proident minim veniam laborum est elit qui ex tempor velit esse consectetur.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.dolor.com"
                        },
                        {
                            id : 33,
                            content : "Do reprehenderit laborum eu ut aliqua mollit aute tempor elit magna non dolore. Ea fugiat excepteur aliqua in do magna sint exercitation pariatur consectetur reprehenderit deserunt esse eu. Veniam adipisicing laboris est qui ad Lorem deserunt. Quis et voluptate velit magna ea ut laborum officia incididunt non.\r\n",
                            title : "Dolore veniam duis do aliqua amet velit est ullamco pariatur.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.nisi.com"
                        },
                        {
                            id : 34,
                            content : "Veniam excepteur nulla est elit eiusmod esse reprehenderit. Nulla ullamco sunt dolor tempor culpa cillum do exercitation sit quis est. Laborum non voluptate ad ex nisi mollit reprehenderit laborum fugiat nostrud eu nisi.\r\n",
                            title : "Consectetur ipsum esse sit duis duis occaecat ipsum sit esse adipisicing voluptate commodo.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.excepteur.com"
                        },
                        {
                            id : 35,
                            content : "Aute in voluptate consectetur cupidatat magna ipsum Lorem ullamco irure eu reprehenderit laboris. Sint mollit in cupidatat deserunt minim nisi irure irure est aliqua veniam eiusmod. Lorem occaecat incididunt in eiusmod labore duis magna voluptate sunt fugiat. Proident deserunt laborum aute veniam esse occaecat fugiat. Et id aute magna pariatur velit ex fugiat est eiusmod tempor ex enim ex amet.\r\n",
                            title : "Incididunt quis eiusmod adipisicing incididunt elit consectetur consequat et labore officia enim.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.ea.com"
                        },
                        {
                            id : 36,
                            content : "Duis officia irure et voluptate id officia irure minim aliquip. Voluptate non culpa commodo fugiat ea in. Excepteur fugiat occaecat non aliquip sint. Consequat nisi nisi velit occaecat dolore adipisicing duis tempor sint exercitation officia ullamco occaecat. Esse ad nulla labore nulla sunt mollit non.\r\n",
                            title : "Enim deserunt nisi aliquip irure incididunt cupidatat anim nostrud sint tempor.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.excepteur.com"
                        },
                        {
                            id : 37,
                            content : "Proident amet incididunt dolor et mollit et nulla. Anim id aliquip officia commodo et ipsum ipsum minim id tempor. Irure Lorem ipsum cupidatat quis culpa cupidatat dolor sit nostrud in adipisicing consectetur sint exercitation. Adipisicing nulla sit deserunt id incididunt eiusmod aliqua nulla ipsum id occaecat dolore ut. Nostrud aliqua deserunt anim do adipisicing id commodo. Do irure mollit laborum irure et magna cillum adipisicing tempor minim deserunt qui.\r\n",
                            title : "Non fugiat enim exercitation ex sint enim excepteur.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.cupidatat.com"
                        },
                        {
                            id : 38,
                            content : "Non dolor laborum fugiat culpa sunt reprehenderit sit labore excepteur consectetur sunt voluptate est. Ullamco adipisicing ea sint excepteur exercitation dolor in occaecat est aliquip commodo duis ea ad. Incididunt aliquip aliquip do qui dolore consequat dolore non non do.\r\n",
                            title : "Ex aliqua id aute occaecat consectetur id consectetur sint elit sit.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.minim.com"
                        },
                        {
                            id : 39,
                            content : "Enim nulla sit pariatur laboris reprehenderit et dolore occaecat cillum. Sint reprehenderit enim adipisicing aliquip cupidatat veniam aute exercitation tempor nulla. Do irure consequat fugiat amet nulla sit veniam dolor laborum do nisi.\r\n",
                            title : "Sunt elit cillum velit velit pariatur Lorem id.",
                            thumbnail : "resources/images/sample.jpg",
                            url : "www.culpa.com"
                        } ]
                }, 0, 0, 0, 0, 0, 0, [ Admin.data.search, "Results" ], 0);

// -----------
Ext.create("Admin.data.search.Users", Admin.data.Simulated, {
    data : [ {
        identifier : 1,
        fullname : "Archie Young",
        profile_pic : "1.png",
        email : "dwatkins@mydeo.name",
        subscription : "minima",
        joinDate : "10/16/2012",
        isActive : false
    }, {
        identifier : 2,
        fullname : "May Williams",
        profile_pic : "2.png",
        email : "jreid@babbleblab.com",
        subscription : "ab",
        joinDate : "6/13/2004",
        isActive : true
    }, {
        identifier : 3,
        fullname : "Kathryn Hill",
        profile_pic : "4.png",
        email : "dwatkins@mydeo.name",
        subscription : "totam",
        joinDate : "2/2/2007",
        isActive : true
    }, {
        identifier : 4,
        fullname : "Katherine Gomez",
        profile_pic : "3.png",
        email : "ewatkins@dazzlesphere.biz",
        subscription : "alias",
        joinDate : "2/22/2002",
        isActive : true
    }, {
        identifier : 5,
        fullname : "Della Allen",
        profile_pic : "1.png",
        email : "vgonzalez@yamia.gov",
        subscription : "et",
        joinDate : "1/16/2001",
        isActive : true
    }, {
        identifier : 6,
        fullname : "Maude Bailey",
        profile_pic : "2.png",
        email : "jgreene@skalith.com",
        subscription : "inventore",
        joinDate : "7/23/2006",
        isActive : true
    }, {
        identifier : 7,
        fullname : "Alma Allen",
        profile_pic : "4.png",
        email : "dwalker@jatri.info",
        subscription : "quo",
        joinDate : "11/24/2011",
        isActive : true
    }, {
        identifier : 8,
        fullname : "Floyd Taylor",
        profile_pic : "3.png",
        email : "ewatkins@dazzlesphere.biz",
        subscription : "eaque",
        joinDate : "12/11/2010",
        isActive : true
    }, {
        identifier : 9,
        fullname : "Archie Reed",
        profile_pic : "1.png",
        email : "dwalker@jatri.info",
        subscription : "sapiente",
        joinDate : "7/22/2001",
        isActive : true
    }, {
        identifier : 10,
        fullname : "Stanley Brooks",
        profile_pic : "1.png",
        email : "foliver@twitterbeat.org",
        subscription : "sed",
        joinDate : "10/3/2012",
        isActive : false
    }, {
        identifier : 11,
        fullname : "Beatrice Miller",
        profile_pic : "1.png",
        email : "walexander@meevee.name",
        subscription : "nemo",
        joinDate : "2/25/2003",
        isActive : false
    }, {
        identifier : 12,
        fullname : "Leon Jones",
        profile_pic : "4.png",
        email : "jreid@babbleblab.com",
        subscription : "est",
        joinDate : "7/14/2009",
        isActive : false
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.data.search, "Users" ], 0);

// -----------
Ext.create("Admin.model.Base", Ext.data.Model, {
    schema : {
        namespace : "Admin.model"
    }
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "Base" ], 0);

// -----------
Ext.create("Admin.model.ChatMessages", Admin.model.Base, {
    fields : [ {
        type : "string",
        name : "message"
    }, {
        type : "string",
        defaultValue : "user",
        name : "sender"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "ChatMessages" ], 0);

// -----------
Ext.create("Admin.model.DataXY", Admin.model.Base, {
    fields : [ {
        name : "xvalue"
    }, {
        name : "yvalue"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "DataXY" ], 0);

// -----------
Ext.create("Admin.model.FriendsList", Admin.model.Base, {
    fields : [ {
        name : "friendsName"
    }, {
        name : "connectionStatus"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "FriendsList" ], 0);

// -----------
Ext.create("Admin.model.MultiDataXY", Admin.model.Base, {
    fields : [ {
        name : "xvalue"
    }, {
        name : "y1value"
    }, {
        name : "y2value"
    }, {
        name : "y3value"
    }, {
        name : "y4value"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "MultiDataXY" ], 0);

// -----------
Ext.create("Admin.model.PanelSetting", Admin.model.Base, {
    fields : [ {
        name : "title"
    }, {
        name : "subTitle"
    }, {
        name : "toggleStatus"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "PanelSetting" ], 0);

// -----------
Ext.create("Admin.model.PersonalInfo", Admin.model.Base, {
    fields : [ {
        name : "name"
    }, {
        name : "status"
    }, {
        name : "icon"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "PersonalInfo" ], 0);

// -----------
Ext.create("Admin.model.Subscription", Admin.model.Base, {
    fields : [ {
        type : "int",
        name : "id"
    }, {
        type : "string",
        name : "name"
    }, {
        type : "string",
        name : "subscription"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "Subscription" ], 0);

// -----------
Ext.create("Admin.model.YearwiseData", Admin.model.Base, {
    fields : [ {
        name : "year"
    }, {
        name : "data"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model, "YearwiseData" ], 0);

// -----------
Ext.create("Admin.model.email.Email", Admin.model.Base, {
    fields : [ {
        type : "int",
        name : "id"
    }, {
        name : "read"
    }, {
        type : "string",
        name : "title"
    }, {
        name : "user_id"
    }, {
        type : "string",
        name : "contents"
    }, {
        type : "string",
        name : "from"
    }, {
        name : "has_attachments"
    }, {
        name : "attachments"
    }, {
        name : "received_on"
    }, {
        name : "favorite"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model.email, "Email" ], 0);

// -----------
Ext.create("Admin.model.email.Friend", Admin.model.Base, {
    fields : [ {
        type : "int",
        name : "id"
    }, {
        type : "string",
        name : "name"
    }, {
        type : "string",
        name : "thumbnail"
    }, {
        type : "boolean",
        name : "online"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model.email, "Friend" ], 0);

// -----------
Ext.create("Admin.model.search.Result", Admin.model.Base, {
    fields : [ {
        type : "int",
        name : "id"
    }, {
        type : "string",
        name : "title"
    }, {
        type : "string",
        name : "thumbnail"
    }, {
        type : "string",
        name : "url"
    }, {
        type : "string",
        name : "content"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model.search, "Result" ], 0);

// -----------
Ext.create("Admin.model.search.User", Admin.model.Base, {
    fields : [ {
        type : "int",
        name : "identifier"
    }, {
        type : "string",
        name : "fullname"
    }, {
        type : "string",
        name : "email"
    }, {
        name : "subscription"
    }, {
        type : "date",
        name : "joinDate"
    }, {
        type : "boolean",
        name : "isActive"
    }, {
        name : "profile_pic"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.model.search, "User" ], 0);

// -----------
Ext.create("Admin.store.NavigationTree", Ext.data.TreeStore, {
    storeId : "NavigationTree",
    root : {
        expanded : true,
        children : [ {
            text : "Dashboard",
            view : "dashboard.Dashboard",
            leaf : true,
            iconCls : "right-icon new-icon x-fa fa-desktop",
            routeId : "dashboard"
        }, {
            text : "Email",
            view : "email.Email",
            iconCls : "right-icon hot-icon x-fa fa-send ",
            leaf : true,
            routeId : "email"
        }, {
            text : "Profile",
            view : "profile.UserProfile",
            leaf : true,
            iconCls : "x-fa fa-user",
            routeId : "profile"
        }, {
            text : "Search results",
            view : "search.Results",
            leaf : true,
            iconCls : "x-fa fa-search",
            routeId : "search"
        }, {
            text : "FAQ",
            view : "pages.FAQ",
            leaf : true,
            iconCls : "x-fa fa-question",
            routeId : "faq"
        }, {
            text : "Pages",
            expanded : false,
            selectable : false,
            iconCls : "x-fa fa-leanpub",
            routeId : "pages-parent",
            id : "pages-parent",
            children : [ {
                text : "Blank Page",
                view : "pages.BlankPage",
                leaf : true,
                iconCls : "x-fa fa-file-o",
                routeId : "pages.blank"
            }, {
                text : "404 Error",
                view : "pages.Error404Window",
                leaf : true,
                iconCls : "x-fa fa-exclamation-triangle",
                routeId : "pages.404"
            }, {
                text : "500 Error",
                view : "pages.Error500Window",
                leaf : true,
                iconCls : "x-fa fa-times-circle",
                routeId : "pages.500"
            }, {
                text : "Lock Screen",
                view : "authentication.LockScreen",
                leaf : true,
                iconCls : "x-fa fa-lock",
                routeId : "authentication.lockscreen"
            }, {
                text : "Login",
                view : "authentication.Login",
                leaf : true,
                iconCls : "x-fa fa-check",
                routeId : "authentication.login"
            }, {
                text : "Register",
                view : "authentication.Register",
                leaf : true,
                iconCls : "x-fa fa-pencil-square-o",
                routeId : "authentication.register"
            }, {
                text : "Password Reset",
                view : "authentication.PasswordReset",
                leaf : true,
                iconCls : "x-fa fa-lightbulb-o",
                routeId : "authentication.passwordreset"
            } ]
        }, {
            text : "Widgets",
            view : "widgets.Widgets",
            leaf : true,
            iconCls : "x-fa fa-flask",
            routeId : "widgets"
        }, {
            text : "Forms",
            view : "forms.Wizards",
            leaf : true,
            iconCls : "x-fa fa-edit",
            routeId : "forms"
        }, {
            text : "Charts",
            view : "charts.Charts",
            iconCls : "x-fa fa-pie-chart",
            leaf : true,
            routeId : "charts"
        } ]
    },
    fields : [ {
        name : "text"
    } ]
}, 0, 0, 0, 0, 0, 0, [ Admin.store, "NavigationTree" ], 0);

// -----------
Ext.create("Admin.store.email.Friends", Ext.data.Store, {
    model : "Admin.model.email.Friend",
    proxy : {
        type : "ajax",
        url : "~api/email/friends",
        reader : {
            type : "json",
            rootProperty : "data"
        }
    },
    sorters : {
        direction : "DESC",
        property : "online"
    }
}, 0, 0, 0, 0, [ "store.emailfriends" ], 0, [ Admin.store.email, "Friends" ], 0);

// -----------
Ext.create("Admin.store.email.Inbox", Ext.data.Store, {
    model : "Admin.model.email.Email",
    pageSize : 20,
    autoLoad : true,
    proxy : {
        type : "ajax",
        url : "~api/email/inbox",
        reader : {
            type : "json",
            rootProperty : "data"
        }
    }
}, 0, 0, 0, 0, [ "store.emailinbox" ], 0, [ Admin.store.email, "Inbox" ], 0);

// -----------
Ext.create("Admin.store.search.Users", Ext.data.Store, {
    model : "Admin.model.search.User",
    proxy : {
        type : "ajax",
        url : "~api/search/users",
        reader : {
            type : "json",
            rootProperty : "data"
        }
    },
    autoLoad : "true",
    sorters : {
        direction : "ASC",
        property : "fullname"
    }
}, 0, 0, 0, 0, [ "store.searchusers" ], 0, [ Admin.store.search, "Users" ], 0);

// -----------
Ext.create("Admin.store.search.Results", Ext.data.Store, {
    model : "Admin.model.search.Result",
    proxy : {
        type : "ajax",
        url : "~api/search/results",
        reader : {
            type : "json",
            rootProperty : "data"
        }
    },
    autoLoad : "true",
    sorters : {
        direction : "ASC",
        property : "title"
    }
}, 0, 0, 0, 0, [ "store.searchresults" ], 0, [ Admin.store.search, "Results" ], 0);



// -----------
Ext.create("Admin.view.charts.Area", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    iconCls : "x-fa fa-area-chart",
    title : "Area Chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "cartesian",
        colors : [ "#115fa6", "#94ae0a" ],
        insetPadding : 0,
        bind : {
            store : "{dashboardfulllinechartstore}"
        },
        innerPadding : {
            top : 10,
            left : 0,
            bottom : 0,
            right : 0
        },
        series : [ {
            type : "line",
            colors : [ "rgba(103, 144, 199, 0.6)" ],
            xField : "xvalue",
            yField : [ "y1value" ],
            fill : true,
            smooth : true
        }, {
            type : "line",
            colors : [ "rgba(238, 146, 156, 0.6)" ],
            xField : "xvalue",
            yField : [ "y2value" ],
            fill : true,
            smooth : true
        } ],
        interactions : [ {
            type : "panzoom"
        } ],
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "y1value", "y2value", "y3value" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ]
    } ]
}, 0, [ "chartsareapanel" ], [ "component", "box", "container", "panel", "chartsareapanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartsareapanel : true
}, [ "widget.chartsareapanel" ], 0, [ Admin.view.charts, "Area" ], 0);

// -----------
Ext.create("Admin.view.charts.Bar", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "Bar Chart",
    iconCls : "x-fa fa-bar-chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "cartesian",
        colors : [ "#6aa5db" ],
        insetPadding : 0,
        bind : {
            store : "{marketshareoneyear}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "yvalue" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "bar",
            xField : "xvalue",
            yField : [ "yvalue" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ]
}, 0, [ "chartsbarpanel" ], [ "component", "box", "container", "panel", "chartsbarpanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartsbarpanel : true
}, [ "widget.chartsbarpanel" ], 0, [ Admin.view.charts, "Bar" ], 0);

// -----------
Ext.create("Admin.view.charts.Charts", Ext.container.Container, {
    viewModel : {
        type : "charts"
    },
    id : "charts",
    layout : "responsivecolumn",
    defaults : {
        defaults : {
            animation : !Ext.isIE9m && Ext.os.is.Desktop
        }
    },
    items : [ {
        xtype : "chartsareapanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "chartspie3dpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "chartspolarpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "chartsstackedpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "chartsbarpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "chartsgaugepanel",
        responsiveCls : "big-50 small-100"
    } ]
}, 0, 0, [ "component", "box", "container" ], {
    component : true,
    box : true,
    container : true
}, 0, 0, [ Admin.view.charts, "Charts" ], 0);

// -----------
Ext.create("Admin.view.charts.ChartsController", Ext.app.ViewController, {}, 0, 0, 0, 0,
        [ "controller.charts" ], 0, [ Admin.view.charts, "ChartsController" ], 0);

// -----------
Ext.create("Admin.view.charts.ChartsModel", Ext.app.ViewModel, {
    stores : {
        marketshareoneyear : {
            model : "Admin.model.DataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/marketshare/oneyear",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        marketsharemultiyear : {
            model : "Admin.model.MultiDataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/marketshare/multiyear",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        gaugechartstore : {
            data : [ {
                position : 40
            } ],
            fields : [ {
                name : "position"
            } ]
        },
        radialchartstore : {
            model : "Admin.model.DataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/radial",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        marketshareoneentitystore : {
            model : "Admin.model.DataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/marketshare/oneentity",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        yearwisemarketsharestore : {
            model : "Admin.model.MultiDataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/marketshare/yearwise",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        piedatastore : {
            model : "Admin.model.DataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/pie",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        dashboardfulllinechartstore : {
            model : "Admin.model.MultiDataXY",
            autoLoad : true,
            proxy : {
                type : "ajax",
                url : "~api/dashboard/full",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.charts" ], 0, [ Admin.view.charts, "ChartsModel" ], 0);

// -----------
Ext.create("Admin.view.charts.Gauge", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "Gauge Chart",
    iconCls : "x-fa fa-wifi",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "polar",
        colors : [ "#6aa5db", "#aed581" ],
        insetPadding : 0,
        bind : {
            store : "{gaugechartstore}"
        },
        series : [ {
            type : "gauge",
            angleField : "position",
            needleLength : 100
        } ]
    } ]
}, 0, [ "chartsgaugepanel" ], [ "component", "box", "container", "panel", "chartsgaugepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartsgaugepanel : true
}, [ "widget.chartsgaugepanel" ], 0, [ Admin.view.charts, "Gauge" ], 0);

// -----------
Ext.create("Admin.view.charts.Line", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "Line Chart",
    iconCls : "x-fa fa-line-chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "cartesian",
        colors : [ "#6aa5db", "#94ae0a" ],
        insetPadding : 0,
        bind : {
            store : "{marketshareoneentitystore}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "yvalue", "y1value", "y2value", "y3value", "y4value", "y5value" ],
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "line",
            xField : "xvalue",
            yField : [ "yvalue" ]
        }, {
            type : "line",
            xField : "xvalue",
            yField : [ "y1value" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ]
}, 0, [ "chartslinepanel" ], [ "component", "box", "container", "panel", "chartslinepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartslinepanel : true
}, [ "widget.chartslinepanel" ], 0, [ Admin.view.charts, "Line" ], 0);

// -----------
Ext.create("Admin.view.charts.Pie", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "2D Pie Chart",
    iconCls : "x-fa fa-pie-chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "polar",
        colors : [ "#aed581", "#6aa5db", "#ee929c" ],
        insetPadding : 0,
        bind : {
            store : "{piedatastore}"
        },
        series : [ {
            type : "pie",
            label : {
                field : "xvalue",
                display : "rotate",
                contrast : true,
                font : "12px Open Sans",
                color : "#888"
            },
            xField : "yvalue"
        } ],
        interactions : [ {
            type : "rotate"
        } ]
    } ]
}, 0, [ "chartspiepanel" ], [ "component", "box", "container", "panel", "chartspiepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartspiepanel : true
}, [ "widget.chartspiepanel" ], 0, [ Admin.view.charts, "Pie" ], 0);

// -----------
Ext.create("Admin.view.charts.Pie3D", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "3D Pie Chart",
    iconCls : "x-fa fa-pie-chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "polar",
        colors : [ "#aed581", "#6aa5db", "#ee929c" ],
        interactions : "rotate",
        insetPadding : 0,
        bind : {
            store : "{piedatastore}"
        },
        series : [ {
            type : "pie3d",
            angleField : "yvalue",
            donut : 30
        } ]
    } ]
}, 0, [ "chartspie3dpanel" ], [ "component", "box", "container", "panel", "chartspie3dpanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartspie3dpanel : true
}, [ "widget.chartspie3dpanel" ], 0, [ Admin.view.charts, "Pie3D" ], 0);

// -----------
Ext.create("Admin.view.charts.Polar", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "Radial Chart",
    iconCls : "x-fa fa-dot-circle-o",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "polar",
        colors : [ "#6aa5db" ],
        insetPadding : 20,
        bind : {
            store : "{radialchartstore}"
        },
        axes : [ {
            type : "numeric",
            fields : [ "yvalue" ],
            grid : true,
            position : "radial"
        }, {
            type : "category",
            fields : [ "xvalue" ],
            grid : true,
            position : "angular"
        } ],
        series : [ {
            type : "radar",
            xField : "xvalue",
            yField : "yvalue"
        } ],
        interactions : [ {
            type : "rotate"
        } ]
    } ]
}, 0, [ "chartspolarpanel" ], [ "component", "box", "container", "panel", "chartspolarpanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    chartspolarpanel : true
}, [ "widget.chartspolarpanel" ], 0, [ Admin.view.charts, "Polar" ], 0);

// -----------
Ext.create("Admin.view.charts.Stacked", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    title : "Stacked Bar Chart",
    iconCls : "x-fa fa-bar-chart",
    height : 300,
    ui : "light",
    layout : "fit",
    headerPosition : "bottom",
    bodyPadding : "15 15 0 15",
    items : [ {
        xtype : "cartesian",
        colors : [ "#6aa5db", "#ee929c" ],
        insetPadding : 0,
        bind : {
            store : "{marketsharemultiyear}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "y1value", "y2value", "y3value" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "bar",
            xField : "xvalue",
            yField : [ "y2value", "y3value" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ]
}, 0, [ "chartsstackedpanel" ], [ "component", "box", "container", "panel", "chartsstackedpanel" ],
        {
            component : true,
            box : true,
            container : true,
            panel : true,
            chartsstackedpanel : true
        }, [ "widget.chartsstackedpanel" ], 0, [ Admin.view.charts, "Stacked" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Dashboard", Ext.container.Container, {
    id : "dashboard",
    controller : "dashboard",
    viewModel : {
        type : "dashboard"
    },
    layout : "responsivecolumn",
    listeners : {
        hide : "onHideView"
    },
    items : [ {
        xtype : "dashboardnetworkpanel",
        responsiveCls : "big-60 small-100"
    }, {
        xtype : "dashboardhddusagepanel",
        responsiveCls : "big-20 small-50"
    }, {
        xtype : "dashboardearningspanel",
        responsiveCls : "big-20 small-50"
    }, {
        xtype : "dashboardsalespanel",
        responsiveCls : "big-20 small-50"
    }, {
        xtype : "dashboardtopmoviepanel",
        responsiveCls : "big-20 small-50"
    }, {
        xtype : "dashboardweatherpanel",
        responsiveCls : "big-40 small-100"
    }, {
        xtype : "dashboardtodospanel",
        responsiveCls : "big-60 small-100"
    }, {
        xtype : "dashboardservicespanel",
        responsiveCls : "big-40 small-100"
    } ]
}, 0, 0, [ "component", "box", "container" ], {
    component : true,
    box : true,
    container : true
}, 0, 0, [ Admin.view.dashboard, "Dashboard" ], 0);

// -----------
Ext.create("Admin.view.dashboard.DashboardController", Ext.app.ViewController,
                {
                    onRefreshToggle : function(d, g, a){
                        var f = this, c = this.getViewModel().getStore(
                                "dashboardfulllinechartstore"), b = Ext.Array.from(c
                                && c.getData().items), h = b.length;
                        if (d.toggleValue) {
                            f.clearChartUpdates(a)
                        } else {
                            if (h) {
                                f.chartTaskRunner = f.chartTaskRunner
                                        || Ext.create("Ext.util.TaskRunner");
                                f.chartTaskRunner.start({
                                    run : function(){
                                        this.last_x += this.last_x - this.second_last_x;
                                        var e = this.items[0].data;
                                        this.store.removeAt(0);
                                        this.store.add({
                                            xvalue : e.xvalue,
                                            y1value : e.y1value,
                                            y2value : e.y2value
                                        });
                                        this.count++
                                    },
                                    store : c,
                                    count : 0,
                                    items : b,
                                    last_x : b[h - 1].data.xvalue,
                                    second_last_x : b[h - 2].data.xvalue,
                                    interval : 200
                                })
                            }
                        }
                        d.toggleValue = !d.toggleValue
                    },
                    clearChartUpdates : function(){
                        this.chartTaskRunner = Ext.destroy(this.chartTaskRunner)
                    },
                    onDestroy : function(){
                        this.clearChartUpdates();
                        this.callParent()
                    },
                    onHideView : function(){
                        this.clearChartUpdates()
                    }
                }, 0, 0, 0, 0, [ "controller.dashboard" ], 0, [
                    Admin.view.dashboard,
                    "DashboardController" ], 0);

// -----------
Ext.create("Admin.view.dashboard.DashboardModel", Ext.app.ViewModel, {
    stores : {
        "dashboard.QGAreaStore" : {
            autoLoad : true,
            model : "Admin.model.DataXY",
            proxy : {
                type : "ajax",
                url : "~api/qg/area",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        "dashboard.QGBarStore" : {
            autoLoad : true,
            model : "Admin.model.DataXY",
            proxy : {
                type : "ajax",
                url : "~api/qg/bar",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        "dashboard.QGLineStore" : {
            autoLoad : true,
            model : "Admin.model.DataXY",
            proxy : {
                type : "ajax",
                url : "~api/qg/line",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        "dashboard.QGPieStore" : {
            autoLoad : true,
            model : "Admin.model.DataXY",
            proxy : {
                type : "ajax",
                url : "~api/qg/pie",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        dashboardfulllinechartstore : {
            autoLoad : true,
            model : "Admin.model.MultiDataXY",
            proxy : {
                type : "ajax",
                url : "~api/dashboard/full",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        dashboardvisitorchartstore : {
            autoLoad : true,
            model : "Admin.model.MultiDataXY",
            proxy : {
                type : "ajax",
                url : "~api/dashboard/visitor",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        dashboardcouncechartstore : {
            autoLoad : true,
            model : "Admin.model.MultiDataXY",
            proxy : {
                type : "ajax",
                url : "~api/dashboard/counce",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        subscriptionstore : {
            autoLoad : true,
            model : "Admin.model.Subscription",
            proxy : {
                type : "ajax",
                url : "~api/subscriptions",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        dashboardtaskstore : {
            autoLoad : true,
            fields : [ {
                type : "int",
                name : "id"
            }, {
                type : "string",
                name : "task"
            }, {
                type : "boolean",
                name : "done"
            } ],
            proxy : {
                type : "ajax",
                url : "~api/dashboard/tasks",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.dashboard" ], 0, [ Admin.view.dashboard, "DashboardModel" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Earnings", Ext.Panel, {
    cls : "quick-graph-panel shadow-panel",
    height : 130,
    layout : "fit",
    headerPosition : "bottom",
    iconCls : "x-fa fa-dollar",
    title : "Earnings",
    items : [ {
        xtype : "cartesian",
        animation : !Ext.isIE9m && Ext.os.is.Desktop,
        background : "#35baf6",
        colors : [
            "#483D8B",
            "#94ae0a",
            "#a61120",
            "#ff8809",
            "#ffd13e",
            "#a61187",
            "#24ad9a",
            "#7c7474",
            "#a66111" ],
        bind : {
            store : "{dashboard.QGLineStore}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "yvalue" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "line",
            style : {
                stroke : "#FFFFFF",
                "stroke-width" : "2px"
            },
            xField : "xvalue",
            yField : [ "yvalue" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ],
    tools : [ {
        xtype : "tool",
        cls : "quick-graph-panel-tool x-fa fa-ellipsis-v"
    } ]
}, 0, [ "dashboardearningspanel" ], [
    "component",
    "box",
    "container",
    "panel",
    "dashboardearningspanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    dashboardearningspanel : true
}, [ "widget.dashboardearningspanel" ], 0, [ Admin.view.dashboard, "Earnings" ], 0);

// -----------
Ext.create("Admin.view.dashboard.HDDUsage", Ext.panel.Panel, {
    cls : "quick-graph-panel shadow-panel",
    height : 130,
    layout : "fit",
    headerPosition : "bottom",
    iconCls : "x-fa fa-database",
    title : "HDD Usage",
    tools : [ {
        xtype : "tool",
        cls : "quick-graph-panel-tool x-fa fa-ellipsis-v"
    } ],
    items : [ {
        xtype : "cartesian",
        animation : !Ext.isIE9m && Ext.os.is.Desktop,
        constrain : true,
        constrainHeader : true,
        background : "#70bf73",
        colors : [ "#a9d9ab" ],
        bind : {
            store : "{dashboard.QGAreaStore}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "yvalue" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "area",
            style : {
                stroke : "#FFFFFF",
                "stroke-width" : "2px"
            },
            useDarkerStrokeColor : false,
            xField : "xvalue",
            yField : [ "yvalue" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ]
}, 0, [ "dashboardhddusagepanel" ], [
    "component",
    "box",
    "container",
    "panel",
    "dashboardhddusagepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    dashboardhddusagepanel : true
}, [ "widget.dashboardhddusagepanel" ], 0, [ Admin.view.dashboard, "HDDUsage" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Members", Ext.grid.Panel, {
    cls : "dashboard-member-grid shadow-panel",
    bodyPadding : 15,
    scroll : "none",
    hideHeaders : true,
    title : "Members",
    bind : {
        store : "{subscriptionstore}"
    },
    columns : [ {
        xtype : "numbercolumn",
        cls : "dashboard-member-header-background",
        minHeight : 35,
        width : 20,
        dataIndex : "id",
        text : "#",
        format : "0,000"
    }, {
        xtype : "gridcolumn",
        cls : "dashboard-member-header-background",
        flex : 1,
        dataIndex : "name",
        text : "Name"
    }, {
        xtype : "gridcolumn",
        cls : "dashboard-member-header-background",
        flex : 1,
        dataIndex : "subscription",
        text : "Subscription",
        renderer : function(a){
            return "<span class='" + a + "'>" + a + "</span>"
        }
    }, {
        xtype : "actioncolumn",
        items : [ {
            xtype : "button",
            iconCls : "x-fa fa-pencil"
        }, {
            xtype : "button",
            iconCls : "x-fa fa-close"
        } ],
        cls : "dashboard-member-header-background",
        width : 100,
        align : "left",
        dataIndex : "bool",
        text : "Actions",
        tooltip : "edit ",
        margin : "0 4 0 0"
    } ],
    viewConfig : {
        cls : "dashboard-member-grid-view",
        width : "100%"
    }
}, 0, [ "dashboardmemberspanel" ], [
    "component",
    "box",
    "container",
    "panel",
    "tablepanel",
    "gridpanel",
    "grid",
    "dashboardmemberspanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    tablepanel : true,
    gridpanel : true,
    grid : true,
    dashboardmemberspanel : true
}, [ "widget.dashboardmemberspanel" ], 0, [ Admin.view.dashboard, "Members" ], 0);

// -----------
Ext.create(
                "Admin.view.dashboard.Network",
                Ext.panel.Panel,
                {
                    cls : "dashboard-main-chart shadow-panel",
                    height : 380,
                    bodyPadding : 15,
                    title : "Network",
                    layout : {
                        type : "vbox",
                        align : "stretch"
                    },
                    tools : [ {
                        xtype : "tool",
                        toggleValue : false,
                        cls : "x-fa fa-refresh dashboard-tools",
                        listeners : {
                            click : "onRefreshToggle"
                        },
                        width : 20,
                        height : 20
                    }, {
                        xtype : "tool",
                        cls : "x-fa fa-wrench dashboard-tools",
                        width : 20,
                        height : 20
                    } ],
                    items : [
                        {
                            xtype : "container",
                            flex : 1,
                            layout : "fit",
                            items : [ {
                                xtype : "cartesian",
                                animation : !Ext.isIE9m && Ext.os.is.Desktop,
                                insetPadding : 0,
                                bind : {
                                    store : "{dashboardfulllinechartstore}"
                                },
                                axes : [ {
                                    type : "category",
                                    fields : [ "xvalue" ],
                                    hidden : true,
                                    position : "bottom"
                                }, {
                                    type : "numeric",
                                    fields : [ "y1value", "y2value" ],
                                    grid : {
                                        odd : {
                                            fill : "#e8e8e8"
                                        }
                                    },
                                    hidden : true,
                                    position : "left"
                                } ],
                                series : [ {
                                    type : "line",
                                    colors : [ "rgba(103, 144, 199, 0.6)" ],
                                    useDarkerStrokeColor : false,
                                    xField : "xvalue",
                                    yField : [ "y1value" ],
                                    fill : true,
                                    smooth : true
                                }, {
                                    type : "line",
                                    colors : [ "rgba(238, 146, 156, 0.6)" ],
                                    useDarkerStrokeColor : false,
                                    xField : "xvalue",
                                    yField : [ "y2value" ],
                                    fill : true,
                                    smooth : true
                                } ],
                                interactions : [ {
                                    type : "panzoom"
                                } ]
                            } ]
                        },
                        {
                            xtype : "container",
                            cls : "graph-analysis-left",
                            height : 138,
                            layout : {
                                type : "hbox",
                                align : "stretch"
                            },
                            items : [
                                {
                                    xtype : "container",
                                    flex : 1,
                                    cls : "dashboard-graph-analysis-left",
                                    layout : {
                                        type : "vbox",
                                        align : "stretch"
                                    },
                                    items : [
                                        {
                                            xtype : "container",
                                            flex : 1,
                                            padding : "10 0 10 0",
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            },
                                            items : [
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "top-info-container",
                                                    html : '<div class="inner"><span class="x-fa fa-pie-chart"></span><span class="dashboard-analytics-percentage"> 25% </span>server load</div>',
                                                    padding : "15 10 10 0"
                                                },
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "top-info-container",
                                                    html : '<div class="inner"><span class="x-fa fa-user"></span><span class="dashboard-analytics-percentage"> 156 </span> online users</div>',
                                                    padding : "15 10 10 0"
                                                } ]
                                        },
                                        {
                                            xtype : "progressbar",
                                            flex : 1,
                                            cls : "left-top-text progressbar-no-text",
                                            height : 3,
                                            hideMode : "offsets",
                                            margin : "0 15 0 0",
                                            maxHeight : 5,
                                            minHeight : 3,
                                            value : 0.4
                                        },
                                        {
                                            xtype : "box",
                                            flex : 1,
                                            cls : "left-top-text",
                                            html : "Tip: Download the analytics mobile app for real time updates on the server.",
                                            padding : "15 5 5 0",
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            }
                                        } ]
                                },
                                {
                                    xtype : "container",
                                    flex : 1,
                                    cls : "graph-analysis-right",
                                    margin : "15 0 0 0",
                                    padding : "0 0 0 15",
                                    layout : {
                                        type : "vbox",
                                        align : "stretch"
                                    },
                                    itemPadding : "0 0 10 0",
                                    items : [
                                        {
                                            xtype : "container",
                                            flex : 1,
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            },
                                            padding : "0 0 10 0",
                                            items : [
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container",
                                                    html : "Visitors"
                                                },
                                                {
                                                    xtype : "container",
                                                    flex : 1,
                                                    alignTarget : "right",
                                                    cls : "graph-analysis-right-inner-container right-value",
                                                    layout : "fit",
                                                    items : [ {
                                                        xtype : "cartesian",
                                                        animation : !Ext.isIE9m
                                                                && Ext.os.is.Desktop,
                                                        minHeight : 50,
                                                        background : "rgba(255, 255, 255, 1)",
                                                        colors : [ "rgba(225,233,244, 0.8)" ],
                                                        insetPadding : {
                                                            top : 0,
                                                            left : 0,
                                                            right : 0,
                                                            bottom : 0
                                                        },
                                                        bind : {
                                                            store : "{dashboardvisitorchartstore}"
                                                        },
                                                        axes : [ {
                                                            type : "category",
                                                            fields : [ "xvalue" ],
                                                            hidden : true,
                                                            position : "bottom"
                                                        }, {
                                                            type : "numeric",
                                                            fields : [ "y1value" ],
                                                            grid : {
                                                                odd : {
                                                                    fill : "#e8e8e8"
                                                                }
                                                            },
                                                            hidden : true,
                                                            position : "left"
                                                        } ],
                                                        series : [ {
                                                            type : "area",
                                                            xField : "xvalue",
                                                            yField : [ "y1value" ]
                                                        } ],
                                                        interactions : [ {
                                                            type : "panzoom"
                                                        } ]
                                                    } ]
                                                } ]
                                        },
                                        {
                                            xtype : "container",
                                            flex : 1,
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            },
                                            padding : "0 0 10 0",
                                            items : [
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container",
                                                    html : "Bounce Rates"
                                                },
                                                {
                                                    xtype : "container",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container right-value",
                                                    layout : "fit",
                                                    items : [ {
                                                        xtype : "cartesian",
                                                        animation : !Ext.isIE9m
                                                                && Ext.os.is.Desktop,
                                                        minHeight : 50,
                                                        background : "rgba(255, 255, 255, 1)",
                                                        colors : [ "rgba(250,222,225, 0.8)" ],
                                                        insetPadding : {
                                                            top : 0,
                                                            left : 0,
                                                            right : 0,
                                                            bottom : 0
                                                        },
                                                        bind : {
                                                            store : "{dashboardcouncechartstore}"
                                                        },
                                                        axes : [ {
                                                            type : "category",
                                                            fields : [ "xvalue" ],
                                                            hidden : true,
                                                            position : "bottom"
                                                        }, {
                                                            type : "numeric",
                                                            fields : [ "y2value" ],
                                                            grid : {
                                                                odd : {
                                                                    fill : "#e8e8e8"
                                                                }
                                                            },
                                                            hidden : true,
                                                            position : "left"
                                                        } ],
                                                        series : [ {
                                                            type : "area",
                                                            xField : "xvalue",
                                                            yField : [ "y2value" ]
                                                        } ],
                                                        interactions : [ {
                                                            type : "panzoom"
                                                        } ]
                                                    } ]
                                                } ]
                                        },
                                        {
                                            xtype : "container",
                                            flex : 1,
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            },
                                            padding : "0 0 10 0",
                                            items : [
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container",
                                                    html : "Today's Sales"
                                                },
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container right-value",
                                                    html : "189,000"
                                                } ]
                                        },
                                        {
                                            xtype : "container",
                                            flex : 1,
                                            layout : {
                                                type : "hbox",
                                                align : "stretch"
                                            },
                                            padding : "0 0 10 0",
                                            items : [
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container",
                                                    html : "Broken Links"
                                                },
                                                {
                                                    xtype : "box",
                                                    flex : 1,
                                                    cls : "graph-analysis-right-inner-container right-value",
                                                    html : "4"
                                                } ]
                                        } ]
                                } ]
                        } ]
                }, 0, [ "dashboardnetworkpanel" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "dashboardnetworkpanel" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    dashboardnetworkpanel : true
                }, [ "widget.dashboardnetworkpanel" ], 0, [ Admin.view.dashboard, "Network" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Sales", Ext.panel.Panel, {
    cls : "quick-graph-panel shadow-panel",
    height : 130,
    layout : "fit",
    headerPosition : "bottom",
    iconCls : "x-fa fa-briefcase",
    title : "Sales",
    tools : [ {
        xtype : "tool",
        cls : "quick-graph-panel-tool x-fa fa-ellipsis-v"
    } ],
    items : [ {
        xtype : "cartesian",
        animation : !Ext.isIE9m && Ext.os.is.Desktop,
        height : 75,
        background : "#8561c5",
        colors : [ "#ffffff" ],
        bind : {
            store : "{dashboard.QGBarStore}"
        },
        axes : [ {
            type : "category",
            fields : [ "xvalue" ],
            hidden : true,
            position : "bottom"
        }, {
            type : "numeric",
            fields : [ "yvalue" ],
            grid : {
                odd : {
                    fill : "#e8e8e8"
                }
            },
            hidden : true,
            position : "left"
        } ],
        series : [ {
            type : "bar",
            xField : "xvalue",
            yField : [ "yvalue" ]
        } ],
        interactions : [ {
            type : "panzoom"
        } ]
    } ]
}, 0, [ "dashboardsalespanel" ],
        [ "component", "box", "container", "panel", "dashboardsalespanel" ], {
            component : true,
            box : true,
            container : true,
            panel : true,
            dashboardsalespanel : true
        }, [ "widget.dashboardsalespanel" ], 0, [ Admin.view.dashboard, "Sales" ], 0);

// -----------
Ext.create(
                "Admin.view.dashboard.Services",
                Ext.Panel,
                {
                    cls : "service-type shadow-panel",
                    height : 320,
                    bodyPadding : 15,
                    title : "Services",
                    layout : {
                        type : "hbox",
                        align : "stretch"
                    },
                    items : [
                        {
                            xtype : "container",
                            width : 140,
                            defaults : {
                                height : 126,
                                insetPadding : "7.5 7.5 7.5 7.5",
                                background : "rgba(255, 255, 255, 1)",
                                colors : [ "#6aa5dc", "#fdbf00", "#ee929d" ],
                                bind : {
                                    store : "{dashboard.QGPieStore}"
                                },
                                series : [ {
                                    type : "pie",
                                    label : {
                                        field : "xField",
                                        display : "rotate",
                                        contrast : true,
                                        font : "12px Arial"
                                    },
                                    useDarkerStrokeColor : false,
                                    xField : "yvalue",
                                    donut : 50,
                                    padding : 0
                                } ],
                                interactions : [ {
                                    type : "rotate"
                                } ]
                            },
                            items : [ {
                                xtype : "polar"
                            }, {
                                xtype : "polar"
                            } ]
                        },
                        {
                            xtype : "container",
                            flex : 1,
                            layout : {
                                type : "vbox",
                                align : "stretch"
                            },
                            items : [
                                {
                                    xtype : "component",
                                    data : {
                                        name : "Finance",
                                        value : "20%"
                                    },
                                    tpl : '<div class="left-aligned-div">{name}</div><div class="right-aligned-div">{value}</div>'
                                },
                                {
                                    xtype : "progressbar",
                                    cls : "bottom-indent service-finance",
                                    height : 4,
                                    minHeight : 4,
                                    value : 0.2
                                },
                                {
                                    xtype : "component",
                                    data : {
                                        name : "Research",
                                        value : "68%"
                                    },
                                    tpl : '<div class="left-aligned-div">{name}</div><div class="right-aligned-div">{value}</div>'
                                },
                                {
                                    xtype : "progressbar",
                                    cls : "bottom-indent service-research",
                                    height : 4,
                                    minHeight : 4,
                                    value : 0.68
                                },
                                {
                                    xtype : "component",
                                    data : {
                                        name : "Marketing",
                                        value : "12%"
                                    },
                                    tpl : '<div class="left-aligned-div">{name}</div><div class="right-aligned-div">{value}</div>'
                                },
                                {
                                    xtype : "progressbar",
                                    cls : "bottom-indent service-marketing",
                                    height : 4,
                                    value : 0.12
                                },
                                {
                                    xtype : "component",
                                    html : '<div class="services-text">The year 2015 saw a significant change in the job market for the industry. With increasing goverment expenditure on research & development, jobs in the research sector rose to 68% from 47% in the previous financial year. Share of jobs in the finance sector remained more or less constant while that in marketing sector dropped to 12%. The reduction in marketing jobs is attributed to increasing use of online advertising in recent years, which is largely automated.</div><div class="services-legend"><span><div class="legend-finance"></div>Finance</span><span><div class="legend-research"></div>Research</span><span><div class="legend-marketing"></div>Marketing</span><div>'
                                } ]
                        } ]
                }, 0, [ "dashboardservicespanel" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "dashboardservicespanel" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    dashboardservicespanel : true
                }, [ "widget.dashboardservicespanel" ], 0, [ Admin.view.dashboard, "Services" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Todos", Ext.panel.Panel, {
    cls : "todo-list shadow-panel",
    title : "TODO List",
    height : 320,
    bodyPadding : 15,
    items : [ {
        xtype : "gridpanel",
        cls : "dashboard-todo-list",
        header : false,
        title : "My Grid Panel",
        hideHeaders : true,
        scroll : "none",
        bind : {
            store : "{dashboardtaskstore}"
        },
        columns : [ {
            xtype : "gridcolumn",
            dataIndex : "task",
            text : "Task",
            flex : 1
        } ],
        dockedItems : [ {
            xtype : "container",
            layout : "hbox",
            dock : "bottom",
            padding : "10 0 0 0",
            items : [ {
                xtype : "textfield",
                flex : 1,
                fieldLabel : "Add Task",
                hideLabel : true,
                width : 540,
                emptyText : "Add New Task"
            }, {
                xtype : "button",
                ui : "soft-green",
                width : 40,
                iconCls : "x-fa fa-plus",
                margin : "0 0 0 10"
            } ]
        } ],
        selModel : {
            selType : "checkboxmodel"
        }
    } ]
}, 0, [ "dashboardtodospanel" ],
        [ "component", "box", "container", "panel", "dashboardtodospanel" ], {
            component : true,
            box : true,
            container : true,
            panel : true,
            dashboardtodospanel : true
        }, [ "widget.dashboardtodospanel" ], 0, [ Admin.view.dashboard, "Todos" ], 0);

// -----------
Ext.create("Admin.view.dashboard.TopMovie", Ext.panel.Panel, {
    cls : "quick-graph-panel shadow-panel",
    height : 130,
    layout : "fit",
    headerPosition : "bottom",
    iconCls : "x-fa fa-video-camera",
    title : "Top Movie",
    tools : [ {
        xtype : "tool",
        cls : "quick-graph-panel-tool x-fa fa-ellipsis-v"
    } ],
    items : [ {
        xtype : "polar",
        animation : !Ext.isIE9m && Ext.os.is.Desktop,
        height : 75,
        background : "#33abaa",
        colors : [
            "#115fa6",
            "#94ae0a",
            "#a61120",
            "#ff8809",
            "#ffd13e",
            "#a61187",
            "#24ad9a",
            "#7c7474",
            "#a66111" ],
        radius : 100,
        bind : {
            store : "{dashboard.QGPieStore}"
        },
        series : [ {
            type : "pie",
            colors : [ "#ffffff" ],
            label : {
                field : "x",
                display : "rotate",
                contrast : true,
                font : "12px Arial"
            },
            xField : "yvalue"
        } ],
        interactions : [ {
            type : "rotate"
        } ]
    } ]
}, 0, [ "dashboardtopmoviepanel" ], [
    "component",
    "box",
    "container",
    "panel",
    "dashboardtopmoviepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    dashboardtopmoviepanel : true
}, [ "widget.dashboardtopmoviepanel" ], 0, [ Admin.view.dashboard, "TopMovie" ], 0);

// -----------
Ext.create(
                "Admin.view.dashboard.Weather",
                Ext.Component,
                {
                    border : false,
                    cls : "weather-panel shadow-panel",
                    height : 80,
                    data : {
                        icon : "cloud-icon.png",
                        forecast : "Partly Cloudy",
                        temperature : 25
                    },
                    tpl : '<div class="weather-image-container"><img src="resources/images/icons/{icon}" alt="{forecast}"/></div><div class="weather-details-container"><div>{temperature}&#176;</div><div>{forecast}</div></div>'
                }, 0, [ "dashboardweatherpanel" ], [ "component", "box", "dashboardweatherpanel" ],
                {
                    component : true,
                    box : true,
                    dashboardweatherpanel : true
                }, [ "widget.dashboardweatherpanel" ], 0, [ Admin.view.dashboard, "Weather" ], 0);

// -----------
Ext.create("Admin.view.dashboard.Widgets", Ext.Panel, {
    cls : "dashboard-widget-block shadow-panel",
    bodyPadding : 15,
    title : "Widgets",
    layout : {
        type : "vbox",
        align : "stretch"
    },
    items : [ {
        xtype : "slider",
        width : 400,
        fieldLabel : "Single Slider",
        value : 40
    }, {
        xtype : "tbspacer",
        flex : 0.3
    }, {
        xtype : "multislider",
        width : 400,
        fieldLabel : "Range Slider",
        values : [ 10, 40 ]
    }, {
        xtype : "tbspacer",
        flex : 0.3
    }, {
        xtype : "pagingtoolbar",
        width : 360,
        displayInfo : false
    }, {
        xtype : "tbspacer",
        flex : 0.3
    }, {
        xtype : "progressbar",
        cls : "widget-progressbar",
        value : 0.4
    }, {
        xtype : "tbspacer"
    } ]
}, 0, [ "dashboardwidgetspanel" ], [
    "component",
    "box",
    "container",
    "panel",
    "dashboardwidgetspanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    dashboardwidgetspanel : true
}, [ "widget.dashboardwidgetspanel" ], 0, [ Admin.view.dashboard, "Widgets" ], 0);

// -----------
Ext.create("Admin.view.email.Compose", Ext.form.Panel, {
    viewModel : {
        type : "emailcompose"
    },
    controller : "emailcompose",
    cls : "email-compose",
    layout : {
        type : "vbox",
        align : "stretch"
    },
    bodyPadding : 10,
    scrollable : true,
    defaults : {
        labelWidth : 60,
        labelSeparator : ""
    },
    items : [ {
        xtype : "textfield",
        fieldLabel : "To"
    }, {
        xtype : "textfield",
        fieldLabel : "Subject"
    }, {
        xtype : "htmleditor",
        flex : 1,
        minHeight : 100,
        labelAlign : "top",
        fieldLabel : "Message"
    } ],
    bbar : {
        overflowHandler : "menu",
        items : [ {
            xtype : "filefield",
            width : 400,
            labelWidth : 80,
            fieldLabel : "Attachment",
            labelSeparator : "",
            buttonConfig : {
                xtype : "filebutton",
                glyph : "",
                iconCls : "x-fa fa-cloud-upload",
                text : "Browse"
            }
        }, "->", {
            xtype : "button",
            ui : "soft-red",
            text : "Discard",
            handler : "onComposeDiscardClick"
        }, {
            xtype : "button",
            ui : "gray",
            text : "Save"
        }, {
            xtype : "button",
            ui : "soft-green",
            text : "Send"
        } ]
    }
}, 0, [ "emailcompose" ], [ "component", "box", "container", "panel", "form", "emailcompose" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    form : true,
    emailcompose : true
}, [ "widget.emailcompose" ], 0, [ Admin.view.email, "Compose" ], 0);

// -----------
Ext.create("Admin.view.email.ComposeViewController", Ext.app.ViewController, {
    onComposeDiscardClick : function(a){
        var b = a.up("window");
        if (b) {
            b.close()
        }
    }
}, 0, 0, 0, 0, [ "controller.emailcompose" ], 0, [ Admin.view.email, "ComposeViewController" ], 0);

// -----------
Ext.create("Admin.view.email.ComposeViewModel", Ext.app.ViewModel, {}, 0, 0, 0, 0,
        [ "viewmodel.emailcompose" ], 0, [ Admin.view.email, "ComposeViewModel" ], 0);

// -----------
Ext.create("Admin.view.email.DetailsViewModel", Ext.app.ViewModel, {}, 0, 0, 0, 0,
        [ "viewmodel.emaildetails" ], 0, [ Admin.view.email, "DetailsViewModel" ], 0);

// -----------
Ext.create("Admin.view.email.Details", Ext.form.Panel, {
    viewModel : {
        type : "emaildetails"
    },
    cls : "shadow-panel",
    bodyPadding : 10,
    layout : {
        type : "anchor",
        anchor : "100%"
    },
    listeners : {
        beforerender : "beforeDetailsRender"
    },
    tbar : [ {
        iconCls : "x-fa fa-angle-left",
        listeners : {
            click : "onBackBtnClick"
        }
    }, {
        iconCls : "x-fa fa-trash"
    }, {
        iconCls : "x-fa fa-exclamation-circle"
    }, {
        iconCls : "x-fa fa-print"
    }, {
        iconCls : "x-fa fa-forward"
    } ],
    bbar : {
        cls : "single-mail-action-button",
        defaults : {
            margin : "0 15 0 0"
        },
        items : [ "->", {
            ui : "gray",
            text : "Save"
        }, {
            ui : "soft-green",
            text : "Send"
        } ]
    },
    items : [
        {
            xtype : "container",
            height : 82,
            layout : {
                type : "hbox",
                align : "stretch"
            },
            items : [
                {
                    xtype : "image",
                    itemId : "userImage",
                    cls : "email-sender-img",
                    alt : "profileImage",
                    height : 80,
                    width : 80
                },
                {
                    xtype : "component",
                    flex : 1,
                    cls : "single-mail-email-subject",
                    data : {},
                    itemId : "emailSubjectContainer",
                    padding : 10,
                    tpl : [
                        '<div class="user-name">{from}</div>',
                        '<div class="user-info">{title}</div>' ]
                } ]
        },
        {
            xtype : "box",
            cls : "mail-body",
            itemId : "mailBody"
        },
        {
            xtype : "box",
            itemId : "attachments",
            cls : "attachment-container",
            data : null,
            tpl : [
                '<tpl for=".">',
                '<img class="single-mail-attachment" src="resources/images/{.}" ',
                'alt="profile image">',
                "</tpl>" ]
        },
        {
            xtype : "htmleditor",
            height : 250,
            fieldLabel : "Reply",
            labelAlign : "top",
            labelSeparator : ""
        } ]
}, 0, [ "emaildetails" ], [ "component", "box", "container", "panel", "form", "emaildetails" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    form : true,
    emaildetails : true
}, [ "widget.emaildetails" ], 0, [ Admin.view.email, "Details" ], 0);

// -----------
Ext.create("Admin.view.email.Email", Ext.container.Container, {
    controller : "email",
    viewModel : {
        type : "email"
    },
    itemId : "emailMainContainer",
    layout : {
        type : "hbox",
        align : "stretch"
    },
    margin : "20 0 0 20",
    items : [ {
        xtype : "container",
        itemId : "navigationPanel",
        layout : {
            type : "vbox",
            align : "stretch"
        },
        width : "30%",
        minWidth : 180,
        maxWidth : 240,
        defaults : {
            cls : "navigation-email",
            margin : "0 20 20 0"
        },
        items : [ {
            xtype : "emailmenu",
            listeners : {
                click : "onMenuClick"
            }
        }, {
            xtype : "emailfriendslist"
        } ]
    }, {
        xtype : "container",
        itemId : "contentPanel",
        margin : "0 20 20 0",
        flex : 1,
        layout : {
            type : "anchor",
            anchor : "100%"
        }
    } ]
}, 0, [ "email" ], [ "component", "box", "container", "email" ], {
    component : true,
    box : true,
    container : true,
    email : true
}, [ "widget.email" ], 0, [ Admin.view.email, "Email" ], 0);

// -----------
Ext.create("Admin.view.email.EmailController", Ext.app.ViewController, {
    init : function(){
        this.setCurrentView("emailinbox")
    },
    onBackBtnClick : function(){
        this.setCurrentView("emailinbox")
    },
    onMenuClick : function(b, a){
        if (a) {
            this.setCurrentView(a.routeId, a.params)
        }
    },
    setCurrentView : function(b, d){
        var c = this.getView().down("#contentPanel");
        if (!c || b === "" || (c.down() && c.down().xtype === b)) {
            return false
        }
        if (d && d.openWindow) {
            var a = Ext.apply({
                xtype : "emailwindow",
                items : [ Ext.apply({
                    xtype : b
                }, d.targetCfg) ]
            }, d.windowCfg);
            Ext.create(a)
        } else {
            Ext.suspendLayouts();
            c.removeAll(true);
            c.add(Ext.apply({
                xtype : b
            }, d));
            Ext.resumeLayouts(true)
        }
    },
    onGridCellItemClick : function(b, d, c, a){
        if (c > 1) {
            this.setCurrentView("emaildetails", {
                record : a
            })
        } else {
            if (c === 1) {
                a.set("favorite", !a.get("favorite"))
            }
        }
    },
    beforeDetailsRender : function(b){
        var a = b.record ? b.record : {};
        b.down("#mailBody").setHtml(a.get("contents"));
        b.down("#attachments").setData(a.get("attachments"));
        b.down("#emailSubjectContainer").setData(a.data ? a.data : {});
        b.down("#userImage").setSrc("resources/images/user-profile/" + a.get("user_id") + ".png")
    }
}, 0, 0, 0, 0, [ "controller.email" ], 0, [ Admin.view.email, "EmailController" ], 0);

// -----------
Ext.create("Admin.view.email.EmailModel", Ext.app.ViewModel, {}, 0, 0, 0, 0,
        [ "viewmodel.email" ], 0, [ Admin.view.email, "EmailModel" ], 0);

// -----------
Ext.create("Admin.view.email.FriendsList", Ext.menu.Menu, {
    viewModel : {
        type : "emailfriendslist"
    },
    controller : "emailfriendslist",
    title : "Friends",
    cls : "navigation-email",
    iconCls : "x-fa fa-group",
    floating : false
}, 0, [ "emailfriendslist" ], [
    "component",
    "box",
    "container",
    "panel",
    "menu",
    "emailfriendslist" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    menu : true,
    emailfriendslist : true
}, [ "widget.emailfriendslist" ], 0, [ Admin.view.email, "FriendsList" ], 0);

// -----------
Ext.create("Admin.view.email.FriendsListViewController", Ext.app.ViewController, {
    init : function(){
        var a = this, b = a.getViewModel().getStore("friends");
        b.on("load", function(c){
            c.sort()
        });
        b.on("sort", function(c){
            a.mutateData(c, c.getRange())
        });
        Ext.app.ViewController.prototype.init.apply(this, arguments)
    },
    mutateData : function(e, d){
        var c = this.getView(), b = [], a = d.length, f;
        for (f = 0; f < a; f++) {
            b.push({
                xtype : "menuitem",
                text : d[f].get("name"),
                cls : "font-icon " + (d[f].get("online") ? "online-user" : "offline-user")
            })
        }
        Ext.suspendLayouts();
        c.removeAll(true);
        c.add(b);
        Ext.resumeLayouts(true)
    }
}, 0, 0, 0, 0, [ "controller.emailfriendslist" ], 0, [
    Admin.view.email,
    "FriendsListViewController" ], 0);

// -----------
Ext.create("Admin.view.email.FriendsListViewModel", Ext.app.ViewModel, {
            stores : {
                friends : {
                    type : "emailfriends",
                    autoLoad : true
                }
            }
        }, 0, 0, 0, 0, [ "viewmodel.emailfriendslist" ], 0, [
            Admin.view.email,
            "FriendsListViewModel" ], 0);

// -----------
Ext.create("Admin.view.email.Inbox", Ext.grid.Panel, {
    cls : "email-inbox-panel shadow-panel",
    viewModel : {
        type : "emailinbox"
    },
    bind : {
        store : "{EmailInbox}"
    },
    viewConfig : {
        preserveScrollOnRefresh : true,
        preserveScrollOnReload : true
    },
    selModel : {
        selType : "checkboxmodel",
        checkOnly : true,
        showHeaderCheckbox : true
    },
    listeners : {
        cellclick : "onGridCellItemClick"
    },
    headerBorders : false,
    rowLines : false,
    columns : [ {
        dataIndex : "favorite",
        menuDisabled : true,
        text : '<span class="x-fa fa-heart"></span>',
        width : 40,
        renderer : function(a){
            return '<span class="x-fa fa-heart' + (a ? "" : "-o") + '"></span>'
        }
    }, {
        dataIndex : "from",
        text : "From",
        width : 140
    }, {
        dataIndex : "title",
        text : "Title",
        flex : 1
    }, {
        dataIndex : "has_attachments",
        text : '<span class="x-fa fa-paperclip"></span>',
        width : 40,
        renderer : function(a){
            return a ? '<span class="x-fa fa-paperclip"></span>' : ""
        }
    }, {
        xtype : "datecolumn",
        dataIndex : "received_on",
        width : 90,
        text : "Received"
    } ]
}, 0, [ "emailinbox" ], [
    "component",
    "box",
    "container",
    "panel",
    "tablepanel",
    "gridpanel",
    "grid",
    "emailinbox" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    tablepanel : true,
    gridpanel : true,
    grid : true,
    emailinbox : true
}, [ "widget.emailinbox" ], 0, [ Admin.view.email, "Inbox" ], 0);

// -----------
Ext.create("Admin.view.email.InboxViewModel", Ext.app.ViewModel, {
    stores : {
        EmailInbox : {
            type : "emailinbox"
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.emailinbox" ], 0, [ Admin.view.email, "InboxViewModel" ], 0);

// -----------
Ext.create("Admin.view.email.Menu", Ext.menu.Menu, {
    viewModel : {
        type : "emailmenu"
    },
    title : "Email",
    iconCls : "x-fa fa-group",
    floating : false,
    items : [ {
        routeId : "emailcompose",
        params : {
            openWindow : true,
            targetCfg : {},
            windowCfg : {
                title : "Compose Message"
            }
        },
        iconCls : "x-fa fa-edit",
        text : "Compose"
    }, {
        routeId : "emailinbox",
        iconCls : "x-fa fa-inbox",
        text : "Inbox"
    }, {
        routeId : "",
        iconCls : "x-fa fa-check-circle",
        text : "Sent Mail"
    }, {
        routeId : "",
        iconCls : "x-fa fa-exclamation-circle",
        text : "Spam"
    }, {
        routeId : "",
        iconCls : "x-fa fa-trash-o",
        text : "Trash"
    } ]
}, 0, [ "emailmenu" ], [ "component", "box", "container", "panel", "menu", "emailmenu" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    menu : true,
    emailmenu : true
}, [ "widget.emailmenu" ], 0, [ Admin.view.email, "Menu" ], 0);

// -----------
Ext.create("Admin.view.email.MenuViewModel", Ext.app.ViewModel, {}, 0, 0, 0, 0,
        [ "viewmodel.emailmenu" ], 0, [ Admin.view.email, "MenuViewModel" ], 0);

// -----------
Ext.create("Admin.view.email.Window", Ext.window.Window, {
    autoShow : true,
    modal : true,
    layout : "fit",
    width : 200,
    height : 200,
    afterRender : function(){
        var a = this;
        Ext.window.Window.prototype.afterRender.apply(this, arguments);
        a.syncSize();
        Ext.on(a.resizeListeners = {
            resize : a.onViewportResize,
            scope : a,
            buffer : 50
        })
    },
    onDestroy : function(){
        Ext.un(this.resizeListeners);
        Ext.window.Window.prototype.onDestroy.call(this)
    },
    onViewportResize : function(){
        this.syncSize()
    },
    syncSize : function(){
        var b = Ext.Element.getViewportWidth(), a = Ext.Element.getViewportHeight();
        this.setSize(Math.floor(b * 0.9), Math.floor(a * 0.9));
        this.setXY([ Math.floor(b * 0.05), Math.floor(a * 0.05) ])
    }
}, 0, [ "emailwindow" ], [ "component", "box", "container", "panel", "window", "emailwindow" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    window : true,
    emailwindow : true
}, [ "widget.emailwindow" ], 0, [ Admin.view.email, "Window" ], 0);

// -----------
Ext.create("Admin.view.forms.WizardFormModel", Ext.app.ViewModel, {
    data : {
        atBeginning : true,
        atEnd : false
    }
}, 0, 0, 0, 0, [ "viewmodel.wizardform" ], 0, [ Admin.view.forms, "WizardFormModel" ], 0);

// -----------
Ext.create(
                "Admin.view.forms.WizardForm",
                Ext.panel.Panel,
                {
                    bodyPadding : 15,
                    height : 340,
                    layout : "card",
                    viewModel : {
                        type : "wizardform"
                    },
                    controller : "wizardform",
                    defaults : {
                        defaultFocus : "textfield:not([value]):focusable:not([disabled])",
                        defaultButton : "nextbutton"
                    },
                    tbar : {
                        reference : "progress",
                        cls : "wizardprogressbar",
                        defaults : {
                            disabled : true,
                            iconAlign : "top"
                        },
                        layout : {
                            pack : "center"
                        },
                        items : [ {
                            step : 0,
                            iconCls : "fa fa-info",
                            cls : "active",
                            text : "Account"
                        }, {
                            step : 1,
                            iconCls : "fa fa-user",
                            text : "Profile"
                        }, {
                            step : 2,
                            iconCls : "fa fa-home",
                            text : "Address"
                        }, {
                            step : 3,
                            iconCls : "fa fa-heart",
                            text : "Finish"
                        } ]
                    },
                    items : [
                        {
                            xtype : "form",
                            defaultType : "textfield",
                            defaults : {
                                labelWidth : 90,
                                labelAlign : "top",
                                labelSeparator : "",
                                submitEmptyText : false,
                                anchor : "100%"
                            },
                            items : [ {
                                emptyText : "Username must be unique."
                            }, {
                                emptyText : "ex: me@somewhere.com"
                            }, {
                                emptyText : "Enter a password",
                                inputType : "password",
                                cls : "wizard-form-break"
                            }, {
                                emptyText : "Passwords must match",
                                inputType : "password"
                            } ]
                        },
                        {
                            xtype : "form",
                            defaultType : "textfield",
                            defaults : {
                                labelWidth : 90,
                                labelAlign : "top",
                                labelSeparator : "",
                                submitEmptyText : false,
                                anchor : "100%"
                            },
                            items : [ {
                                emptyText : "First Name"
                            }, {
                                emptyText : "Last Name"
                            }, {
                                emptyText : "Company"
                            }, {
                                xtype : "fieldcontainer",
                                cls : "wizard-form-break",
                                fieldLabel : "MemberType",
                                defaultType : "radiofield",
                                defaults : {
                                    flex : 1
                                },
                                layout : "hbox",
                                items : [ {
                                    boxLabel : "Free",
                                    name : "MemberType",
                                    inputValue : "Free"
                                }, {
                                    boxLabel : "Personal",
                                    name : "MemberType",
                                    inputValue : "Perosnal"
                                }, {
                                    boxLabel : "Black",
                                    name : "MemberType",
                                    inputValue : "Business"
                                } ]
                            } ]
                        },
                        {
                            xtype : "form",
                            defaultType : "textfield",
                            defaults : {
                                labelWidth : 90,
                                labelAlign : "top",
                                labelSeparator : "",
                                submitEmptyText : false,
                                anchor : "100%"
                            },
                            items : [ {
                                emptyText : "Phone number"
                            }, {
                                emptyText : "Address"
                            }, {
                                emptyText : "City"
                            }, {
                                emptyText : "Postal Code / Zip Code"
                            } ]
                        },
                        {
                            xtype : "form",
                            items : [ {
                                html : "<h2>Thank You</h2><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>"
                            } ]
                        } ],
                    bbar : {
                        reference : "navigation-toolbar",
                        margin : 8,
                        items : [ "->", {
                            text : "Previous",
                            ui : "blue",
                            formBind : true,
                            bind : {
                                disabled : "{atBeginning}"
                            },
                            listeners : {
                                click : "onPreviousClick"
                            }
                        }, {
                            text : "Next",
                            ui : "blue",
                            formBind : true,
                            reference : "nextbutton",
                            bind : {
                                disabled : "{atEnd}"
                            },
                            listeners : {
                                click : "onNextClick"
                            }
                        } ]
                    }
                }, 0, [ "wizardform" ], [ "component", "box", "container", "panel", "wizardform" ],
                {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    wizardform : true
                }, [ "widget.wizardform" ], 0, [ Admin.view.forms, "WizardForm" ], 0);

// -----------
Ext.create(
                "Admin.view.forms.WizardFormController",
                Ext.app.ViewController,
                {
                    init : function(b){
                        var a = this.lookupReference("navigation-toolbar"), c = a.items.items, d = b.colorScheme;
                        if (d) {
                            c[1].setUI(d);
                            c[2].setUI(d)
                        }
                    },
                    onNextClick : function(b){
                        var a = b.up("panel");
                        a.getViewModel().set("atBeginning", false);
                        this.navigate(b, a, "next")
                    },
                    onPreviousClick : function(b){
                        var a = b.up("panel");
                        a.getViewModel().set("atEnd", false);
                        this.navigate(b, a, "prev")
                    },
                    navigate : function(f, b, j){
                        var h = b.getLayout(), a = this.lookupReference("progress"), g = b
                                .getViewModel(), c = a.items.items, l, e, d, k;
                        h[j]();
                        d = h.getActiveItem();
                        k = b.items.indexOf(d);
                        for (e = 0; e < c.length; e++) {
                            l = c[e];
                            if (k === l.step) {
                                l.addCls("active")
                            } else {
                                l.removeCls("active")
                            }
                            if (Ext.isIE8) {
                                l.btnIconEl.syncRepaint()
                            }
                        }
                        d.focus();
                        if (k === 0) {
                            g.set("atBeginning", true)
                        }
                        if (k === 3) {
                            g.set("atEnd", true)
                        }
                    }
                }, 0, 0, 0, 0, [ "controller.wizardform" ], 0, [
                    Admin.view.forms,
                    "WizardFormController" ], 0);

// -----------
Ext.create(
                "Admin.view.forms.WizardOne",
                Ext.panel.Panel,
                {
                    cls : "wizardone shadow-panel",
                    plugins : "responsive",
                    responsiveConfig : {
                        "width >= 1000" : {
                            layout : {
                                type : "box",
                                align : "stretch",
                                vertical : false
                            }
                        },
                        "width < 1000" : {
                            layout : {
                                type : "box",
                                align : "stretch",
                                vertical : true
                            }
                        }
                    },
                    items : [
                        {
                            xtype : "box",
                            minWidth : 200,
                            flex : 1,
                            cls : "bg-primary",
                            html : '<div class="eq-box-md text-center bg-primary pad-all"><div class="box-vmiddle pad-all"><h3 class="text-thin">Register Today</h3><span class="icon-wrap icon-wrap-lg icon-circle bg-trans-light"><i class="fa fa-gift fa-5x text-primary"></i></span><p>Members get <span class="text-lg text-bold">50%</span> more points, so register today and start earning points for savings on great rewards!</p><a class="btn btn-lg btn-primary btn-labeled fa fa-arrow-right" href="#faq"> Learn More...</a></div></div>'
                        },
                        {
                            xtype : "wizardform",
                            cls : "wizardone",
                            colorScheme : "blue",
                            flex : 1
                        } ]
                }, 0, [ "formswizardone" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "formswizardone" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    formswizardone : true
                }, [ "widget.formswizardone" ], 0, [ Admin.view.forms, "WizardOne" ], 0);

// -----------
Ext.create("Admin.view.forms.Wizards", Ext.container.Container, {
    cls : "wizards",
    defaultFocus : "wizardform",
    layout : "responsivecolumn",
    items : [ {
        xtype : "formswizardone",
        responsiveCls : "big-100"
    }, {
        xtype : "wizardform",
        cls : "wizardtwo shadow-panel",
        colorScheme : "soft-purple",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "wizardform",
        cls : "wizardthree shadow-panel",
        colorScheme : "soft-green",
        responsiveCls : "big-50 small-100"
    } ]
}, 0, [ "formswizardscontainer" ], [ "component", "box", "container", "formswizardscontainer" ], {
    component : true,
    box : true,
    container : true,
    formswizardscontainer : true
}, [ "widget.formswizardscontainer" ], 0, [ Admin.view.forms, "Wizards" ], 0);

// -----------
Ext.create("Admin.view.main.MainContainerWrap", Ext.container.Container, {
    scrollable : "y",
    layout : {
        type : "hbox",
        align : "stretchmax",
        animate : true,
        animatePolicy : {
            x : true,
            width : true
        }
    },
    beforeLayout : function(){
        var b = this, a = Ext.Element.getViewportHeight() - 64, c = b
                .getComponent("navigationTreeList");
        b.minHeight = a;
        c.setStyle({
            "min-height" : a + "px"
        });
        Ext.container.Container.prototype.beforeLayout.apply(this, arguments)
    }
}, 0, [ "maincontainerwrap" ], [ "component", "box", "container", "maincontainerwrap" ], {
    component : true,
    box : true,
    container : true,
    maincontainerwrap : true
}, [ "widget.maincontainerwrap" ], 0, [ Admin.view.main, "MainContainerWrap" ], 0);


// -----------
Ext.create(
                "Admin.view.pages.BlankPage",
                Ext.container.Container,
                {
                    anchor : "100% -1",
                    layout : {
                        type : "vbox",
                        pack : "center",
                        align : "center"
                    },
                    items : [ {
                        xtype : "box",
                        cls : "blank-page-container",
                        html : "<div class='fa-outer-class'><span class='x-fa fa-clock-o'></span></div><h1>Coming Soon!</h1><span class='blank-page-text'>Stay tuned for updates</span>"
                    } ]
                }, 0, [ "blankpage" ], [ "component", "box", "container", "blankpage" ], {
                    component : true,
                    box : true,
                    container : true,
                    blankpage : true
                }, [ "widget.blankpage" ], 0, [ Admin.view.pages, "BlankPage" ], 0);

// -----------
Ext.create(
                "Admin.view.pages.Error404Window",
                Ext.window.Window,
                {
                    autoShow : true,
                    cls : "error-page-container",
                    closable : false,
                    title : "Sencha",
                    titleAlign : "center",
                    maximized : true,
                    modal : true,
                    layout : {
                        type : "vbox",
                        align : "center",
                        pack : "center"
                    },
                    items : [ {
                        xtype : "container",
                        width : 400,
                        cls : "error-page-inner-container",
                        layout : {
                            type : "vbox",
                            align : "center",
                            pack : "center"
                        },
                        items : [
                            {
                                xtype : "label",
                                cls : "error-page-top-text",
                                text : "404"
                            },
                            {
                                xtype : "label",
                                cls : "error-page-desc",
                                html : '<div>Seems you\'ve hit a wall!</div><div>Try going back to our <a href="#dashboard"> Home page </a></div>'
                            },
                            {
                                xtype : "tbspacer",
                                flex : 1
                            } ]
                    } ]
                }, 0, [ "pageserror404window" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "window",
                    "pageserror404window" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    window : true,
                    pageserror404window : true
                }, [ "widget.pageserror404window" ], 0, [ Admin.view.pages, "Error404Window" ], 0);

// -----------
Ext.create(
                "Admin.view.pages.Error500Window",
                Ext.window.Window,
                {
                    autoShow : true,
                    cls : "error-page-container",
                    closable : false,
                    title : "Sencha",
                    titleAlign : "center",
                    maximized : true,
                    modal : true,
                    layout : {
                        type : "vbox",
                        align : "center",
                        pack : "center"
                    },
                    items : [ {
                        xtype : "container",
                        width : 600,
                        cls : "error-page-inner-container",
                        layout : {
                            type : "vbox",
                            align : "center",
                            pack : "center"
                        },
                        items : [
                            {
                                xtype : "label",
                                cls : "error-page-top-text",
                                text : "500"
                            },
                            {
                                xtype : "label",
                                cls : "error-page-desc",
                                html : '<div>Something went wrong and server could not process your request.</div><div>Try going back to our <a href="#dashboard"> Home page </a></div>'
                            },
                            {
                                xtype : "tbspacer",
                                flex : 1
                            } ]
                    } ]
                }, 0, [ "pageserror500window" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "window",
                    "pageserror500window" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    window : true,
                    pageserror500window : true
                }, [ "widget.pageserror500window" ], 0, [ Admin.view.pages, "Error500Window" ], 0);

// -----------
Ext.create(
                "Admin.view.pages.FAQ",
                Ext.container.Container,
                {
                    layout : {
                        type : "hbox",
                        align : "stretch"
                    },
                    padding : 10,
                    items : [
                        {
                            xtype : "panel",
                            cls : "faq-left-sidebar shadow-panel",
                            margin : 10,
                            header : false,
                            ui : "light",
                            responsiveConfig : {
                                "width < 1000" : {
                                    width : 0,
                                    visible : false
                                },
                                "width >= 1000 && width < 1600" : {
                                    width : 230,
                                    visible : true
                                },
                                "width >= 1600" : {
                                    width : 300,
                                    visible : true
                                }
                            },
                            items : [
                                {
                                    xtype : "panel",
                                    title : "Useful Tips",
                                    ui : "light",
                                    cls : "shadow-panel pages-faq-container",
                                    iconCls : "x-fa fa-lightbulb-o",
                                    html : "<p>We have created the following list of tips for our users. We hope that they will help you get the most of this website.</p> \n<ul class='faq-tips-list'><li class='pointone'>Point One</li><li class='pointtwo'>Point Two</li><li class='pointthree'>Point Three</li>\n<li class='pointfour'>Point Four</li></ul>",
                                    bodyPadding : 15
                                },
                                {
                                    xtype : "panel",
                                    bodyPadding : 20,
                                    ui : "light",
                                    cls : "shadow-panel pages-faq-container",
                                    iconCls : "x-fa fa-question",
                                    title : "Can't find the answer?",
                                    layout : {
                                        type : "vbox",
                                        align : "stretch"
                                    },
                                    items : [
                                        {
                                            xtype : "box",
                                            html : "<p>Help is just an email or a phone call away. If you cannot find what you are looking for on this page, our customer service representatives will be happy to help you.</p><br>"
                                        },
                                        {
                                            xtype : "button",
                                            ui : "soft-blue",
                                            margin : "20 20 20 20",
                                            text : "Contact Us"
                                        } ]
                                } ],
                            plugins : [ {
                                ptype : "responsive"
                            } ]
                        },
                        {
                            xtype : "panel",
                            ui : "light",
                            margin : 10,
                            flex : 1,
                            cls : "pages-faq-container shadow-panel",
                            iconCls : "x-fa fa-question-circle",
                            title : "FAQs",
                            bodyPadding : 15,
                            items : [
                                {
                                    xtype : "panel",
                                    cls : "FAQPanel",
                                    layout : "accordion",
                                    title : "General",
                                    height : 340,
                                    ui : "light",
                                    items : [
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "How can I access high resolution images?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "Can I download the application on my PC?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "How often does the database get updated?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "Can I use the downloaded images on a commercial website?",
                                            iconCls : "x-fa fa-caret-down"
                                        } ]
                                },
                                {
                                    xtype : "panel",
                                    cls : "FAQPanel",
                                    layout : "accordion",
                                    title : "Account",
                                    height : 340,
                                    bodyPadding : 10,
                                    ui : "light",
                                    items : [
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "What are the different membership plans?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "Can I change my plan in between?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "How can I deactivate my account?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "Can I transfer my account to another user?",
                                            iconCls : "x-fa fa-caret-down"
                                        } ]
                                },
                                {
                                    xtype : "panel",
                                    cls : "FAQPanel",
                                    layout : "accordion",
                                    title : "Payment",
                                    height : 300,
                                    bodyPadding : 10,
                                    ui : "light",
                                    items : [
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "What are the payment methods you accept?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "What is the refund policy?",
                                            iconCls : "x-fa fa-caret-down"
                                        },
                                        {
                                            xtype : "panel",
                                            html : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                            title : "How long does it take to process my payment?",
                                            iconCls : "x-fa fa-caret-down"
                                        } ]
                                } ]
                        } ]
                }, 0, [ "faq" ], [ "component", "box", "container", "faq" ], {
                    component : true,
                    box : true,
                    container : true,
                    faq : true
                }, [ "widget.faq" ], 0, [ Admin.view.pages, "FAQ" ], 0);

// -----------
Ext.create(
                "Admin.view.profile.Description",
                Ext.container.Container,
                {
                    height : 300,
                    layout : {
                        type : "vbox",
                        align : "stretch"
                    },
                    cls : "timeline-items-wrap user-profile-desc shadow-panel",
                    items : [
                        {
                            xtype : "box",
                            componentCls : "x-fa fa-home",
                            html : "San Jose, CA",
                            padding : "0 0 12 0"
                        },
                        {
                            xtype : "box",
                            componentCls : "x-fa fa-clock-o",
                            html : "Member since 1 years ago",
                            padding : "0 0 12 0"
                        },
                        {
                            xtype : "box",
                            componentCls : "x-fa fa-globe",
                            html : '<a href="#"\'>http://www.sencha-dash.com/</a>',
                            padding : "0 0 12 0"
                        },
                        {
                            xtype : "container",
                            flex : 1,
                            cls : "about-me-wrap",
                            html : '<h3 class="x-fa fa-user">About Me</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</p>'
                        },
                        {
                            xtype : "toolbar",
                            layout : {
                                type : "hbox",
                                pack : "center"
                            },
                            items : [ {
                                xtype : "box",
                                cls : "large-icon icon-padding",
                                componentCls : "x-fa fa-thumbs-up",
                                padding : "8 0 8 0"
                            }, {
                                xtype : "container",
                                layout : {
                                    type : "vbox",
                                    align : "center",
                                    pack : "center"
                                },
                                items : [ {
                                    xtype : "label",
                                    cls : "likes-value",
                                    text : "523"
                                }, {
                                    xtype : "label",
                                    cls : "likes-label",
                                    text : "Likes"
                                } ]
                            }, {
                                xtype : "box",
                                cls : "icon-padding",
                                componentCls : "x-fa fa-ellipsis-v",
                                padding : "8 0 8 0"
                            }, {
                                xtype : "box",
                                cls : "large-icon icon-padding",
                                componentCls : "x-fa fa-user-plus",
                                padding : "8 0 8 0"
                            }, {
                                xtype : "container",
                                layout : {
                                    type : "vbox",
                                    align : "center",
                                    pack : "center"
                                },
                                items : [ {
                                    xtype : "label",
                                    cls : "friends-value",
                                    text : "734"
                                }, {
                                    xtype : "label",
                                    cls : "friends-label",
                                    text : "Friends"
                                } ]
                            } ]
                        } ]
                }, 0, [ "profiledescriptionpanel" ], [
                    "component",
                    "box",
                    "container",
                    "profiledescriptionpanel" ], {
                    component : true,
                    box : true,
                    container : true,
                    profiledescriptionpanel : true
                }, [ "widget.profiledescriptionpanel" ], 0, [ Admin.view.profile, "Description" ],
                0);

// -----------
Ext.create(
                "Admin.view.profile.Notifications",
                Ext.grid.Panel,
                {
                    cls : "timeline-items-wrap shadow-panel",
                    bind : {
                        store : "{userNotificationStore}"
                    },
                    hideHeaders : true,
                    columns : [ {
                        xtype : "gridcolumn",
                        flex : 1,
                        dataIndex : "_id",
                        renderer : function(d, b, a, e){
                            var c = "<table><tr><td rowspan='3'><img src='resources/images/user-profile/5.png' alt='Smiley face' height='50' width='50'></td><td><h4>"
                                    + a.data.name
                                    + "</h4></td></tr><tr><td><div width='200px'>"
                                    + a.data.content + "</div></td></tr></table>";
                            switch (e) {
                            case 0:
                                c = "<div class=\"timeline-item\"><div class='timeline-day now'>Now</div><div class='profile-pic-wrap'><img src='resources/images/user-profile/6.png' alt='Smiley face'><div>30 Min ago</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='shared-by'><a href='#'>"
                                        + a.data.name
                                        + "</a> shared an image</div><img src='resources/images/img2.jpg' class='shared-img' alt='Smiley face'></div></div>";
                                break;
                            case 1:
                                c = "<div class='timeline-item'><div class='profile-pic-wrap'><img src='resources/images/user-profile/7.png' alt='Smiley face'><div>2 Hours ago</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='job-meeting'><a href='#'>Job Meeting</a></div><div>"
                                        + a.data.content + "</div></div></div>";
                                break;
                            case 2:
                                c = "<div class='timeline-item'><div class='profile-pic-wrap'><img src='resources/images/user-profile/8.png' alt='Smiley face'><div>3 Hours ago</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='shared-by'><a href='#'>"
                                        + a.data.name
                                        + "</a> commented on The Article</div><div class='article-comment'><span class='x-fa fa-quote-left'></span>"
                                        + a.data.content + "</div></div></div>";
                                break;
                            case 3:
                                c = "<div class='timeline-item'><div class='profile-pic-wrap'><img src='resources/images/user-profile/9.png' alt='Smiley face'><div>5 Hours ago</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='followed-by'><img src='resources/images/user-profile/10.png' alt='Smiley face'><div class='followed-by-inner'><a href='#'>"
                                        + a.data.name
                                        + "</a> followed you.</div></div></div></div>";
                                break;
                            case 4:
                                c = "<div class='timeline-item'><div class='timeline-day yesterday'>Yesterday</div><div class='profile-pic-wrap'><img src='resources/images/user-profile/12.png' alt='Smiley face'><div>15:45</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='shared-by'><a href='#'>Lorem ipsum dolor sit amet</a></div><div>"
                                        + a.data.content + "</div></div></div>";
                                break;
                            case 5:
                                c = "<div class='timeline-item'><div class='profile-pic-wrap'><img src='resources/images/user-profile/14.png' alt='Smiley face'><div>13:27</div></div><div class='contents-wrap'><span class='vertical-line'></span><div class='followed-by'><img src='resources/images/user-profile/1.png' alt='Smiley face'><div class='followed-by-inner'><a href='#'>"
                                        + a.data.name
                                        + "</a> Like The Article.</div></div></div></div>";
                                break
                            }
                            return c
                        }
                    } ]
                }, 0, [ "profilenotificationspanel" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "tablepanel",
                    "gridpanel",
                    "grid",
                    "profilenotificationspanel" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    tablepanel : true,
                    gridpanel : true,
                    grid : true,
                    profilenotificationspanel : true
                }, [ "widget.profilenotificationspanel" ], 0,
                [ Admin.view.profile, "Notifications" ], 0);

// -----------
Ext.create("Admin.view.profile.ShareUpdate", Ext.panel.Panel, {
    bodyPadding : 10,
    layout : "fit",
    cls : "share-panel shadow-panel",
    items : [ {
        xtype : "textareafield",
        emptyText : "What's on your mind?"
    } ],
    bbar : {
        defaults : {
            margin : "0 10 5 0"
        },
        items : [ {
            xtype : "button",
            iconCls : "x-fa fa-video-camera"
        }, {
            xtype : "button",
            iconCls : "x-fa fa-camera"
        }, {
            xtype : "button",
            iconCls : "x-fa fa-file"
        }, "->", {
            xtype : "button",
            text : "Share",
            ui : "soft-blue"
        } ]
    }
}, 0, [ "profilesharepanel" ], [ "component", "box", "container", "panel", "profilesharepanel" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    profilesharepanel : true
}, [ "widget.profilesharepanel" ], 0, [ Admin.view.profile, "ShareUpdate" ], 0);

// -----------
Ext.create("Admin.view.profile.Social", Ext.panel.Panel, {
    height : 300,
    bodyPadding : 10,
    layout : {
        type : "vbox",
        align : "middle"
    },
    cls : "social-panel shadow-panel",
    items : [ {
        xtype : "image",
        cls : "userProfilePic",
        height : 120,
        width : 120,
        alt : "profile-picture",
        src : "resources/images/user-profile/20.png"
    }, {
        xtype : "component",
        cls : "userProfileName",
        height : "",
        html : "Jessica Warren"
    }, {
        xtype : "component",
        cls : "userProfileDesc",
        html : "CO-FOUNDER, CEO"
    }, {
        xtype : "container",
        layout : "hbox",
        defaults : {
            xtype : "button",
            margin : 5
        },
        margin : 5,
        items : [ {
            ui : "blue",
            iconCls : "x-fa fa-facebook"
        }, {
            ui : "soft-cyan",
            iconCls : "x-fa fa-twitter"
        }, {
            ui : "soft-red",
            iconCls : "x-fa fa-google-plus"
        }, {
            ui : "soft-purple",
            iconCls : "x-fa fa-envelope"
        } ]
    }, {
        xtype : "button",
        scale : "large",
        width : 220,
        text : "Follow"
    } ]
}, 0, [ "profilesocialpanel" ], [ "component", "box", "container", "panel", "profilesocialpanel" ],
        {
            component : true,
            box : true,
            container : true,
            panel : true,
            profilesocialpanel : true
        }, [ "widget.profilesocialpanel" ], 0, [ Admin.view.profile, "Social" ], 0);

// -----------
Ext.create(
                "Admin.view.profile.Timeline",
                Ext.grid.Panel,
                {
                    cls : "timeline-items-wrap shadow-panel",
                    hideHeaders : true,
                    bind : {
                        store : "{userSharedItemsStore}"
                    },
                    columns : [ {
                        xtype : "gridcolumn",
                        dataIndex : "name",
                        flex : 1,
                        renderer : function(c, b, a){
                            if (a.data._id !== a.data.parent_id) {
                                return "<div class='comments sub-comments'><img src='resources/images/user-profile/1.png' alt='Smiley face' class='profile-icon'><div class='content-wrap'><div><span class='from-now'><span class='x-fa fa-clock-o'></span>3 Hours Ago</span><h4>"
                                        + a.data.name
                                        + "<span class='x-fa fa-mobile'></span></h4></div><div class='content'>"
                                        + a.data.content
                                        + "</div><div class='like-comment-btn-wrap'><button type='button' class='x-fa fa-thumbs-up' onclick=''></button><button type='button' class='x-fa fa-thumbs-down' onclick=''></button><button type='button' onclick='' class='x-fa fa-comments'></button></div></div></div>"
                            }
                            return "<div class='comments'><img src='resources/images/user-profile/15.png' alt='Smiley face' class='profile-icon'><div class='content-wrap'><div><span class='from-now'><span class='x-fa fa-clock-o'></span>3 Hours Ago</span><h4>"
                                    + a.data.name
                                    + "<span class='x-fa fa-mobile'></span></h4></div><div class='content'>"
                                    + a.data.content
                                    + "</div><div class='like-comment-btn-wrap'><button type='button' class='x-fa fa-thumbs-up' onclick=''></button><button type='button' class='x-fa fa-thumbs-down' onclick=''></button><button type='button' onclick='' class='x-fa fa-comments'></button></div></div></div>"
                        }
                    } ]
                }, 0, [ "profiletimelinepanel" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "tablepanel",
                    "gridpanel",
                    "grid",
                    "profiletimelinepanel" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    tablepanel : true,
                    gridpanel : true,
                    grid : true,
                    profiletimelinepanel : true
                }, [ "widget.profiletimelinepanel" ], 0, [ Admin.view.profile, "Timeline" ], 0);

// -----------
Ext.create("Admin.view.profile.UserProfile", Ext.container.Container, {
    controller : "userprofile",
    viewModel : {
        type : "userprofile"
    },
    cls : "userProfile-container",
    layout : "responsivecolumn",
    items : [ {
        xtype : "profilesharepanel",
        responsiveCls : "big-100"
    }, {
        xtype : "profilesocialpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "profiledescriptionpanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "profiletimelinepanel",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "profilenotificationspanel",
        responsiveCls : "big-50 small-100"
    } ]
}, 0, [ "userprofile" ], [ "component", "box", "container", "userprofile" ], {
    component : true,
    box : true,
    container : true,
    userprofile : true
}, [ "widget.userprofile" ], 0, [ Admin.view.profile, "UserProfile" ], 0);

// -----------
Ext.create("Admin.view.profile.UserProfileController", Ext.app.ViewController, {}, 0, 0, 0, 0,
        [ "controller.userprofile" ], 0, [ Admin.view.profile, "UserProfileController" ], 0);

// -----------
Ext.create("Admin.view.profile.UserProfileModel", Ext.app.ViewModel, {
    stores : {
        userSharedItemsStore : {
            autoLoad : true,
            fields : [ {
                name : "_id"
            }, {
                name : "parent_id"
            }, {
                name : "name"
            }, {
                name : "source"
            }, {
                name : "date"
            }, {
                name : "isActive"
            }, {
                name : "time"
            }, {
                name : "content"
            } ],
            proxy : {
                type : "ajax",
                url : "~api/usershareditems",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        },
        userNotificationStore : {
            autoLoad : true,
            fields : [ {
                name : "_id"
            }, {
                name : "name"
            }, {
                name : "content"
            }, {
                name : "date"
            }, {
                name : "time"
            } ],
            proxy : {
                type : "ajax",
                url : "~api/usernotifications",
                reader : {
                    type : "json",
                    rootProperty : "data"
                }
            }
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.userprofile" ], 0, [ Admin.view.profile, "UserProfileModel" ], 0);

// -----------
Ext.create(
                "Admin.view.search.Results",
                Ext.tab.Panel,
                {
                    controller : "searchresults",
                    viewModel : {
                        type : "searchresults"
                    },
                    cls : "shadow-panel",
                    activeTab : 0,
                    margin : 20,
                    items : [
                        {
                            xtype : "gridpanel",
                            cls : "allRecordsCls",
                            hideHeaders : true,
                            border : false,
                            title : "All",
                            routeId : "all",
                            bind : {
                                store : "{allresultsstore}"
                            },
                            viewConfig : {
                                preserveScrollOnRefresh : true,
                                stripeRows : false
                            },
                            columns : [ {
                                xtype : "gridcolumn",
                                renderer : function(d, b, a, e){
                                    var c = "<div class='resultsItemCls'><div class='resultsTitleCls'>"
                                            + a.data.title
                                            + "</div><div class='resultsUrlCls'><a href='#'>"
                                            + a.data.url
                                            + "</a></div><div class='resultsContentCls'>"
                                            + a.data.content + "</div></div>";
                                    if (e === 3) {
                                        c = "<div class='imageRowCls'><img src='resources/images/img2.jpg' alt='Smiley face' height='100' width='100' class='imagecls'><img src='resources/images/img2.jpg' alt='Smiley face' height='100' width='100' class='imagecls'></div>"
                                    }
                                    return c
                                },
                                dataIndex : "content",
                                flex : 1
                            } ],
                            dockedItems : [ {
                                xtype : "pagingtoolbar",
                                dock : "bottom",
                                displayInfo : true,
                                bind : {
                                    store : "{allresultsstore}"
                                }
                            } ]
                        },
                        {
                            xtype : "gridpanel",
                            cls : "user-grid",
                            title : "User Results",
                            routeId : "user",
                            bind : {
                                store : "{usersStore}"
                            },
                            columns : [
                                {
                                    xtype : "gridcolumn",
                                    width : 40,
                                    dataIndex : "identifier",
                                    text : "#"
                                },
                                {
                                    xtype : "gridcolumn",
                                    renderer : function(a){
                                        return "<img src='resources/images/user-profile/" + a
                                                + "' alt='Profile Pic' height='40px' width='40px'>"
                                    },
                                    width : 75,
                                    dataIndex : "profile_pic",
                                    text : "User"
                                },
                                {
                                    xtype : "gridcolumn",
                                    cls : "content-column",
                                    dataIndex : "fullname",
                                    text : "Name",
                                    flex : 1
                                },
                                {
                                    xtype : "gridcolumn",
                                    cls : "content-column",
                                    dataIndex : "email",
                                    text : "Email",
                                    flex : 1
                                },
                                {
                                    xtype : "datecolumn",
                                    cls : "content-column",
                                    width : 120,
                                    dataIndex : "joinDate",
                                    text : "Date"
                                },
                                {
                                    xtype : "gridcolumn",
                                    cls : "content-column",
                                    dataIndex : "subscription",
                                    text : "Subscription",
                                    flex : 1
                                },
                                {
                                    xtype : "actioncolumn",
                                    items : [ {
                                        xtype : "button",
                                        iconCls : "x-fa fa-pencil"
                                    }, {
                                        xtype : "button",
                                        iconCls : "x-fa fa-close"
                                    }, {
                                        xtype : "button",
                                        iconCls : "x-fa fa-ban"
                                    } ],
                                    cls : "content-column",
                                    width : 120,
                                    dataIndex : "bool",
                                    text : "Actions",
                                    tooltip : "edit "
                                } ],
                            dockedItems : [ {
                                xtype : "pagingtoolbar",
                                dock : "bottom",
                                itemId : "userPaginationToolbar",
                                displayInfo : true,
                                bind : {
                                    store : "{usersStore}"
                                }
                            } ]
                        },
                        {
                            xtype : "gridpanel",
                            cls : "email-inbox-panel",
                            itemId : "messagesGrid",
                            hideHeaders : true,
                            title : "Messages",
                            routeId : "messages",
                            bind : {
                                store : "{EmailInboxStore}"
                            },
                            columns : [ {
                                xtype : "gridcolumn",
                                renderer : function(a){
                                    if (a) {
                                        return '<span class="x-fa fa-heart"></span>'
                                    }
                                    return '<span class="x-fa fa-heart-o"></span>'
                                },
                                width : 45,
                                dataIndex : "favorite"
                            }, {
                                xtype : "gridcolumn",
                                dataIndex : "from",
                                flex : 1
                            }, {
                                xtype : "gridcolumn",
                                dataIndex : "title",
                                flex : 2
                            }, {
                                xtype : "gridcolumn",
                                renderer : function(a){
                                    return a ? '<span class="x-fa fa-paperclip"></span>' : ""
                                },
                                dataIndex : "has_attachments"
                            }, {
                                xtype : "datecolumn",
                                dataIndex : "received_on"
                            } ],
                            dockedItems : [ {
                                xtype : "pagingtoolbar",
                                dock : "bottom",
                                itemId : "pagingToolbar",
                                prependButtons : true,
                                bind : {
                                    store : "{EmailInboxStore}"
                                }
                            } ]
                        } ]
                }, 0, [ "searchresults" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "tabpanel",
                    "searchresults" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    tabpanel : true,
                    searchresults : true
                }, [ "widget.searchresults" ], 0, [ Admin.view.search, "Results" ], 0);

// -----------
Ext.create("Admin.view.search.ResultsController", Ext.app.ViewController, {}, 0, 0, 0, 0,
        [ "controller.searchresults" ], 0, [ Admin.view.search, "ResultsController" ], 0);

// -----------
Ext.create("Admin.view.search.ResultsModel", Ext.app.ViewModel, {
    stores : {
        allresultsstore : {
            type : "searchresults"
        },
        usersStore : {
            type : "searchusers"
        },
        EmailInboxStore : {
            type : "emailinbox"
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.searchresults" ], 0, [ Admin.view.search, "ResultsModel" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetA", Ext.panel.Panel, {
    cls : "admin-widget shadow-panel",
    items : [ {
        xtype : "image",
        cls : "widget-top-container-first-img",
        height : 66,
        width : 66,
        alt : "profile-image",
        src : "resources/images/user-profile/3.png"
    }, {
        xtype : "component",
        cls : "widget-top-first-container postion-class",
        height : 135
    }, {
        xtype : "container",
        cls : "widget-bottom-first-container postion-class",
        height : 135,
        padding : "30 0 0 0",
        layout : {
            type : "vbox",
            align : "center"
        },
        items : [ {
            xtype : "label",
            cls : "widget-name-text",
            html : "John Doe"
        }, {
            xtype : "label",
            html : "Administrator"
        }, {
            xtype : "toolbar",
            cls : "widget-tool-button",
            flex : 1,
            items : [ {
                ui : "soft-green",
                text : "Follow"
            }, {
                ui : "soft-blue",
                text : "Message"
            } ]
        } ]
    } ]
}, 0, [ "widget-a" ], [ "component", "box", "container", "panel", "widget-a" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    "widget-a" : true
}, [ "widget.widget-a" ], 0, [ Admin.view.widgets, "WidgetA" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetB", Ext.panel.Panel, {
    cls : "admin-widget shadow-panel",
    items : [ {
        xtype : "image",
        cls : "widget-top-container-first-img",
        height : 66,
        width : 66,
        alt : "profile-image",
        src : "resources/images/user-profile/4.png"
    }, {
        xtype : "component",
        cls : "widget-top-second-container postion-class",
        height : 135
    }, {
        xtype : "container",
        cls : "widget-bottom-first-container postion-class",
        height : 135,
        padding : "30 0 0 0",
        layout : {
            type : "vbox",
            align : "center"
        },
        items : [ {
            xtype : "label",
            cls : "widget-name-text",
            html : "Lucy Moon"
        }, {
            xtype : "label",
            html : "Web and Graphic designer"
        }, {
            xtype : "toolbar",
            flex : 1,
            items : [ {
                ui : "blue",
                iconCls : "x-fa fa-facebook"
            }, {
                ui : "soft-cyan",
                iconCls : "x-fa fa-twitter"
            }, {
                ui : "soft-red",
                iconCls : "x-fa fa-google-plus"
            }, {
                ui : "soft-purple",
                iconCls : "x-fa fa-envelope"
            } ]
        } ]
    } ]
}, 0, [ "widget-b" ], [ "component", "box", "container", "panel", "widget-b" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    "widget-b" : true
}, [ "widget.widget-b" ], 0, [ Admin.view.widgets, "WidgetB" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetC", Ext.panel.Panel, {
    cls : "admin-widget shadow-panel",
    items : [ {
        xtype : "image",
        cls : "widget-top-container-first-img",
        height : 66,
        width : 66,
        alt : "profile-image",
        src : "resources/images/user-profile/1.png"
    }, {
        xtype : "component",
        cls : "widget-top-first-third-container postion-class",
        height : 135
    }, {
        xtype : "container",
        cls : "widget-bottom-first-container postion-class",
        height : 135,
        padding : "30 0 0 0",
        layout : {
            type : "vbox",
            align : "center",
            pack : "center"
        },
        items : [ {
            xtype : "label",
            cls : "widget-name-text",
            html : "Donald Brown"
        }, {
            xtype : "label",
            html : "Art Designer"
        }, {
            xtype : "toolbar",
            flex : 1,
            cls : "widget-follower-toolbar",
            width : "100%",
            margin : "20 0 0 0",
            defaults : {
                xtype : "displayfield",
                flex : 1,
                labelAlign : "top"
            },
            items : [ {
                value : '<div class="label">Following</div><div>1,345</div>'
            }, {
                cls : "widget-follower-tool-label",
                value : '<div class="label">Followers</div><div>23,456</div>'
            }, {
                value : '<div class="label">Likes</div><div>52,678</div>'
            } ]
        } ]
    } ]
}, 0, [ "widget-c" ], [ "component", "box", "container", "panel", "widget-c" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    "widget-c" : true
}, [ "widget.widget-c" ], 0, [ Admin.view.widgets, "WidgetC" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetD", Ext.panel.Panel, {
    cls : "admin-widget shadow-panel",
    items : [ {
        xtype : "image",
        cls : "widget-top-container-first-img",
        height : 66,
        width : 66,
        alt : "profile-image",
        src : "resources/images/user-profile/2.png"
    }, {
        xtype : "component",
        cls : "widget-top-first-fourth-container postion-class",
        height : 135
    }, {
        xtype : "container",
        cls : "widget-bottom-first-container postion-class",
        height : 135,
        padding : "30 0 0 0",
        layout : {
            type : "vbox",
            align : "center",
            pack : "center"
        },
        items : [ {
            xtype : "label",
            cls : "widget-name-text",
            html : "Goff Smith"
        }, {
            xtype : "label",
            html : "Project manager"
        }, {
            xtype : "toolbar",
            flex : 1,
            cls : "widget-tool-button",
            items : [ {
                ui : "soft-green",
                text : "Follow"
            }, {
                ui : "soft-blue",
                text : "Message"
            } ]
        } ]
    } ]
}, 0, [ "widget-d" ], [ "component", "box", "container", "panel", "widget-d" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    "widget-d" : true
}, [ "widget.widget-d" ], 0, [ Admin.view.widgets, "WidgetD" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetE", Ext.panel.Panel, {
    cls : "admin-widget-small sale-panel info-card-item shadow-panel",
    containerColor : "",
    height : 170,
    data : {
        amount : 0,
        type : "",
        icon : ""
    },
    tpl : '<div><h2>{amount}</h2><div>{type}</div><span class="x-fa fa-{icon}"></span></div>',
    initComponent : function(){
        var a = this;
        Ext.apply(a, {
            cls : a.config.containerColor
        });
        Ext.panel.Panel.prototype.initComponent.apply(this, arguments)
    }
}, 0, [ "widget-e" ], [ "component", "box", "container", "panel", "widget-e" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    "widget-e" : true
}, [ "widget.widget-e" ], 0, [ Admin.view.widgets, "WidgetE" ], 0);

// -----------
Ext.create(
                "Admin.view.widgets.WidgetF",
                Admin.view.widgets.WidgetE,
                {
                    cls : "admin-widget info-card-item info-card-large-wrap shadow-panel",
                    height : 280,
                    tpl : '<div><span class="x-fa fa-{icon}"></span><h2>{amount}</h2><div class="infodiv">{type}</div></div>'
                }, 0, [ "widget-f" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "widget-e",
                    "widget-f" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    "widget-e" : true,
                    "widget-f" : true
                }, [ "widget.widget-f" ], 0, [ Admin.view.widgets, "WidgetF" ], 0);

// -----------
Ext.create("Admin.view.widgets.Widgets", Ext.container.Container, {
    viewModel : {
        type : "widgets"
    },
    layout : "responsivecolumn",
    defaults : {
        xtype : "container"
    },
    items : [ {
        xtype : "widget-a",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "widget-b",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "widget-c",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "widget-d",
        responsiveCls : "big-50 small-100"
    }, {
        xtype : "widget-e",
        containerColor : "cornflower-blue",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 840,
            type : "Sales",
            icon : "shopping-cart"
        }
    }, {
        xtype : "widget-e",
        containerColor : "green",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 611,
            type : "Messages",
            icon : "envelope"
        }
    }, {
        xtype : "widget-e",
        containerColor : "magenta",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 792,
            type : "Lines of Code",
            icon : "code"
        }
    }, {
        xtype : "widget-e",
        containerColor : "orange",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 637,
            type : "Users",
            icon : "plus-circle"
        }
    }, {
        xtype : "widget-e",
        containerColor : "blue",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 112,
            type : "Servers",
            icon : "tasks"
        }
    }, {
        xtype : "widget-e",
        containerColor : "pink",
        responsiveCls : "big-33 small-50",
        data : {
            amount : 244,
            type : "Files",
            icon : "file-text"
        }
    }, {
        xtype : "widget-f",
        containerColor : "cornflower-blue",
        responsiveCls : "big-50 small-100",
        data : {
            amount : 840,
            type : "Sales",
            icon : "shopping-cart"
        }
    }, {
        xtype : "widget-f",
        containerColor : "green",
        responsiveCls : "big-50 small-100",
        data : {
            amount : 611,
            type : "Messages",
            icon : "envelope"
        }
    }, {
        xtype : "widget-f",
        containerColor : "magenta",
        responsiveCls : "big-50 small-100",
        data : {
            amount : 792,
            type : "Lines of Code",
            icon : "code"
        }
    }, {
        xtype : "widget-f",
        containerColor : "pink",
        responsiveCls : "big-50 small-100",
        data : {
            amount : 244,
            type : "Files",
            icon : "file-text"
        }
    } ]
}, 0, [ "widgets" ], [ "component", "box", "container", "widgets" ], {
    component : true,
    box : true,
    container : true,
    widgets : true
}, [ "widget.widgets" ], 0, [ Admin.view.widgets, "Widgets" ], 0);

// -----------
Ext.create("Admin.view.widgets.WidgetsModel", Ext.app.ViewModel, {
    stores : {
        widgetsFirstRowdataStore : {
            data : [ {
                content : [ {
                    _id : 964,
                    numbers : 840,
                    content : "Sales",
                    fa_image : "x-fa fa-shopping-cart",
                    container_color : "cornflower-blue "
                }, {
                    _id : 837,
                    numbers : 611,
                    content : "Messages",
                    fa_image : "x-fa fa-envelope",
                    container_color : "green"
                }, {
                    _id : 758,
                    numbers : 792,
                    content : "Lines of Code",
                    fa_image : "x-fa fa-code",
                    container_color : "magenta "
                }, {
                    _id : 75,
                    numbers : 244,
                    content : "Files",
                    fa_image : "x-fa fa-file-text",
                    container_color : "pink"
                }, {
                    _id : 482,
                    numbers : 637,
                    content : "Users",
                    fa_image : "x-fa fa-plus-circle",
                    container_color : "orange"
                }, {
                    _id : 948,
                    numbers : 112,
                    content : "Servers",
                    fa_image : "x-fa fa-tasks",
                    container_color : "blue"
                } ]
            } ],
            fields : [ {
                name : "content"
            } ]
        }
    }
}, 0, 0, 0, 0, [ "viewmodel.widgets" ], 0, [ Admin.view.widgets, "WidgetsModel" ], 0);



// -----------
Ext.create("Admin.Application", Ext.app.Application, {
    name : "Admin",
    stores : [ "NavigationTree" ],
    defaultToken : "dashboard",
    onAppUpdate : function(){
        Ext.Msg.confirm("Application Update", "This application has an update, reload?",
                function(a){
                    if (a === "yes") {
                        window.location.reload()
                    }
                })
    }
}, 0, 0, 0, 0, 0, 0, [ Admin, "Application" ], 0);

Ext.application({
    name : "Admin",
    extend : Admin.Application,
    mainView : "Admin.view.main.Viewport"
});
