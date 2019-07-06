$ = function (query) {
    if(typeof(query)=='function'){
        query.call(window);
        return;
    }
    //class
    var nodeList = document.querySelectorAll(query);

    var el = {
        length: 0
    };
    var array = [];

    if (nodeList.length != 0) {
        el = nodeList[0]
        wrap(el, array);
        for (var key in el) {
            array[key] = el[key];
        }

        for (var i = 0; i < nodeList.length; i++) {
            array.push(wrap(nodeList[i]));
        }
    }

    return array
}

function wrap(el, array) {

    for (var k in methods) {
        (function (label, obj, list) {
            obj[label] = function () {
                if (list) {
                    return methods[label].call(list, arguments.length == 1 ? arguments[0] : arguments);
                } else {
                    return methods[label].call(obj, arguments.length == 1 ? arguments[0] : arguments)
                }
            }
        })(k, el, array);
    }
    el.target = el;
    el.data = {};
    return el
}

function isArguments(value) {
    return Object.prototype.toString.call(value) === '[object Arguments]';
}

function cl(self, callback) {
    if (Array.isArray(self)) {
        self.forEach(node => {
            callback.call(self, node);
        })
    } else {
        callback.call(self, self);
    }
    return this;
}


var methods = {
    each: function (callback) {
        this.forEach((item, index) => callback(item, index));
        return this;
    },
    click: function (p) {
        cl(this, e => {
            e.addEventListener('click', p);
        });

        return this;
    },
    dblclick: function (p) {
        cl(this, e => {
            e.addEventListener('dblclick', p);
        });
    },
    text: function (p) {
        if (p) {
            cl(this, e => {
                e.innerText = p;
            });
        } else {
            return this.innerText;
        }
    },
    html: function (p) {
        if (p) {
            cl(this, e => {
                e.innerHTML = p;
            });
        } else {
            return this.innerHTML;
        }
    },
    css: function (p) {
        if (typeof (p) == 'string') {
            return this.style[p];
        }
        var self = this;
        cl(this, e => {
            if (isArguments(p)) {
                e.style[p[0]] = p[1];
            } else {
                for (var key in p) {
                    e.style[key] = p[key];
                }
            }

        });

        return this;
    },
    show: function () {
        cl(this, e => {
            e.style.display = this.data['display'] || 'block';
        })
    },
    hide: function () {
        cl(this, e => {
            this.data['display'] = this.css('display');
            e.style.display = 'none';
        })
    },
    height() {
        return this.offsetHeight;
    },
    width:function () {
        return this.offsetWidth;
    }
}