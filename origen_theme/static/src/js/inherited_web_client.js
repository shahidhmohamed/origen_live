odoo.define("dash_background.InheritedWebClient", function (require) {
    "use strict";
    
    var WebClient = require('web.WebClient');
    
    WebClient.include({
        init: function(parent, client_options) {
            this._super(parent);
            this.set('title_part', {"zopenerp": "Origen"});
            },
        });
    });