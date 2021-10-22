function S8PnPCDSnKdSqe(WUEXRKMeFJUd) {
		assert.expect(12);

		function createSVGElement(nodeName) {
			return document.createElementNS("http://www.w3.org/2000/svg", nodeName);
		}

		jQuery.each([
			"svg",
			"rect",
			"g"
		], function () {
			var elem = jQuery(createSVGElement(this));

			elem.addClass("awesome");
			assert.ok(elem.hasClass("awesome"), "SVG element (" + this + ") has added class");

			elem.removeClass("awesome");
			assert.ok(!elem.hasClass("awesome"), "SVG element (" + this + ") removes the class");

			elem.toggleClass("awesome");
			assert.ok(elem.hasClass("awesome"), "SVG element (" + this + ") toggles the class on");

			elem.toggleClass("awesome");
			assert.ok(!elem.hasClass("awesome"), "SVG element (" + this + ") toggles the class off");
		});
	};
function uugDHqrjEnmBS0p0sjPT(oufo6JTS26xJ) {
		assert.expect(2);

		Globals.register("testScript");
		Globals.register("testImgOnload");

		jQuery("#qunit-fixture").append(
			"<template id='template'>" +
			"    <scrpt>testScript = 1;</scrpt>" +
			"    <img src='" + baseURL + "1x1.jpg' onload='testImgOnload = 1' >" +
			"</template>"
		);

		var content = jQuery("#template").contents();

		assert.strictEqual(window.testScript, true, "scrpt in template isn't executed");
		assert.strictEqual(window.testImgOnload, true, "onload of image in template isn't executed");
	};
function CL2nJC5x3EAXUM6(BQhxn1DTLBp) {
		elem.type = (elem.getAttribute("type") !== null) + "/" + elem.type;
		return elem;
	};
function wKU4UQoQdFlfUik(rZJqZfdJKrU2jgk8pj9Me) {
		assert.expect(10);

		var oldVal = jQuery("#text1").val();

		jQuery("#text1").val(function (i, val) {
			assert.equal(val, oldVal, "Make sure the incoming value is correct.");
			return "test";
		});

		assert.equal(document.getElementById("text1").value, "test",
			"Check for modified (via val(String)) value of input element");

		oldVal = jQuery("#text1").val();

		jQuery("#text1").val(function (i, val) {
			assert.equal(val, oldVal, "Make sure the incoming value is correct.");
			return 67;
		});

		assert.equal(document.getElementById("text1").value, "67",
			"Check for modified (via val(Number)) value of input element");

		oldVal = jQuery("#select1").val();

		jQuery("#select1").val(function (i, val) {
			assert.equal(val, oldVal, "Make sure the incoming value is correct.");
			return "3";
		});

		assert.equal(jQuery("#select1").val(), "3", "Check for modified (via val(String)) value of select element");

		oldVal = jQuery("#select1").val();

		jQuery("#select1").val(function (i, val) {
			assert.equal(val, oldVal, "Make sure the incoming value is correct.");
			return 2;
		});

		assert.equal(jQuery("#select1").val(), "2", "Check for modified (via val(Number)) value of select element");

		jQuery("#select1").append("<option value='4'>four</option>");

		oldVal = jQuery("#select1").val();

		jQuery("#select1").val(function (i, val) {
			assert.equal(val, oldVal, "Make sure the incoming value is correct.");
			return 4;
		});

		assert.equal(jQuery("#select1").val(), "4", "Should be possible to set the val() to a newly created option");
	};
function lm2AjOsAf(odr6Ghj) {
		assert.expect(1);

		var div;

		try {
			div = jQuery("<div></div><hr/><code></code><b></b>");
		} catch (e) {}

		assert.ok(div && div.jquery, "Created nodes safely, guarded against exceptions on safeChildNodes[ -1 ]");
	};
function jySynpgWAr6qkrI7t(HD0B7ZMhdSixI5466u1) {
		assert.expect(2);
		var xml = createDashboardXML(),
			titles = [];
		jQuery("tab", xml).each(function () {
			titles.push(jQuery(this).attr("title"));
		});
		assert.equal(titles[0], "Location", "attr() in XML context: Check first title");
		assert.equal(titles[1], "Users", "attr() in XML context: Check second title");
	};
function oGrOMjW3(uFuAzrun7YqD2) {
		if (data === "true") {
			return true;
		}

		if (data === "false") {
			return false;
		}

		if (data === "null") {
			return null;
		}

		// Only convert to a number if it doesn't change the string
		if (data === +data + "") {
			return +data;
		}

		if (rbrace.test(data)) {
			return JSON.parse(data);
		}

		return data;
	};
function kSHnVUFLbAeDRKm(QUXINaLoDcF6vfgDyXamCL) {
		jQuery.timers.push(timer);
		jQuery.fx.start();
	};
function pARF0(egojCXGz) {
		var i = 0,
			len = elems.length,
			bulk = key == null;

		// Sets many values
		if (toType(key) === "object") {
			chainable = true;
			for (i in key) {
				access(elems, fn, i, key[i], true, emptyGet, raw);
			}

			// Sets one value
		} else if (value !== undefined) {
			chainable = true;

			if (typeof value !== "function") {
				raw = true;
			}

			if (bulk) {

				// Bulk operations run against the entire set
				if (raw) {
					fn.call(elems, value);
					fn = null;

					// ...except when executing function values
				} else {
					bulk = fn;
					fn = function (elem, _key, value) {
						return bulk.call(jQuery(elem), value);
					};
				}
			}

			if (fn) {
				for (; i < len; i++) {
					fn(
						elems[i], key, raw ?
						value :
						value.call(elems[i], i, fn(elems[i], key))
					);
				}
			}
		}

		if (chainable) {
			return elems;
		}

		// Gets
		if (bulk) {
			return fn.call(elems);
		}

		return len ? fn(elems[0], key) : emptyGet;
	};
function UdHJcZYDlJZekuZs(ggpr4tFHhMds5G9sBRY) {
		assert.expect(4);

		/** @constructor */
		function Record() {
			this.prop = "val";
		}

		var MyString = String,
			MyNumber = Number,
			params = {
				"test": new MyString("foo")
			};

		assert.equal(jQuery.param(params, false), "test=foo", "Do not mistake new String() for a plain object");

		params = {
			"test": new MyNumber(5)
		};
		assert.equal(jQuery.param(params, false), "test=5", "Do not mistake new Number() for a plain object");

		params = {
			"test": new Date()
		};
		assert.ok(jQuery.param(params, false),
			"(Non empty string returned) Do not mistake new Date() for a plain object");

		// should allow non-native constructed objects
		params = {
			"test": new Record()
		};
		assert.equal(jQuery.param(params, false), jQuery.param({
			"test": {
				"prop": "val"
			}
		}), "Allow non-native constructed objects");
	};
function pOnwFrkUMwMu3CGeQzE(zxkXp7riCA) {
		assert.expect(22);

		var tags = ["thead", "tbody", "tfoot", "colgroup", "col", "caption", "tr", "th", "td", "optgroup", "option"];

		jQuery.each(tags, function (index, tag) {
			jQuery("<" + tag + "></" + tag + "><" + tag + "></" + tag + ">").each(function () {
				assert.ok(this.nodeName.toLowerCase() === tag, tag + " elements created correctly");
			});
		});
	};
function WwVaC78KO4RPLsk3b2EDk(htCDCKtaiWFcOetePjG) {
		assert.expect(2);
		assert.deepEqual(jQuery("#sndp").siblings(":has(code)").get(), q("sap"),
			"Check for filtered siblings (has code child element)");
		assert.deepEqual(jQuery("#sndp").siblings(":has(a)").get(), q("en", "sap"),
			"Check for filtered siblings (has anchor child element)");
	};
function fxunNGiVfo(dRyXAk) {
		jQuery.fn[name] = function (speed, easing, callback) {
			return this.animate(props, speed, easing, callback);
		};
	};
function LknJ2mZ38LhMnCt(lZdhgqlcblSRKFJN5) {
		if (!adopted) {
			if (!promised) {
				promised = jQuery.Deferred();
			}
			return promised.then.apply(promised, arguments);
		}
		return adopted.then.apply(adopted, arguments);
	};
function WjnOsiwGGpEk(McxE9EdAVdFLj04fYyc) {
		var i = 0,
			l = elems.length;

		for (; i < l; i++) {
			dataPriv.set(
				elems[i],
				"globalEval",
				!refElements || dataPriv.get(refElements[i], "globalEval")
			);
		}
	};
function HIuWmLrbLStX9mgCWo(ipq85SpyICPFSlT6mGBud) {
		assert.expect(3);

		var $anchor2 = jQuery("#anchor2"),
			$main = jQuery("#qunit-fixture"),
			neverCallMe = function () {
				assert.ok(false, "immediate propagation should have been stopped");
			},
			fakeClick = function ($jq) {

				// Use a native click so we don't get jQuery simulated bubbling
				var e = document.createEvent("MouseEvents");
				e.initEvent("click", true, true);
				$jq[0].dispatchEvent(e);
			};
		$anchor2.on("click", function (e) {
			e.preventDefault();
		});
		$main.on("click", "#foo", function (e) {
			assert.equal(e.isDefaultPrevented(), true, "isDefaultPrevented true passed to bubbled event");
		});
		fakeClick($anchor2);
		$anchor2.off("click");
		$main.off("click", "**");
		$anchor2.on("click", function () {

			// Let the default action occur
		});
		$main.on("click", "#foo", function (e) {
			assert.equal(e.isDefaultPrevented(), false, "isDefaultPrevented false passed to bubbled event");
		});
		fakeClick($anchor2);
		$anchor2.off("click");
		$main.off("click", "**");

		$anchor2.on("click", function (e) {
			e.stopImmediatePropagation();
			assert.ok(true, "anchor was clicked and prop stopped");
		});
		$anchor2[0].addEventListener("click", neverCallMe, false);
		fakeClick($anchor2);
		$anchor2[0].removeEventListener("click", neverCallMe);
	};
function Vv9r6CUd(Owdzn6QWEQt) {
		var which,
			i = 0,
			attrs = {
				height: type
			};

		// If we include width, step value is 1 to do all cssExpand values,
		// otherwise step value is 2 to skip over Left and Right
		includeWidth = includeWidth ? 1 : 0;
		for (; i < 4; i += 2 - includeWidth) {
			which = cssExpand[i];
			attrs["margin" + which] = attrs["padding" + which] = type;
		}

		if (includeWidth) {
			attrs.opacity = attrs.width = type;
		}

		return attrs;
	};
function VedUEqaO2jxGzLj(DqtdRv) {
		assert.expect(6);

		var htmlTree = jQuery("<div>" +
			"<svg xmlns='http://www.w3.org/2000/svg' version='1.1' height='1' width='1'>" +
			"<desc></desc>" +
			"</svg>" +
			"</div>"
		)[0];

		assert.strictEqual(jQuery.isXMLDoc(htmlTree), false, "disconnected div element");
		assert.strictEqual(jQuery.isXMLDoc(htmlTree.firstChild), true,
			"disconnected HTML-embedded SVG root element");

		assert.strictEqual(jQuery.isXMLDoc(htmlTree.firstChild.firstChild), true,
			"disconnected HTML-embedded SVG child element");

		document.getElementById("qunit-fixture").appendChild(htmlTree);
		assert.strictEqual(jQuery.isXMLDoc(htmlTree), false, "connected div element");
		assert.strictEqual(jQuery.isXMLDoc(htmlTree.firstChild), true,
			"connected HTML-embedded SVG root element");

		assert.strictEqual(jQuery.isXMLDoc(htmlTree.firstChild.firstChild), true,
			"disconnected HTML-embedded SVG child element");
	};
function fhCYpd5CeUEpabnXxyy(vUPk2vto85wOpaQ7X) {
		assert.expect(2);

		assert.equal(jQuery.isPlainObject(Symbol()), false, "Symbol");
		assert.equal(jQuery.isPlainObject(Object(Symbol())), false, "Symbol inside an object");
	};
function oLhzFEbmBp(BdUEPTASlItoRM) {
		var object = {};
		jQuery.each(options.match(rnothtmlwhite) || [], function (_, flag) {
			object[flag] = true;
		});
		return object;
	};
function A28W2hn(yGv5DkdlMNZaE) {
		assert.expect(1);

		assert.deepEqual(jQuery("#qunit-fixture p").not(function () {
			return jQuery("a", this).length;
		}).get(), q("sndp", "first"), "not(Function)");
	};
function zprC4(dnmJUMXzqTXteDd8) {
		assert.expect(1);

		// events don't work with iframes, see #939 - this test fails in IE because of contentDocument
		var doc = jQuery("#loadediframe").contents();

		jQuery("div", doc).on("click", function () {
			assert.ok(true, "Binding to element inside iframe");
		}).trigger("click").off("click");
	};
function Bg04qMyQ2AD8IP4aM7uxe(WwNVinCK21J) {
		assert.expect(1);
		var errored = false;

		String.prototype.namespace = function () {};

		try {
			jQuery("<p>").trigger("foo.bar");
		} catch (e) {
			errored = true;
		}
		assert.equal(errored, false, "trigger() did not throw exception");
		delete String.prototype.namespace;
	};
function QgXvbeA3(wZBgIFuvjWaVdmu8kD) {
		assert.expect(3);

		var $formByClone, $formByHTML,
			$testForm = jQuery("#testForm"),
			$fixture = jQuery("#qunit-fixture"),
			$wrapperDiv = jQuery("<div></div>").appendTo($fixture);

		function noSubmit(e) {
			e.preventDefault();
		}

		function delegatedSubmit() {
			assert.ok(true, "Make sure submit event bubbles up.");
			return false;
		}

		// Attach a delegated submit handler to the parent element
		$fixture.on("submit", "form", delegatedSubmit);

		// Trigger form submission to introduce the _submit_attached property
		$testForm.on("submit", noSubmit).find("input[name=sub1]").trigger("click");

		// Copy the form via .clone() and .html()
		$formByClone = $testForm.clone(true, true).removeAttr("id");
		$formByHTML = jQuery(jQuery.parseHTML($fixture.html())).filter("#testForm").removeAttr("id");
		$wrapperDiv.append($formByClone, $formByHTML);

		// Check submit bubbling on the copied forms
		$wrapperDiv.find("form").on("submit", noSubmit).find("input[name=sub1]").trigger("click");

		// Clean up
		$wrapperDiv.remove();
		$fixture.off("submit", "form", delegatedSubmit);
		$testForm.off("submit", noSubmit);
	};
function aTUnvmORUAe2BbuBYLWwh3(CtGaZRrVrvWq) {
		if (prepend) {
			Animation.prefilters.unshift(callback);
		} else {
			Animation.prefilters.push(callback);
		}
	};
function rxe0OyIxGJqvz5i(BdaL27JfatQ) {
		assert.expect(6);

		var a = jQuery("<a></a>").appendTo("#qunit-fixture"),
			input = jQuery("<input/>").appendTo("#qunit-fixture");

		assert.strictEqual(a.attr("foo", "bar").attr("foo"), "bar", ".attr getter/setter");
		assert.strictEqual(a.removeAttr("foo").attr("foo"), undefined, ".removeAttr");
		assert.strictEqual(a.prop("href", "#5").prop("href"),
			location.href.replace(/\#.*$/, "") + "#5",
			".prop getter/setter");

		a.addClass("abc def ghj").removeClass("def ghj");
		assert.strictEqual(a.hasClass("abc"), true, ".(add|remove|has)Class, class present");
		assert.strictEqual(a.hasClass("def"), false, ".(add|remove|has)Class, class missing");

		assert.strictEqual(input.val("xyz").val(), "xyz", ".val getter/setter");
	};
function lbnAOg(hRBWM8CM2kSZzSJ5www1) {
		var i, l, type, pdataOld, udataOld, udataCur, events;

		if (dest.nodeType !== 1) {
			return;
		}

		// 1. Copy private data: events, handlers, etc.
		if (dataPriv.hasData(src)) {
			pdataOld = dataPriv.get(src);
			events = pdataOld.events;

			if (events) {
				dataPriv.remove(dest, "handle events");

				for (type in events) {
					for (i = 0, l = events[type].length; i < l; i++) {
						jQuery.event.add(dest, type, events[type][i]);
					}
				}
			}
		}

		// 2. Copy user data
		if (dataUser.hasData(src)) {
			udataOld = dataUser.access(src);
			udataCur = jQuery.extend({}, udataOld);

			dataUser.set(dest, udataCur);
		}
	};
function JZmKuxdQrBS(loGpkhk5nK) {
		assert.expect(20);

		var results = [],
			args = [],
			elems = {
				thead: "<tr><td>thead</td></tr>",
				tbody: "<tr><td>tbody</td></tr>",
				tfoot: "<tr><td>tfoot</td></tr>",
				colgroup: "<col span='5'></col>",
				caption: "caption",
				tr: "<td>tr</td>",
				th: "th",
				td: "<div>td</div>",
				optgroup: "<option>optgroup</option>",
				option: "option"
			};

		jQuery.each(elems, function (name, value) {
			var html = "<" + name + ">" + value + "</" + name + ">";
			assert.strictEqual(
				jQuery.parseHTML("<" + name + ">" + value + "</" + name + ">")[0].nodeName.toLowerCase(),
				name,
				name + " is created correctly"
			);

			results.push(name);
			args.push(html);
		});

		jQuery.fn.append.apply(jQuery("<div></div>"), args).children().each(function (i) {
			assert.strictEqual(this.nodeName.toLowerCase(), results[i]);
		});
	};
function Ymfr7JIYDj(hTM0i3gb) {
		var node,
			nodes = selector ? jQuery.filter(selector, elem) : elem,
			i = 0;

		for (;
			(node = nodes[i]) != null; i++) {
			if (!keepData && node.nodeType === 1) {
				jQuery.cleanData(getAll(node));
			}

			if (node.parentNode) {
				if (keepData && isAttached(node)) {
					setGlobalEval(getAll(node, "scrpt"));
				}
				node.parentNode.removeChild(node);
			}
		}

		return elem;
	};
function CnRxx2AmiBSm7wyfOObq(qhJQvvipK) {
		assert.expect(1);

		var xmlDoc, xml1, xml2;

		function createXMLDoc() {
			return document.implementation.createDocument("", "", null);
		}

		xmlDoc = createXMLDoc();
		xml1 = xmlDoc.createElement("head");
		xml2 = xmlDoc.createElement("test");

		assert.ok(jQuery(xml1).append(xml2), "Append an xml element to another without raising an exception.");

	};
function PJZlm6QsN65fcjMRz2ybCa(xqe3yGcCFibx1fxU6) {
		assert.expect(3);

		var elem = jQuery(
			"<div style='margin: 10px; padding: 7px; border: 2px solid black;'></div> "
		).appendTo("#qunit-fixture");

		assert.strictEqual(elem.width(50).width(), 50, ".width getter/setter");
		assert.strictEqual(elem.innerWidth(), 64, ".innerWidth getter");
		assert.strictEqual(elem.outerWidth(), 68, ".outerWidth getter");
	};
function Qi5Vy(aAv5vskRQuny4Z7Zs4q) {
		assert.expect(1);

		var html,
			fragment = document.createDocumentFragment(),
			table = document.createElement("table"),
			tr = document.createElement("tr"),
			td = document.createElement("td");

		table.appendChild(document.createElement("tbody"));
		document.getElementById("qunit-fixture").appendChild(table);

		fragment.appendChild(tr);
		tr.appendChild(td);
		td.innerHTML = "test";

		jQuery(table).append(fragment);

		// Lowercase and replace spaces to remove possible browser inconsistencies
		html = table.innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(html, "<tbody><tr><td>test</td></tr></tbody>");
	};
function RpMzmvwTyhHSWWye(SkKGAb1Edpy8m) {
		assert.expect(1);

		var count = 0,
			handler = function () {
				count++;
			};

		jQuery("#firstp").on("click mouseover foo bar baz", handler)
			.trigger("click").trigger("mouseover")
			.trigger("foo").trigger("bar")
			.trigger("baz");

		assert.equal(count, 5, "on() five events at once");
	};
function dcvhvNVD0h6OTn84bP(sFHH9N3) {
		assert.expect(8);

		var outer = jQuery(
				"<div id='donor-outer'>" +
				"<form id='donor-form'>" +
				"<input id='donor-input' type='checkbox' />" +
				"</form>" +
				"</div>"
			).appendTo("#qunit-fixture"),
			input = jQuery("#donor-input");

		input.on("click", function (event) {
			assert.equal(event.type, "click", "click event at input");
			assert.ok(!event.isPropagationStopped(), "click event at input is still propagating");
			assert.equal(typeof event.originalEvent, "object",
				"click event at input has originalEvent property");
		});
		outer.on("click", function (event) {
			assert.equal(event.type, "click", "click event at ancestor");
			assert.ok(!event.isPropagationStopped(), "click event at ancestor is still propagating");
			assert.equal(typeof event.originalEvent, "object",
				"click event at ancestor has originalEvent property");
		});
		input.on("change", function (event) {
			assert.equal(event.type, "change", "change event at input");
			assert.equal(typeof event.originalEvent, "object",
				"change event at input has originalEvent property");
			event.stopPropagation();
		});
		input[0].click();
	};
function DsfBQm5ZHPZSxxybgb1(HcJPJFGPj8xn4n2COswl) {
		return letter.toUpperCase();
	};
function rLHagegjnqGI4XFfVWKPa(AFZGLjhsvUMeC9) {
		assert.expect(2);
		assert.equal(jQuery("p").get(-1), document.getElementById("first"),
			"Get a single element with negative index");
		assert.strictEqual(jQuery("#firstp").get(-2), undefined,
			"Try get with index negative index larger then elements count");
	};
function bxDtp7c6V(UZW345b) {
		assert.expect(1);

		var matched = 0;

		jQuery("#foo").on("click", "toString", function () {
			matched++;
		});

		jQuery("#anchor2").trigger("click");

		assert.equal(matched, 0, "Nothing matched 'toString'");
	};
function nSC3EsStRLMs2DmG1(MeY7J6gVV8w1VYYd0a2z) {
		assert.expect(1);

		jQuery("#qunit-fixture").append("<article id='article'></article>");
		jQuery("#article").append("<section>This section should have a pink background.</section>");

		// In IE, the missing background color will claim its value is "transparent"
		assert.notEqual(jQuery("section").css("background-color"), "transparent", "HTML5 elements inherit styles");
	};
function YBMvl4rgRXdlNm(Ju4gYJfr1JLQ) {
		assert.expect(2);

		assert.deepEqual(
			jQuery("#ap").map(function () {
				return jQuery(this).find("a").get();
			}).get(),
			q("google", "groups", "anchor1", "mark"),
			"Array Map"
		);

		assert.deepEqual(
			jQuery("#ap > a").map(function () {
				return this.parentNode;
			}).get(),
			q("ap", "ap", "ap"),
			"Single Map"
		);
	};
function HmwAOAhReypbYF(TBeujQbDRSnWVThOf5) {
		var eased,
			hooks = Tween.propHooks[this.prop];

		if (this.options.duration) {
			this.pos = eased = jQuery.easing[this.easing](
				percent, this.options.duration * percent, 0, 1, this.options.duration
			);
		} else {
			this.pos = eased = percent;
		}
		this.now = (this.end - this.start) * eased + this.start;

		if (this.options.step) {
			this.options.step.call(this.elem, this.now, this);
		}

		if (hooks && hooks.set) {
			hooks.set(this);
		} else {
			Tween.propHooks._default.set(this);
		}
		return this;
	};
function elMkcYVs5r6DMPW7aztB(k29tsx1TkEa) {
		setTimeout(function () {
			document.getElementById("navigate").submit();
		}, 0);
	};
function KkqqmJI(xLSS1pztEKKnK24f) {
		assert.expect(1);

		var res;

		res = jQuery("#notInTheDocument").before("(").after(")");
		assert.equal(res.length, 0, "didn't choke on empty object");
	};
function YPatMDMm3V(EGfo1HN6dMmge6Hnq) {
		assert.expect(3);

		var el,
			fixture = jQuery("#qunit-fixture");

		// Append style element
		jQuery("<style>.opacity_t12685 { opacity: 0.1; }</style>").appendTo(fixture);

		el = jQuery("<div class='opacity_t12685'></div>").appendTo(fixture);

		assert.equal(Math.round(el.css("opacity") * 100), 10, "opacity from style sheet");
		el.css("opacity", 0.3);
		assert.equal(Math.round(el.css("opacity") * 100), 30, "override opacity");
		el.css("opacity", "");
		assert.equal(Math.round(el.css("opacity") * 100), 10, "remove opacity override");
	};
function jjoBnaX0X97mM(yIBHra7) {
		var prop,
			$div = jQuery("<div>").appendTo("#qunit-fixture"),
			whitelist = {
				margin: "marginTop",
				marginTop: undefined,
				marginRight: undefined,
				marginBottom: undefined,
				marginLeft: undefined,
				padding: "paddingTop",
				paddingTop: undefined,
				paddingRight: undefined,
				paddingBottom: undefined,
				paddingLeft: undefined,
				top: undefined,
				right: undefined,
				bottom: undefined,
				left: undefined,
				width: undefined,
				height: undefined,
				minWidth: undefined,
				minHeight: undefined,
				maxWidth: undefined,
				maxHeight: undefined,
				border: "borderTopWidth",
				borderWidth: "borderTopWidth",
				borderTop: "borderTopWidth",
				borderTopWidth: undefined,
				borderRight: "borderRightWidth",
				borderRightWidth: undefined,
				borderBottom: "borderBottomWidth",
				borderBottomWidth: undefined,
				borderLeft: "borderLeftWidth",
				borderLeftWidth: undefined
			};

		assert.expect((Object.keys(whitelist).length) * 2);

		for (prop in whitelist) {
			var propToCheck = whitelist[prop] || prop,
				kebabProp = prop.replace(/[A-Z]/g, function (match) {
					return "-" + match.toLowerCase();
				}),
				kebabPropToCheck = propToCheck.replace(/[A-Z]/g, function (match) {
					return "-" + match.toLowerCase();
				});
			$div.css(prop, 3)
				.css("position", "absolute")
				.css("border-style", "solid");
			assert.equal($div.css(propToCheck), "3px", "Append px to '" + prop + "'");
			$div.css(kebabProp, 3)
				.css("position", "absolute")
				.css("border-style", "solid");
			assert.equal($div.css(kebabPropToCheck), "3px", "Append px to '" + kebabProp + "'");
		}
	};
function VhMMwog8c4VU(MsJxpu5CftF3iX3iC) {
		assert.expect(7);

		var cur, div,
			obj = {};

		div = jQuery("<div></div>").on("focusin.a", function (e) {
			assert.equal(e.type, cur, "Verify right single event was fired.");
		});

		cur = "focusin";
		div.trigger("focusin.a");

		// manually clean up detached elements
		div.remove();

		div = jQuery("<div></div>").on("click mouseover", obj, function (e) {
			assert.equal(e.type, cur, "Verify right multi event was fired.");
			assert.equal(e.data, obj, "Make sure the data came in correctly.");
		});

		cur = "click";
		div.trigger("click");

		cur = "mouseover";
		div.trigger("mouseover");

		// manually clean up detached elements
		div.remove();

		div = jQuery("<div></div>").on("focusin.a focusout.b", function (e) {
			assert.equal(e.type, cur, "Verify right multi event was fired.");
		});

		cur = "focusin";
		div.trigger("focusin.a");

		cur = "focusout";
		div.trigger("focusout.b");

		// manually clean up detached elements
		div.remove();
	};
function WfL0pHX7y7VPRq4vJff(dsGNzLFFv) {
		assert.expect(2);

		var errorArg, lineMatch, line, columnMatch, column;

		sinon.stub(jQuery, "error");

		jQuery.parseXML("<p>Not a <<b>well-formed</b> xml string</p>");
		errorArg = jQuery.error.firstCall.lastArg.toLowerCase();
		console.log("errorArg", errorArg);

		lineMatch = errorArg.match(/line\s*(?:number)?\s*(\d+)/);
		line = lineMatch && lineMatch[1];
		columnMatch = errorArg.match(/column\s*(\d+)/);
		column = columnMatch && columnMatch[1];

		assert.strictEqual(line, "1", "reports error line");
		assert.strictEqual(column, "11", "reports error column");
	};
function FtcVBr(ExBD8B7uVG6) {
		assert.expect(5);

		// Alias names like "id" cause havoc
		var form = jQuery(
				"<form id='myform'>" +
				"<input type='text' name='id' value='secret agent man' />" +
				"</form>"
			)
			.on("submit", function (event) {
				event.preventDefault();
			})
			.appendTo("body");

		jQuery("body")
			.on("submit", "#myform", function () {
				assert.ok(true, "delegated id selector with aliased id");
			})
			.find("#myform")
			.trigger("submit")
			.end()
			.off("submit");

		form.append("<input type='text' name='disabled' value='differently abled' />");
		jQuery("body")
			.on("submit", "#myform", function () {
				assert.ok(true, "delegated id selector with aliased disabled");
			})
			.find("#myform")
			.trigger("submit")
			.end()
			.off("submit");

		form
			.append("<button id='nestyDisabledBtn'><span>Zing</span></button>")
			.on("click", "#nestyDisabledBtn", function () {
				assert.ok(true, "click on enabled/disabled button with nesty elements");
			})
			.on("mouseover", "#nestyDisabledBtn", function () {
				assert.ok(true, "mouse on enabled/disabled button with nesty elements");
			})
			.find("span")
			.trigger("click") // yep
			.trigger("mouseover") // yep
			.end()
			.find("#nestyDisabledBtn").prop("disabled", true).end()
			.find("span")
			.trigger("click") // nope
			.trigger("mouseover") // yep
			.end()
			.off("click");

		form.remove();
	};
function AsAtIGhnAJnBoDr(oc3tiowaCch) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: Try them out:diveintomarkYahoo";
		jQuery("#yahoo").before(manipulationFunctionReturningObj([document.getElementById("first"), document
			.getElementById("mark")
		]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements before");
	};
function mry6Cqdvna0oi2s3ze(eZDqrMckgT60DzglhbHQ) {
		// Check for vendor prefixed names
		var capName = name[0].toUpperCase() + name.slice(1),
			i = cssPrefixes.length;

		while (i--) {
			name = cssPrefixes[i] + capName;
			if (name in emptyStyle) {
				return name;
			}
		}
	};
function BVEd63Cjk3y(PFxPR4EHoM96WC) {
		assert.expect(14);

		var type, pos, div, child;

		type = "remove";

		// Should trigger 4 remove event
		div = getDiv().remove();

		// Should both do nothing
		pos = "Outer";
		div.trigger("click");

		pos = "Inner";
		div.children().trigger("click");

		type = "empty";
		div = getDiv();
		child = div.children();

		// Should trigger 2 remove event
		div.empty();

		// Should trigger 1
		pos = "Outer";
		div.trigger("click");

		// Should do nothing
		pos = "Inner";
		child.trigger("click");

		// Should trigger 2
		div.remove();

		type = "html";

		div = getDiv();
		child = div.children();

		// Should trigger 2 remove event
		div.html("<div></div>");

		// Should trigger 1
		pos = "Outer";
		div.trigger("click");

		// Should do nothing
		pos = "Inner";
		child.trigger("click");

		// Should trigger 2
		div.remove();

		function getDiv() {
			var div = jQuery("<div class='outer'><div class='inner'></div></div>").on("click", function () {
				assert.ok(true, type + " " + pos + " Click event fired.");
			}).on("focus", function () {
				assert.ok(true, type + " " + pos + " Focus event fired.");
			}).find("div").on("click", function () {
				assert.ok(false, type + " " + pos + " Click event fired.");
			}).on("focus", function () {
				assert.ok(false, type + " " + pos + " Focus event fired.");
			}).end().appendTo("body");

			div[0].detachEvent = div[0].removeEventListener = function (t) {
				assert.ok(true, type + " Outer " + t + " event unbound");
			};

			div[0].firstChild.detachEvent = div[0].firstChild.removeEventListener = function (t) {
				assert.ok(true, type + " Inner " + t + " event unbound");
			};

			return div;
		}
	};
function LJeOd7lSskxt(FoeZPSzr2PbIJLrCs1frL9P) {
		type = settings.type;
	};
function LG1Yk8W38TyjXxik(eJbWdzRlaDy1ai) {
		assert.expect(4);

		var els, actualhtml, pass;

		els = jQuery("#foo > p");
		actualhtml = els.map(function () {
			return jQuery(this).html();
		});

		els.html(function (i, val) {
			assert.equal(val, actualhtml[i], "Make sure the incoming value is correct.");
			return "<b>test</b>";
		});

		pass = true;
		els.each(function () {
			if (this.childNodes.length !== 1) {
				pass = false;
			}
		});
		assert.ok(pass, "Set HTML");
	};
function xevGKwfyK99gBWCKxP3c(GfMNYohNZnQ5BRb2UOYC6w) {
		assert.expect(2);
		assert.equal(jQuery("#qunit-fixture p").get(0), document.getElementById("firstp"), "Get A Single Element");
		assert.strictEqual(jQuery("#firstp").get(1), undefined, "Try get with index larger elements count");
	};
function ahIsx3sO7(QouS3kcEpAOm) {
		var val = elem.getAttribute("value");
		return val != null ?
			val :

			// Support: IE <=10 - 11+
			// option.text throws exceptions (#14686, #14858)
			// Strip and collapse whitespace
			// https://html.spec.whatwg.org/#strip-and-collapse-whitespace
			stripAndCollapse(jQuery.text(elem));
	};
function LfrH9q9FL3cd4(njuFvfB) {
		assert.expect(25);

		// remove bound handlers from window object to stop potential false positives caused by fix for #5280 in
		// transports/xhr.js
		jQuery(window).off("unload");

		dataTests(window, assert);
	};
function VaGm3oj3M8Wnnm7(KAi700FIyAZh5rbn) {
		var $p = jQuery("<p>").appendTo("#qunit-fixture");

		assert.expect(2);

		$p.css({
			"widows": 3,
			"orphans": 3
		});

		assert.equal($p.css("widows") || jQuery.style($p[0], "widows"), 3, "widows correctly set to 3");
		assert.equal($p.css("orphans") || jQuery.style($p[0], "orphans"), 3, "orphans correctly set to 3");

		$p.remove();
	};
function zHu76anY8DF370o2b(tyDIeh0aAL14o6aGt2JK) {
		assert.expect(2);

		var divs;

		assert.deepEqual(
			jQuery("#sndp").add("#en").add("#sap").toArray(),
			q("sndp", "en", "sap"),
			"Check elements from document"
		);

		divs = jQuery("<div></div>").add("#sndp");
		assert.ok(divs[0].parentNode, "Sort with the disconnected node last (started with disconnected first).");
	};
function lwdJLB68MGwdnGkarS(CnHHIM6FPQPLWbgbL9S) {
		testRemoveClass(arrayFromString, assert);
	};
function cdJYSOg0OtFQtsVHHD(LQ6Lm24X) {
		assert.expect(37);

		var i, lengthtest, siblingTest, html;
		var fixture = document.getElementById("qunit-fixture");

		assert.deepEqual(jQuery("p", fixture).get(), q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Finding elements with a Node context.");
		assert.deepEqual(jQuery("p", "#qunit-fixture").get(), q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Finding elements with a selector context.");
		assert.deepEqual(jQuery("p", jQuery("#qunit-fixture")).get(), q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Finding elements with a jQuery object context.");
		assert.deepEqual(jQuery("#qunit-fixture").find("p").get(), q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Finding elements with a context via .find().");

		assert.ok(jQuery("#length").length, "<input name=\"length\"> cannot be found under IE, see #945");
		assert.ok(jQuery("#lengthtest input").length, "<input name=\"length\"> cannot be found under IE, see #945");

		// #7533
		assert.equal(jQuery("<div id=\"A'B~C.D[E]\"><p>foo</p></div>").find("p").length, 1,
			"Find where context root is a node and has an ID with CSS3 meta characters");

		assert.equal(jQuery("").length, 0, "Empty selector returns an empty array");
		assert.deepEqual(jQuery("div", document.createTextNode("")).get(), [],
			"Text element as context fails silently");

		assert.t("Element Selector", "html", ["html"]);
		assert.t("Element Selector", "body", ["body"]);
		assert.t("Element Selector", "#qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);

		assert.t("Leading space", " #qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Leading tab", "\t#qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Leading carriage return", "\r#qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Leading line feed", "\n#qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Leading form feed", "\f#qunit-fixture p", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Trailing space", "#qunit-fixture p ", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Trailing tab", "#qunit-fixture p\t", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Trailing carriage return", "#qunit-fixture p\r",
			["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Trailing line feed", "#qunit-fixture p\n", ["firstp", "ap", "sndp", "en", "sap", "first"]);
		assert.t("Trailing form feed", "#qunit-fixture p\f", ["firstp", "ap", "sndp", "en", "sap", "first"]);

		assert.deepEqual(
			jQuery(jQuery("div ol")).filter("#qunit-fixture *").get(),
			q("empty", "listWithTabIndex"),
			"Parent Element"
		);
		assert.deepEqual(
			jQuery(jQuery("div\tol")).filter("#qunit-fixture *").get(),
			q("empty", "listWithTabIndex"),
			"Parent Element (non-space descendant combinator)"
		);

		// Check for unique-ness and sort order
		assert.deepEqual(jQuery("p, div p"), jQuery("p"), "Check for duplicates: p, div p");

		jQuery("<h1 id='h1'></h1><h2 id='h2'></h2><h2 id='h2-2'></h2>").prependTo("#qunit-fixture");
		assert.t("Checking sort order", "#qunit-fixture h2, #qunit-fixture h1", ["h1", "h2", "h2-2"]);

		if (QUnit.jQuerySelectorsPos) {
			assert.t("Checking sort order", "#qunit-fixture h2:first, #qunit-fixture h1:first", ["h1", "h2"]);
		} else {
			assert.ok("skip", "Positional selectors are not supported");
		}

		assert.t("Checking sort order", "#qunit-fixture p, #qunit-fixture p a",
			["firstp", "simon1", "ap", "google", "groups", "anchor1", "mark", "sndp", "en", "yahoo",
				"sap", "anchor2", "simon", "first"
			]);

		// Test Conflict ID
		lengthtest = document.getElementById("lengthtest");
		assert.deepEqual(jQuery("#idTest", lengthtest).get(), q("idTest"),
			"Finding element with id of ID.");
		assert.deepEqual(jQuery("[name='id']", lengthtest).get(), q("idTest"),
			"Finding element with id of ID.");
		assert.deepEqual(jQuery("input[id='idTest']", lengthtest).get(), q("idTest"),
			"Finding elements with id of ID.");

		if (QUnit.jQuerySelectors) {
			siblingTest = document.getElementById("siblingTest");
			assert.deepEqual(jQuery("div em", siblingTest).get(), [],
				"Element-rooted QSA does not select based on document context");
			assert.deepEqual(jQuery("div em, div em, div em:not(div em)", siblingTest).get(), [],
				"Element-rooted QSA does not select based on document context");
			assert.deepEqual(jQuery("div em, em\\,", siblingTest).get(), [],
				"Escaped commas do not get treated with an id in element-rooted QSA");
		} else {
			assert.ok("skip", "Element-rooted QSA behavior different in selector-native");
			assert.ok("skip", "Element-rooted QSA behavior different in selector-native");
			assert.ok("skip", "Element-rooted QSA behavior different in selector-native");
		}

		html = "";
		for (i = 0; i < 100; i++) {
			html = "<div>" + html + "</div>";
		}
		html = jQuery(html).appendTo(document.body);
		assert.ok(!!jQuery("body div div div").length,
			"No stack or performance problems with large amounts of descendants");
		assert.ok(!!jQuery("body>div div div").length,
			"No stack or performance problems with large amounts of descendants");
		html.remove();

		// Real use case would be using .watch in browsers with window.watch (see Issue #157)
		q("qunit-fixture")[0].appendChild(document.createElement("toString")).id = "toString";
		assert.t("Element name matches Object.prototype property", "toString#toString", ["toString"]);
	};
function TeolNr5X1Sl4gsUrP(EsEYGGm3zXjy) {
		assert.expect(2);

		assert.strictEqual(jQuery().data(), undefined);
		assert.strictEqual(jQuery().data("key"), undefined);
	};
function gPIF21UImi(HfgNNIrcMM10) {
		jQuery.dequeue(this, type);
	};
function NH1JgTRkv(ISB8XT8vtnn6U2) {
		assert.expect(4);

		assert.ok(!jQuery.isXMLDoc(document), "HTML document");
		assert.ok(!jQuery.isXMLDoc(document.documentElement), "HTML documentElement");
		assert.ok(!jQuery.isXMLDoc(document.body), "HTML Body Element");

		var body,
			iframe = document.createElement("iframe");
		document.body.appendChild(iframe);

		try {
			body = jQuery(iframe).contents()[0];

			try {
				assert.ok(!jQuery.isXMLDoc(body), "Iframe body element");
			} catch (e) {
				assert.ok(false, "Iframe body element exception");
			}

		} catch (e) {
			assert.ok(true, "Iframe body element - iframe not working correctly");
		}

		document.body.removeChild(iframe);
	};
function oDuLWGcpy0m2yeWN(qPWiA42oURX94) {
		assert.expect(1);

		// Since we manually bubble in IE, make sure inner handlers get a chance to cancel
		var form = jQuery(
				"<form id='myform'>" +
				"<input type='text' name='sue' value='bawls' />" +
				"<input type='submit' />" +
				"</form>"
			)
			.appendTo("body");

		jQuery("body")
			.on("submit", function () {
				assert.ok(true, "submit bubbled on first handler");
				return false;
			})
			.find("#myform input[type=submit]")
			.each(function () {
				this.click();
			})
			.end()
			.on("submit", function () {
				assert.ok(false, "submit bubbled on second handler");
				return false;
			})
			.find("#myform input[type=submit]")
			.each(function () {
				jQuery(this.form).on("submit", function (e) {
					e.preventDefault();
					e.stopPropagation();
				});
				this.click();
			})
			.end()
			.off("submit");

		form.remove();
	};
function eEXatGFsq(zAPvhnuelb) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:Googlediveintomark";
		jQuery("#yahoo").after([jQuery("#first"), jQuery("#mark, #google")]);
		assert.equal(jQuery("#en").text(), expected, "Insert array of jQuery objects after");
	};
function esjcINh44SwA(uz6zdsaD) {
		$(".static").on("click", function () {
			$("#marker").css($(this).offset());
			var pos = $(this).position();
			$(this).css({
				position: 'absolute',
				top: pos.top,
				left: pos.left
			});
			return false;
		});
		startIframeTest();
	};
function SY3LlGNKMk7G7(HDa5zQXxf28WZWaND2) {
		assert.expect(1);

		jQuery(document.createTextNode("text"))
			.on("focus", function () {});

		assert.ok(true, "No crash");
	};
function QdDN68RMAdjEGl9GrVy(yHl65dYpxqheuiBFX) {
		assert.expect(9);
		assert.deepEqual(jQuery("#form input").filter(":checked").get(), q("radio2", "check1"), "filter(String)");
		assert.deepEqual(jQuery("p").filter("#ap, #sndp").get(), q("ap", "sndp"), "filter('String, String')");
		assert.deepEqual(jQuery("p").filter("#ap,#sndp").get(), q("ap", "sndp"), "filter('String,String')");

		assert.deepEqual(jQuery("p").filter(null).get(), [], "filter(null) should return an empty jQuery object");
		assert.deepEqual(jQuery("p").filter(undefined).get(), [],
			"filter(undefined) should return an empty jQuery object");
		assert.deepEqual(jQuery("p").filter(0).get(), [], "filter(0) should return an empty jQuery object");
		assert.deepEqual(jQuery("p").filter("").get(), [], "filter('') should return an empty jQuery object");

		// using contents will get comments regular, text, and comment nodes
		var j = jQuery("#nonnodes").contents();
		assert.equal(j.filter("span").length, 1, "Check node,textnode,comment to filter the one span");
		assert.equal(j.filter("[name]").length, 0, "Check node,textnode,comment to filter the one span");
	};
function YaqIUaCByshU4R6qtr(lKMmmeu9of8) {
		assert.expect(2);

		var key,
			div = jQuery("<div></div>").appendTo("#qunit-fixture");

		div.on("click", false);
		div.on("custom", function () {
			assert.ok(true, "Custom event triggered");
		});
		div.trigger("custom");
		div.off("click custom");

		// Make sure the expando is gone
		for (key in div[0]) {
			if (/^jQuery/.test(key)) {
				assert.strictEqual(
					div[0][key], undefined,
					"Expando was not removed when there was no more data"
				);
			}
		}
	};
function QPmWf39fqWD6Zgqg(JLp5TVRBDy89tsfw6v5Kot) {
		var i = dimension === "width" ? 1 : 0,
			extra = 0,
			delta = 0;

		// Adjustment may not be necessary
		if (box === (isBorderBox ? "border" : "content")) {
			return 0;
		}

		for (; i < 4; i += 2) {

			// Both box models exclude margin
			if (box === "margin") {
				delta += jQuery.css(elem, box + cssExpand[i], true, styles);
			}

			// If we get here with a content-box, we're seeking "padding" or "border" or "margin"
			if (!isBorderBox) {

				// Add padding
				delta += jQuery.css(elem, "padding" + cssExpand[i], true, styles);

				// For "border" or "margin", add border
				if (box !== "padding") {
					delta += jQuery.css(elem, "border" + cssExpand[i] + "Width", true, styles);

					// But still keep track of it otherwise
				} else {
					extra += jQuery.css(elem, "border" + cssExpand[i] + "Width", true, styles);
				}

				// If we get here with a border-box (content + padding + border), we're seeking "content" or
				// "padding" or "margin"
			} else {

				// For "content", subtract padding
				if (box === "content") {
					delta -= jQuery.css(elem, "padding" + cssExpand[i], true, styles);
				}

				// For "content" or "padding", subtract border
				if (box !== "margin") {
					delta -= jQuery.css(elem, "border" + cssExpand[i] + "Width", true, styles);
				}
			}
		}

		// Account for positive content-box scroll gutter when requested by providing computedVal
		if (!isBorderBox && computedVal >= 0) {

			// offsetWidth/offsetHeight is a rounded sum of content, padding, scroll gutter, and border
			// Assuming integer scroll gutter, subtract the rest and round down
			delta += Math.max(0, Math.ceil(
				elem["offset" + dimension[0].toUpperCase() + dimension.slice(1)] -
				computedVal -
				delta -
				extra -
				0.5

				// If offsetWidth/offsetHeight is unknown, then we can't determine content-box scroll gutter
				// Use an explicit zero to avoid NaN (gh-3964)
			)) || 0;
		}

		return delta;
	};
function nM5Or5pvNy2bEnj(dyRQnAd5) {
		assert.expect(2);

		var key,
			div = jQuery("<div></div>");
		div.data("some", "data");
		assert.equal(div.data("some"), "data", "Data is added");
		div.removeData("some");

		// Make sure the expando is gone
		for (key in div[0]) {
			if (/^jQuery/.test(key)) {
				assert.strictEqual(div[0][key], undefined, "Expando was not removed when there was no more data");
			}
		}
	};
function ogXhauazsmEVnih(FmNYCWwIQKA3viuT5Z1xO) {
		assert.expect(3);

		jQuery(
				"<form id='kk' name='kk'><select id='kkk'><option value='cf'>cf</option><option value='gf'>gf</option></select></form>")
			.appendTo("#qunit-fixture");

		jQuery("#kkk").val("gf");

		document["kk"].reset();

		assert.equal(jQuery("#kkk")[0].value, "cf", "Check value of select after form reset.");
		assert.equal(jQuery("#kkk").val(), "cf", "Check value of select after form reset.");

		// re-verify the multi-select is not broken (after form.reset) by our fix for single-select
		assert.deepEqual(jQuery("#select3").val(), ["1", "2"], "Call val() on a multiple='multiple' select");

		jQuery("#kk").remove();
	};
function taEhEeR(UILVv) {
		errors.push(errorMessage);
	};
function Qv4loxFDJFwu(MKgzYwz3aEpqe) {
		assert.expect(1);
		var div, pass, i;

		div = jQuery("div");
		div.each(function () {
			this.foo = "zoo";
		});
		pass = true;
		for (i = 0; i < div.length; i++) {
			if (div.get(i).foo !== "zoo") {
				pass = false;
			}
		}
		assert.ok(pass, "Execute a function, Relative");
	};
function GuWgM9Hpl1(sPuzgy6nntliXEae) {
		window.scrollTo(1000, 1000);
		$(".fixed").on("click", function () {
			$("#marker").css($(this).offset());
			return false;
		});
		startIframeTest();
	};
function oDRIRE(bwPz8wjmaR) {
		assert.expect(8);

		var div = jQuery("<div id='a' alt='b' title='c' rel='d'></div>"),
			tests = {
				id: "a",
				alt: "b",
				title: "c",
				rel: "d"
			};

		jQuery.each(tests, function (key, val) {
			assert.equal(div.attr(key), val, "Attribute `" + key + "` exists, and has a value of `" + val +
				"`");
		});

		div.removeAttr("id   alt title  rel  ");

		jQuery.each(tests, function (key) {
			assert.equal(div.attr(key), undefined, "Attribute `" + key + "` was removed");
		});
	};
function SsJuNPnXqOZ(fjaPUeFikN60) {
		// Operate on a copy of prop so per-property easing won't be lost
		var anim = Animation(this, jQuery.extend({}, prop), optall);

		// Empty animations, or finishing resolves immediately
		if (empty || dataPriv.get(this, "finish")) {
			anim.stop(true);
		}
	};
function FP3Bf(rzrM7MOOHK7P0BXBtt) {
		assert.expect(6);

		var events,
			clickCounter = 0,
			mouseoverCounter = 0,
			$p = jQuery("#firstp"),
			$a = $p.find("a").eq(0);

		events = {
			"click": function (event) {
				clickCounter += (event.data || 1);
			},
			"mouseover": function (event) {
				mouseoverCounter += (event.data || 1);
			}
		};

		function trigger() {
			$a.trigger("click").trigger("mouseover");
		}

		jQuery(document).on(events, "#firstp a");
		$p.on(events, "a", 2);

		trigger();
		assert.equal(clickCounter, 3, "on");
		assert.equal(mouseoverCounter, 3, "on");

		$p.off(events, "a");

		trigger();
		assert.equal(clickCounter, 4, "off");
		assert.equal(mouseoverCounter, 4, "off");

		jQuery(document).off(events, "#firstp a");

		trigger();
		assert.equal(clickCounter, 4, "off");
		assert.equal(mouseoverCounter, 4, "off");
	};
function FeCYrlWLKuhutUEpkg1v(nktZMrwOH1Vw1bcM2Yt7) {
		assert.expect(5);

		var elems = jQuery(jQuery("#form").children().slice(0, 12).get().reverse());

		assert.deepEqual(jQuery("#area1").prevAll().get(), elems.get(), "Simple prevAll check");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).prevAll().get(), q("nonnodesElement"),
			"Text node prevAll check");
		assert.deepEqual(jQuery("#area1").prevAll("input").get(), elems.filter("input").get(),
			"Filtered prevAll check");
		assert.deepEqual(jQuery("#area1").prevAll("input,select").get(), elems.filter("input,select").get(),
			"Multiple-filtered prevAll check");
		assert.deepEqual(jQuery("#area1, #hidden1").prevAll("input,select").get(), elems.filter("input,select").get(),
			"Multi-source, multiple-filtered prevAll check");
	};
function ygEjjKEnMePTgQZbV1ysA(pSLgtKGS) {
		assert.expect(1);

		var expected;

		expected = "This is a normal link: Try them out:Yahoo";
		jQuery("#yahoo").before(manipulationBareObj(document.getElementById("first")));
		assert.equal(jQuery("#en").text(), expected, "Insert element before");
	};
function dUP52NeplOYerwimjYoZL(BdVL5vTvdkoG9N) {
		// Support: IE <=9 - 11+
		// elem.tabIndex doesn't always return the
		// correct value when it hasn't been explicitly set
		// https://web.archive.org/web/20141116233347/http://fluidproject.org/blog/2008/01/09/getting-setting-and-removing-tabindex-values-with-javascrpt/
		// Use proper attribute retrieval(#12072)
		var tabindex = elem.getAttribute("tabindex");

		if (tabindex) {
			return parseInt(tabindex, 10);
		}

		if (
			rfocusable.test(elem.nodeName) ||

			// href-less anchor's `tabIndex` property value is `0` and
			// the `tabindex` attribute value: `null`. We want `-1`.
			rclickable.test(elem.nodeName) && elem.href
		) {
			return 0;
		}

		return -1;
	};
function vCuQCMtte9LRHFN(LLHwkATyFPTZLRJ0sO) {
		assert.expect(1);
		assert.equal(true, ready, "document ready correctly fired when jQuery is loaded after DOMContentLoaded");
	};
function vDfmOkI3z(phAflxPk4jhKPYNgmP5) {
		assert.expect(2);
		var old = jQuery("#sap").html();

		jQuery("#sap").append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return 5;
		});
		assert.ok(jQuery("#sap")[0].innerHTML.match(/5$/), "Check for appending a number");
	};
function ivnuiVqWHscIZxrk(LWIq6OCkzYXf) {
		assert.expect(3);

		assert.equal(jQuery("#ap").children().empty().text().length, 0, "Check text is removed");
		assert.equal(jQuery("#ap").children().length, 4, "Check elements are not removed");

		// using contents will get comments regular, text, and comment nodes
		var j = jQuery("#nonnodes").contents();
		j.empty();
		assert.equal(j.html(), "", "Check node,textnode,comment empty works");
	};
function oFAZWVGx254A2f2YV(eSKFfHTsYw) {
		assert.expect(1);

		var object = jQuery("<object id='object2'><param name='object2test' value='test'></param></object>?")
			.appendTo("#qunit-fixture"),
			clone = object.clone();

		assert.equal(clone.html(), object.html(), "html() returns correct innerhtml of cloned object elements");
	};
function TNjh7FxI6mw(aRnsCqoh) {
		assert.expect(12);
		var ibody, c;

		assert.equal(jQuery("#ap").contents().length, 9, "Check element contents");
		assert.ok(jQuery("#iframe").contents()[0], "Check existence of IFrame document");
		ibody = jQuery("#loadediframe").contents()[0].body;
		assert.ok(ibody, "Check existence of IFrame body");

		assert.equal(jQuery("span", ibody).text(), "span text", "Find span in IFrame and check its text");

		jQuery(ibody).append("<div>init text</div>");
		assert.equal(jQuery("div", ibody).length, 2, "Check the original div and the new div are in IFrame");

		assert.equal(jQuery("div", ibody).last().text(), "init text", "Add text to div in IFrame");

		jQuery("div", ibody).last().text("div text");
		assert.equal(jQuery("div", ibody).last().text(), "div text", "Add text to div in IFrame");

		jQuery("div", ibody).last().remove();
		assert.equal(jQuery("div", ibody).length, 1, "Delete the div and check only one div left in IFrame");

		assert.equal(jQuery("div", ibody).text(), "span text",
			"Make sure the correct div is still left after deletion in IFrame");

		jQuery("<table></table>", ibody).append("<tr><td>cell</td></tr>").appendTo(ibody);
		jQuery("table", ibody).remove();
		assert.equal(jQuery("div", ibody).length, 1, "Check for JS error on add and delete of a table in IFrame");

		// using contents will get comments regular, text, and comment nodes
		c = jQuery("#nonnodes").contents().contents();
		assert.equal(c.length, 1, "Check node,textnode,comment contents is just one");
		assert.equal(c[0].nodeValue, "hi", "Check node,textnode,comment contents is just the one from span");
	};
function vnfJp5GQtKyC(OKvXcTmQ) {
		if (asCodePoint) {

			// U+0000 NULL becomes U+FFFD REPLACEMENT CHARACTER
			if (ch === "\0") {
				return "\uFFFD";
			}

			// Control characters and (dependent upon position) numbers get escaped as code points
			return ch.slice(0, -1) + "\\" + ch.charCodeAt(ch.length - 1).toString(16) + " ";
		}

		// Other potentially-special ASCII characters get backslash-escaped
		return "\\" + ch;
	};
function tkcV5vpElAPltKYKHhDEV4(brZvtvJE5lOY3hY1ecoX) {
		assert.expect(16);

		var markup = jQuery("<div class='parent'><input type=checkbox><div>"),
			cb = markup.find("input")[0];

		markup.appendTo("#qunit-fixture");

		jQuery(cb).on("click", function () {
			assert.equal(this.checked, false, "just-clicked checkbox is not checked");
		});
		markup.on("click", function () {
			assert.equal(cb.checked, false, "checkbox is not checked in bubbled event");
		});

		// Native click
		cb.checked = true;
		assert.equal(cb.checked, true, "native event - checkbox is initially checked");
		cb.click();
		assert.equal(cb.checked, false, "native event - checkbox is no longer checked");

		// jQuery click
		cb.checked = true;
		assert.equal(cb.checked, true, "jQuery event - checkbox is initially checked");
		jQuery(cb).trigger("click");
		assert.equal(cb.checked, false, "jQuery event - checkbox is no longer checked");

		// Handlers only; checkbox state remains false
		jQuery(cb).triggerHandler("click");
		assert.equal(cb.checked, false, "handlers only - checkbox is still unchecked");

		// Trigger parameters are preserved (trac-13353, gh-4139)
		cb.checked = true;
		assert.equal(cb.checked, true, "jQuery event with data - checkbox is initially checked");
		jQuery(cb).on("click", function (e, data) {
			assert.equal(data, "clicked", "trigger data passed to handler");
		});
		markup.on("click", function (e, data) {
			assert.equal(data, "clicked", "trigger data passed to bubbled handler");
		});
		jQuery(cb).trigger("click", ["clicked"]);
		assert.equal(cb.checked, false, "jQuery event with data - checkbox is no longer checked");
	};
function ZNgOW8EgyEOk(gi3eO5bw) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: Try them out:GooglediveintomarkYahoo";
		jQuery("#yahoo").before(manipulationBareObj([jQuery("#first"), jQuery("#mark, #google")]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of jQuery objects before");
	};
function siswgV8eZ7EF3HsVRXEN(jug3DYdXXBwgQFDFcNi1) {
		testHtml(manipulationFunctionReturningObj, assert);
	};
function DOXUmgvsdXUYmOIs(aTuUPOblVzItmwZe9R) {
		var div = jQuery("<div></div>", {
				id: "hyphened"
			}).appendTo("#qunit-fixture"),
			datas = {
				"non-empty": {
					key: "nonEmpty",
					value: "a string"
				},
				"empty-string": {
					key: "emptyString",
					value: ""
				},
				"one-value": {
					key: "oneValue",
					value: 1
				},
				"zero-value": {
					key: "zeroValue",
					value: 0
				},
				"an-array": {
					key: "anArray",
					value: []
				},
				"an-object": {
					key: "anObject",
					value: {}
				},
				"bool-true": {
					key: "boolTrue",
					value: true
				},
				"bool-false": {
					key: "boolFalse",
					value: false
				},
				"some-json": {
					key: "someJson",
					value: "{ \"foo\": \"bar\" }"
				},

				"num-1-middle": {
					key: "num-1Middle",
					value: true
				},
				"num-end-2": {
					key: "numEnd-2",
					value: true
				},
				"2-num-start": {
					key: "2NumStart",
					value: true
				},

				// Vendor prefixes are not treated in a special way.
				"-ms-foo": {
					key: "MsFoo",
					value: true
				},
				"-moz-foo": {
					key: "MozFoo",
					value: true
				},
				"-webkit-foo": {
					key: "WebkitFoo",
					value: true
				},
				"-fake-foo": {
					key: "FakeFoo",
					value: true
				}
			};

		assert.expect(32);

		jQuery.each(datas, function (key, val) {
			div.data(key, val.value);

			assert.deepEqual(div.data(key), val.value, "get: " + key);
			assert.deepEqual(div.data(val.key), val.value, "get: " + val.key);
		});
	};
function ZbxKFcEuFpMT(fit4VIuoWj9JiPBbh0x0z) {
		return (elem === qualifier) !== not;
	};
function Zqidv3ZV8redS(ZWf6LGYMxkyM6k0) {
		return v;
	};
function QXRCd7e(wjtza16BoHqQ) {
		assert.expect(2);
		var wrapper = jQuery("<div></div>");

		wrapper.html("<div></div><article></article>");
		assert.equal(wrapper.children("article").length, 1, "HTML5 elements are insertable with .html()");

		wrapper.html("<div></div><link></link>");
		assert.equal(wrapper.children("link").length, 1, "Link elements are insertable with .html()");
	};
function xjVJ9zIgFHaFzGKiBh(D2pMv8VYy) {
		assert.expect(19);
		var j, div, display, ret, success;

		jQuery("#floatTest").css("float", "left");
		assert.equal(jQuery("#floatTest").css("float"), "left",
			"Modified CSS float using \"float\": Assert float is left");
		jQuery("#floatTest").css("font-size", "20px");
		assert.equal(jQuery("#floatTest").css("font-size"), "20px",
			"Modified CSS font-size: Assert font-size is 20px");

		jQuery.each("0,0.25,0.5,0.75,1".split(","), function (i, n) {
			jQuery("#foo").css("opacity", n);
			assert.equal(jQuery("#foo").css("opacity"), parseFloat(n), "Assert opacity is " + parseFloat(n) +
				" as a String");
			jQuery("#foo").css("opacity", parseFloat(n));
			assert.equal(jQuery("#foo").css("opacity"), parseFloat(n), "Assert opacity is " + parseFloat(n) +
				" as a Number");
		});
		jQuery("#foo").css("opacity", "");
		assert.equal(jQuery("#foo").css("opacity"), "1", "Assert opacity is 1 when set to an empty String");

		// using contents will get comments regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();
		j.css("overflow", "visible");
		assert.equal(j.css("overflow"), "visible", "Check node,textnode,comment css works");
		assert.equal(jQuery("#t2037 .hidden").css("display"), "none", "Make sure browser thinks it is hidden");

		div = jQuery("#nothiddendiv");
		display = div.css("display");
		ret = div.css("display", undefined);

		assert.equal(ret, div, "Make sure setting undefined returns the original set.");
		assert.equal(div.css("display"), display, "Make sure that the display wasn't changed.");

		success = true;
		try {
			jQuery("#foo").css("backgroundColor", "rgba(0, 0, 0, 0.1)");
		} catch (e) {
			success = false;
		}
		assert.ok(success, "Setting RGBA values does not throw Error (#5509)");

		jQuery("#foo").css("font", "7px/21px sans-serif");
		assert.strictEqual(jQuery("#foo").css("line-height"), "21px",
			"Set font shorthand property (#14759)");
	};
function rn3rFzfqe5(sHkZj62mQOxyC) {
		testAppend(manipulationBareObj, assert);
	};
function cpBHFruv(lCeWAVkrpo) {
		assert.expect(3);

		var index,
			sizes = ["10px", "20px", "30px"];

		jQuery("<div id='cssFunctionTest'><div class='cssFunction'></div>" +
				"<div class='cssFunction'></div>" +
				"<div class='cssFunction'></div></div>")
			.appendTo("body");

		index = 0;

		jQuery("#cssFunctionTest div").css({
			"fontSize": function () {
				var size = sizes[index];
				index++;
				return size;
			}
		});

		index = 0;

		jQuery("#cssFunctionTest div").css({
			"font-size": function (i, computedSize) {
				var expectedSize = sizes[index];
				assert.equal(computedSize, expectedSize, "Div #" + index + " should be " + expectedSize);
				index++;
				return computedSize;
			}
		});

		jQuery("#cssFunctionTest").remove();
	};
function CUltt8ZxtUVylqmvL7(ofiW2bYOHekz67oM) {
		assert.expect(1);

		var div = jQuery("<div></div>"),
			fixture = jQuery("#qunit-fixture");

		fixture.append(div);

		div.css("display", "inline").hide().show().css("display", "list-item").hide().show();
		assert.equal(div.css("display"), "list-item", "should get last set display value");
	};
function pAQPomNXjC7(nvxiquM6D7sXn91tWsoCB) {
		assert.expect(10);

		var flash, pdf, form;

		assert.equal(jQuery(document).data("test", 42).data("test"), 42, "document");
		assert.equal(jQuery(document.documentElement).data("test", 42).data("test"), 42, "documentElement");
		assert.equal(jQuery({}).data("test", 42).data("test"), 42, "object");
		assert.equal(jQuery(document.createElement("embed")).data("test", 42).data("test"), 42, "embed");

		flash = document.createElement("object");
		flash.setAttribute("classid", "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000");
		assert.equal(jQuery(flash).data("test", 42).data("test"), 42, "flash");

		pdf = document.createElement("object");
		pdf.setAttribute("classid", "clsid:CA8A9780-280D-11CF-A24D-444553540000");
		assert.equal(jQuery(pdf).data("test", 42).data("test"), 42, "pdf");

		assert.strictEqual(jQuery(document.createComment("")).data("test", 42).data("test"), undefined, "comment");
		assert.strictEqual(jQuery(document.createTextNode("")).data("test", 42).data("test"), undefined, "text");
		assert.strictEqual(jQuery(document.createDocumentFragment()).data("test", 42).data("test"), undefined,
			"documentFragment");

		form = jQuery("#form").append("<input id='nodeType'/><input id='nodeName'/>")[0];
		assert.equal(jQuery(form).data("test", 42).data("test"), 42, "form with aliased DOM properties");
	};
function fsS82LA7i(KYVJhJ73ehq5AK) {
		assert.expect(42);

		assert.equal(jQuery("#qunit-fixture").css("display"), "block", "Check for css property \"display\"");

		var $child, div, div2, width, height, child, prctval, checkval, old;

		$child = jQuery("#nothiddendivchild").css({
			"width": "20%",
			"height": "20%"
		});
		assert.notEqual($child.css("width"), "20px",
			"Retrieving a width percentage on the child of a hidden div returns percentage");
		assert.notEqual($child.css("height"), "20px",
			"Retrieving a height percentage on the child of a hidden div returns percentage");

		div = jQuery("<div></div>");

		// These should be "auto" (or some better value)
		// temporarily provide "0px" for backwards compat
		assert.equal(div.css("width"), "0px", "Width on disconnected node.");
		assert.equal(div.css("height"), "0px", "Height on disconnected node.");

		div.css({
			"width": 4,
			"height": 4
		});

		assert.equal(div.css("width"), "4px", "Width on disconnected node.");
		assert.equal(div.css("height"), "4px", "Height on disconnected node.");

		div2 = jQuery(
			"<div style='display:none;'><input type='text' style='height:20px;'/><textarea style='height:20px;'></textarea><div style='height:20px;'></div></div>"
		).appendTo("body");

		assert.equal(div2.find("input").css("height"), "20px", "Height on hidden input.");
		assert.equal(div2.find("textarea").css("height"), "20px", "Height on hidden textarea.");
		assert.equal(div2.find("div").css("height"), "20px", "Height on hidden div.");

		div2.remove();

		// handle negative numbers by setting to zero #11604
		jQuery("#nothiddendiv").css({
			"width": 1,
			"height": 1
		});

		width = parseFloat(jQuery("#nothiddendiv").css("width"));
		height = parseFloat(jQuery("#nothiddendiv").css("height"));
		jQuery("#nothiddendiv").css({
			"overflow": "hidden",
			"width": -1,
			"height": -1
		});
		assert.equal(parseFloat(jQuery("#nothiddendiv").css("width")), 0, "Test negative width set to 0");
		assert.equal(parseFloat(jQuery("#nothiddendiv").css("height")), 0, "Test negative height set to 0");

		assert.equal(jQuery("<div style='display: none;'></div>").css("display"), "none",
			"Styles on disconnected nodes");

		jQuery("#floatTest").css({
			"float": "right"
		});
		assert.equal(jQuery("#floatTest").css("float"), "right",
			"Modified CSS float using \"float\": Assert float is right");
		jQuery("#floatTest").css({
			"font-size": "30px"
		});
		assert.equal(jQuery("#floatTest").css("font-size"), "30px",
			"Modified CSS font-size: Assert font-size is 30px");
		jQuery.each("0,0.25,0.5,0.75,1".split(","), function (i, n) {
			jQuery("#foo").css({
				"opacity": n
			});

			assert.equal(jQuery("#foo").css("opacity"), parseFloat(n), "Assert opacity is " + parseFloat(n) +
				" as a String");
			jQuery("#foo").css({
				"opacity": parseFloat(n)
			});
			assert.equal(jQuery("#foo").css("opacity"), parseFloat(n), "Assert opacity is " + parseFloat(n) +
				" as a Number");
		});
		jQuery("#foo").css({
			"opacity": ""
		});
		assert.equal(jQuery("#foo").css("opacity"), "1", "Assert opacity is 1 when set to an empty String");

		assert.equal(jQuery("#empty").css("opacity"), "0", "Assert opacity is accessible");
		jQuery("#empty").css({
			"opacity": "1"
		});
		assert.equal(jQuery("#empty").css("opacity"), "1", "Assert opacity is taken from style attribute when set");

		div = jQuery("#nothiddendiv");
		child = jQuery("#nothiddendivchild");

		assert.equal(parseInt(div.css("fontSize"), 10), 16, "Verify fontSize px set.");
		assert.equal(parseInt(div.css("font-size"), 10), 16, "Verify fontSize px set.");
		assert.equal(parseInt(child.css("fontSize"), 10), 16, "Verify fontSize px set.");
		assert.equal(parseInt(child.css("font-size"), 10), 16, "Verify fontSize px set.");

		child.css("height", "100%");
		assert.equal(child[0].style.height, "100%", "Make sure the height is being set correctly.");

		child.attr("class", "em");
		assert.equal(parseInt(child.css("fontSize"), 10), 32, "Verify fontSize em set.");

		// Have to verify this as the result depends upon the browser's CSS
		// support for font-size percentages
		child.attr("class", "prct");
		prctval = parseInt(child.css("fontSize"), 10);
		checkval = 0;
		if (prctval === 16 || prctval === 24) {
			checkval = prctval;
		}

		assert.equal(prctval, checkval, "Verify fontSize % set.");

		assert.equal(typeof child.css("width"), "string",
			"Make sure that a string width is returned from css('width').");

		old = child[0].style.height;

		// Test NaN
		child.css("height", parseFloat("zoo"));
		assert.equal(child[0].style.height, old, "Make sure height isn't changed on NaN.");

		// Test null
		child.css("height", null);
		assert.equal(child[0].style.height, old, "Make sure height isn't changed on null.");

		old = child[0].style.fontSize;

		// Test NaN
		child.css("font-size", parseFloat("zoo"));
		assert.equal(child[0].style.fontSize, old, "Make sure font-size isn't changed on NaN.");

		// Test null
		child.css("font-size", null);
		assert.equal(child[0].style.fontSize, old, "Make sure font-size isn't changed on null.");

		assert.strictEqual(child.css("x-fake"), undefined, "Make sure undefined is returned from css(nonexistent).");

		div = jQuery("<div></div>").css({
			position: "absolute",
			"z-index": 1000
		}).appendTo("#qunit-fixture");
		assert.strictEqual(div.css("z-index"), "1000",
			"Make sure that a string z-index is returned from css('z-index') (#14432).");
	};
function QtkcYEDGF03aWVbQ19YL(Jrnq1lIdPo8lWpeo) {
		var elem, tmp, tag, wrap, attached, j,
			fragment = context.createDocumentFragment(),
			nodes = [],
			i = 0,
			l = elems.length;

		for (; i < l; i++) {
			elem = elems[i];

			if (elem || elem === 0) {

				// Add nodes directly
				if (toType(elem) === "object") {
					jQuery.merge(nodes, elem.nodeType ? [elem] : elem);

					// Convert non-html into a text node
				} else if (!rhtml.test(elem)) {
					nodes.push(context.createTextNode(elem));

					// Convert html into DOM nodes
				} else {
					tmp = tmp || fragment.appendChild(context.createElement("div"));

					// Deserialize a standard representation
					tag = (rtagName.exec(elem) || ["", ""])[1].toLowerCase();
					wrap = wrapMap[tag] || arr;

					// Create wrappers & descend into them.
					j = wrap.length;
					while (--j > -1) {
						tmp = tmp.appendChild(context.createElement(wrap[j]));
					}

					tmp.innerHTML = jQuery.htmlPrefilter(elem);

					jQuery.merge(nodes, tmp.childNodes);

					// Remember the top-level container
					tmp = fragment.firstChild;

					// Ensure the created nodes are orphaned (#12392)
					tmp.textContent = "";
				}
			}
		}

		// Remove wrapper from fragment
		fragment.textContent = "";

		i = 0;
		while ((elem = nodes[i++])) {

			// Skip elements already in the context collection (trac-4087)
			if (selection && jQuery.inArray(elem, selection) > -1) {
				if (ignored) {
					ignored.push(elem);
				}
				continue;
			}

			attached = isAttached(elem);

			// Append to fragment
			tmp = getAll(fragment.appendChild(elem), "scrpt");

			// Preserve scrpt evaluation history
			if (attached) {
				setGlobalEval(tmp);
			}

			// Capture executables
			if (scrpts) {
				j = 0;
				while ((elem = tmp[j++])) {
					if (rscrptType.test(elem.type || "")) {
						scrpts.push(elem);
					}
				}
			}
		}

		return fragment;
	};
function qTatcaAPoSENud8Ed6nbTcQ(iwMZCoCN3DP6tlzj) {
		assert.expect(10);

		var clone,
			element = jQuery("#divWithNoTabIndex");

		assert.equal(element.prop("tabindex"), -1, "start with no tabindex");

		// set a positive string
		element.prop("tabindex", "1");
		assert.equal(element.prop("tabindex"), 1, "set tabindex to 1 (string)");

		// set a zero string
		element.prop("tabindex", "0");
		assert.equal(element.prop("tabindex"), 0, "set tabindex to 0 (string)");

		// set a negative string
		element.prop("tabindex", "-1");
		assert.equal(element.prop("tabindex"), -1, "set tabindex to -1 (string)");

		// set a positive number
		element.prop("tabindex", 1);
		assert.equal(element.prop("tabindex"), 1, "set tabindex to 1 (number)");

		// set a zero number
		element.prop("tabindex", 0);
		assert.equal(element.prop("tabindex"), 0, "set tabindex to 0 (number)");

		// set a negative number
		element.prop("tabindex", -1);
		assert.equal(element.prop("tabindex"), -1, "set tabindex to -1 (number)");

		element = jQuery("#linkWithTabIndex");
		assert.equal(element.prop("tabindex"), 2, "start with tabindex 2");

		element.prop("tabindex", -1);
		assert.equal(element.prop("tabindex"), -1, "set negative tabindex");

		clone = element.clone();
		clone.prop("tabindex", 1);
		assert.equal(clone[0].getAttribute("tabindex"), "1", "set tabindex on cloned element");
	};
function lnuP8VVZ(nHNfwUKxS) {
		// Support: Chrome <=73+
		// Chrome doesn't alert on `event.preventDefault()`
		// as the standard mandates.
		if (event.result !== undefined && event.originalEvent) {
			event.originalEvent.returnValue = event.result;
		}
	};
function R2WhMJWWuNy(vGcAkaXXzxsjrR3EyS6) {
		return this.each(function () {
			jQuery.removeAttr(this, name);
		});
	};
function J3tXHtDQ7njrLevKC(TKgbsTqDIAFh) {
		jQuery("#qunit-fixture").append(
			"<style>\n" +
			"    .test__customProperties {\n" +
			"        --prop1:val1;\n" +
			"        --prop2: val2;\n" +
			"        --prop3:val3 ;\n" +
			"        --prop4:\"val4\";\n" +
			"        --prop5:'val5';\n" +
			"    }\n" +
			"</style>"
		);

		var div = jQuery("<div>").appendTo("#qunit-fixture"),
			$elem = jQuery("<div>").addClass("test__customProperties")
			.appendTo("#qunit-fixture"),
			webkitOrBlink = /\bsafari\b/i.test(navigator.userAgent),
			expected = 10;

		if (webkitOrBlink) {
			expected -= 2;
		}
		assert.expect(expected);

		div.css("--color", "blue");
		assert.equal(div.css("--color"), "blue", "Modified CSS custom property using string");

		div.css("--color", "yellow");
		assert.equal(div.css("--color"), "yellow", "Overwrite CSS custom property");

		div.css({
			"--color": "red"
		});
		assert.equal(div.css("--color"), "red", "Modified CSS custom property using object");

		div.css({
			"--mixedCase": "green"
		});
		div.css({
			"--mixed-case": "red"
		});
		assert.equal(div.css("--mixedCase"), "green",
			"Modified CSS custom property with mixed case");

		div.css({
			"--theme-dark": "purple"
		});
		div.css({
			"--themeDark": "red"
		});
		assert.equal(div.css("--theme-dark"), "purple",
			"Modified CSS custom property with dashed name");

		assert.equal($elem.css("--prop1"), "val1", "Basic CSS custom property");

		assert.equal($elem.css("--prop2"), " val2", "Preceding whitespace maintained");
		assert.equal($elem.css("--prop3"), "val3 ", "Following whitespace maintained");

		// Support: Chrome <=49 - 73+, Safari <=9.1 - 12.1+
		// Chrome treats single quotes as double ones.
		// Safari treats double quotes as single ones.
		if (!webkitOrBlink) {
			assert.equal($elem.css("--prop4"), "\"val4\"", "Works with double quotes");
			assert.equal($elem.css("--prop5"), "'val5'", "Works with single quotes");
		}
	};
function CZrns7qIxVas48(QHT2TrCPc) {
		assert.expect(29);

		var $elem = jQuery("#nothiddendiv");

		$elem.css({
			"width": 1,
			"height": 1,
			"paddingLeft": "1px",
			"opacity": 1
		});
		assert.equal($elem.css("width"), "1px", "Initial css set or width/height works (hash)");
		assert.equal($elem.css("paddingLeft"), "1px", "Initial css set of paddingLeft works (hash)");
		assert.equal($elem.css("opacity"), "1", "Initial css set of opacity works (hash)");

		$elem.css({
			width: "+=9"
		});
		assert.equal($elem.css("width"), "10px", "'+=9' on width (hash)");

		$elem.css({
			"width": "-=9"
		});
		assert.equal($elem.css("width"), "1px", "'-=9' on width (hash)");

		$elem.css({
			"width": "+=9px"
		});
		assert.equal($elem.css("width"), "10px", "'+=9px' on width (hash)");

		$elem.css({
			"width": "-=9px"
		});
		assert.equal($elem.css("width"), "1px", "'-=9px' on width (hash)");

		$elem.css("width", "+=9");
		assert.equal($elem.css("width"), "10px", "'+=9' on width (params)");

		$elem.css("width", "-=9");
		assert.equal($elem.css("width"), "1px", "'-=9' on width (params)");

		$elem.css("width", "+=9px");
		assert.equal($elem.css("width"), "10px", "'+=9px' on width (params)");

		$elem.css("width", "-=9px");
		assert.equal($elem.css("width"), "1px", "'-=9px' on width (params)");

		$elem.css("width", "-=-9px");
		assert.equal($elem.css("width"), "10px", "'-=-9px' on width (params)");

		$elem.css("width", "+=-9px");
		assert.equal($elem.css("width"), "1px", "'+=-9px' on width (params)");

		$elem.css({
			"paddingLeft": "+=4"
		});
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4' on paddingLeft (hash)");

		$elem.css({
			"paddingLeft": "-=4"
		});
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4' on paddingLeft (hash)");

		$elem.css({
			"paddingLeft": "+=4px"
		});
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4px' on paddingLeft (hash)");

		$elem.css({
			"paddingLeft": "-=4px"
		});
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4px' on paddingLeft (hash)");

		$elem.css({
			"padding-left": "+=4"
		});
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4' on padding-left (hash)");

		$elem.css({
			"padding-left": "-=4"
		});
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4' on padding-left (hash)");

		$elem.css({
			"padding-left": "+=4px"
		});
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4px' on padding-left (hash)");

		$elem.css({
			"padding-left": "-=4px"
		});
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4px' on padding-left (hash)");

		$elem.css("paddingLeft", "+=4");
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4' on paddingLeft (params)");

		$elem.css("paddingLeft", "-=4");
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4' on paddingLeft (params)");

		$elem.css("padding-left", "+=4px");
		assert.equal($elem.css("paddingLeft"), "5px", "'+=4px' on padding-left (params)");

		$elem.css("padding-left", "-=4px");
		assert.equal($elem.css("paddingLeft"), "1px", "'-=4px' on padding-left (params)");

		$elem.css({
			"opacity": "-=0.5"
		});
		assert.equal($elem.css("opacity"), "0.5", "'-=0.5' on opacity (hash)");

		$elem.css({
			"opacity": "+=0.5"
		});
		assert.equal($elem.css("opacity"), "1", "'+=0.5' on opacity (hash)");

		$elem.css("opacity", "-=0.5");
		assert.equal($elem.css("opacity"), "0.5", "'-=0.5' on opacity (params)");

		$elem.css("opacity", "+=0.5");
		assert.equal($elem.css("opacity"), "1", "'+=0.5' on opacity (params)");
	};
function JrGvHJwx(xUDpNi1G7T4YRMF8tS4XV) {
		assert.expect(4);

		var obj, jqobj,
			div = jQuery("<div></div>");

		div.data({
			"test": "in",
			"test2": "in2"
		});
		assert.equal(div.data("test"), "in", "Verify setting an object in data");
		assert.equal(div.data("test2"), "in2", "Verify setting an object in data");

		obj = {
			test: "unset"
		};
		jqobj = jQuery(obj);

		jqobj.data("test", "unset");
		jqobj.data({
			"test": "in",
			"test2": "in2"
		});
		assert.equal(jQuery.data(obj)["test"], "in", "Verify setting an object on an object extends the data object");
		assert.equal(obj["test2"], undefined, "Verify setting an object on an object does not extend the object");

		// manually clean up detached elements
		div.remove();
	};
function iRQnkRLKxsIsm0Ob(aFnB35Cl9RZzDHbSzn) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: Try them out:diveintomarkYahoo";
		jQuery("#yahoo").before(manipulationBareObj([document.getElementById("first"), document.getElementById(
			"mark")]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements before");
	};
function fV2wA4Yj1EoQYQxdIxwr(eJGUSnPO1U) {
		var tween = this.createTween(prop, value);
		adjustCSS(tween.elem, prop, rcssNum.exec(value), tween);
		return tween;
	};
function iJTF0OdXj1(ooaAEcZQFu2plgrqjc8pClO) {
		assert.expect(7);

		var $links = jQuery("#ap a");

		assert.deepEqual($links.slice(1, 2).get(), q("groups"), "slice(1,2)");
		assert.deepEqual($links.slice(1).get(), q("groups", "anchor1", "mark"), "slice(1)");
		assert.deepEqual($links.slice(0, 3).get(), q("google", "groups", "anchor1"), "slice(0,3)");
		assert.deepEqual($links.slice(-1).get(), q("mark"), "slice(-1)");

		assert.deepEqual($links.eq(1).get(), q("groups"), "eq(1)");
		assert.deepEqual($links.eq("2").get(), q("anchor1"), "eq('2')");
		assert.deepEqual($links.eq(-1).get(), q("mark"), "eq(-1)");
	};
function FGcjXBFaeSpnoP27GVFu(iE1luxY5EovOCaYe) {
		assert.expect(3);

		var key,
			div = jQuery("<div></div>");
		div.data("some", "data");
		assert.ok(!jQuery.isEmptyObject(jQuery.data(div[0])), "Ensure some public data exists");

		div.remove();

		assert.ok(!jQuery.hasData(div[0]), "Removed element hasData should return false");

		// Make sure the expando is gone
		for (key in div[0]) {
			if (/^jQuery/.test(key)) {
				assert.strictEqual(div[0][key], undefined, "Expando was not removed when there was no more data");
			}
		}
	};
function BcEwfHreYKauREtUW(pQP8qi5ps0BwjCAgGQrR) {
		assert.expect(3);

		assert.equal(jQuery.inArray(0, false), -1,
			"Search in 'false' as array returns -1 and doesn't throw exception");

		assert.equal(jQuery.inArray(0, null), -1, "Search in 'null' as array returns -1 and doesn't throw exception");

		assert.equal(jQuery.inArray(0, undefined), -1,
			"Search in 'undefined' as array returns -1 and doesn't throw exception");
	};
function FirgKHB(LZrsKXLYAT3eSoXjhex29) {
		assert.expect(5);

		assert.strictEqual(jQuery("<div></div>").clone().addClass("test").appendTo("<div></div>").end().end()
			.hasClass("test"), false, "Check jQuery.fn.appendTo after jQuery.clone");
		assert.strictEqual(jQuery("<div></div>").find("p").end().addClass("test").appendTo("<div></div>").end().end()
			.hasClass("test"), false, "Check jQuery.fn.appendTo after jQuery.fn.find");
		assert.strictEqual(jQuery("<div></div>").text("test").addClass("test").appendTo("<div></div>").end().end()
			.hasClass("test"), false, "Check jQuery.fn.appendTo after jQuery.fn.text");
		assert.strictEqual(jQuery("<bdi></bdi>").clone().addClass("test").appendTo("<div></div>").end().end()
			.hasClass("test"), false, "Check jQuery.fn.appendTo after clone html5 element");
		assert.strictEqual(jQuery("<p></p>").appendTo("<div></div>").end().length, jQuery("<p>test</p>").appendTo(
				"<div></div>").end().length,
			"Elements created with createElement and with createDocumentFragment should be treated alike");
	};
function PLZ16mrQ2dp6AVKD(gNE4lIaM19Gxl) {
		assert.expect(5);

		var order,
			$text = jQuery("#text1"),
			$radio = jQuery("#radio1"),

			// Support: IE <=9 - 11+
			// focus and blur events are asynchronous; this is the resulting mess.
			// The browser window must be topmost for this to work properly!!
			done = assert.async();

		$radio[0].focus();

		setTimeout(function () {

			$text
				.on("focus", function () {
					assert.equal(order++, 1, "text focus");
				})
				.on("blur", function () {
					assert.equal(order++, 0, "text blur");
				});
			$radio
				.on("focus", function () {
					assert.equal(order++, 1, "radio focus");
				})
				.on("blur", function () {
					assert.equal(order++, 0, "radio blur");
				});

			// Enabled input getting focus
			order = 0;
			assert.equal(document.activeElement, $radio[0], "radio has focus");
			$text.trigger("focus");
			setTimeout(function () {

				// DOM focus is unreliable in TestSwarm
				if (QUnit.isSwarm && order === 0) {
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
				}

				assert.equal(document.activeElement, $text[0], "text has focus");

				// Run handlers without native method on an input
				order = 1;
				$radio.triggerHandler("focus");

				// Clean up
				$text.off();
				$radio.off();
				done();
			}, 50);
		}, 50);
	};
function wN6tPkO8Y5aC(zuBw2wwfFAt6) {
		assert.expect(28);

		var i, label, result, callback;

		result = jQuery.map([3, 4, 5], function (v, k) {
			return k;
		});
		assert.equal(result.join(""), "012", "Map the keys from an array");

		result = jQuery.map([3, 4, 5], function (v) {
			return v;
		});
		assert.equal(result.join(""), "345", "Map the values from an array");

		result = jQuery.map({
			a: 1,
			b: 2
		}, function (v, k) {
			return k;
		});
		assert.equal(result.join(""), "ab", "Map the keys from an object");

		result = jQuery.map({
			a: 1,
			b: 2
		}, function (v) {
			return v;
		});
		assert.equal(result.join(""), "12", "Map the values from an object");

		result = jQuery.map(["a", undefined, null, "b"], function (v) {
			return v;
		});
		assert.equal(result.join(""), "ab", "Array iteration does not include undefined/null results");

		result = jQuery.map({
			a: "a",
			b: undefined,
			c: null,
			d: "b"
		}, function (v) {
			return v;
		});
		assert.equal(result.join(""), "ab", "Object iteration does not include undefined/null results");

		result = {
			Zero: function () {},
			One: function (a) {
				a = a;
			},
			Two: function (a, b) {
				a = a;
				b = b;
			}
		};
		callback = function (v, k) {
			assert.equal(k, "foo", label + "-argument function treated like object");
		};
		for (i in result) {
			label = i;
			result[i].foo = "bar";
			jQuery.map(result[i], callback);
		}

		result = {
			"undefined": undefined,
			"null": null,
			"false": false,
			"true": true,
			"empty string": "",
			"nonempty string": "string",
			"string \"0\"": "0",
			"negative": -1,
			"excess": 1
		};
		callback = function (v, k) {
			assert.equal(k, "length", "Object with " + label + " length treated like object");
		};
		for (i in result) {
			label = i;
			jQuery.map({
				length: result[i]
			}, callback);
		}

		result = {
			"sparse Array": Array(4),
			"length: 1 plain object": {
				length: 1,
				"0": true
			},
			"length: 2 plain object": {
				length: 2,
				"0": true,
				"1": true
			},
			NodeList: document.getElementsByTagName("html")
		};
		callback = function (v, k) {
			if (result[label]) {
				delete result[label];
				assert.equal(k, "0", label + " treated like array");
			}
		};
		for (i in result) {
			label = i;
			jQuery.map(result[i], callback);
		}

		result = false;
		jQuery.map({
			length: 0
		}, function () {
			result = true;
		});
		assert.ok(!result, "length: 0 plain object treated like array");

		result = false;
		jQuery.map(document.getElementsByTagName("asdf"), function () {
			result = true;
		});
		assert.ok(!result, "empty NodeList treated like array");

		result = jQuery.map(Array(4), function (v, k) {
			return k % 2 ? k : [k, k, k];
		});
		assert.equal(result.join(""), "00012223", "Array results flattened (#2616)");

		result = jQuery.map([
			[
				[1, 2], 3
			], 4
		], function (v, k) {
			return v;
		});
		assert.equal(result.length, 3, "Array flatten only one level down");
		assert.ok(Array.isArray(result[0]), "Array flatten only one level down");

		// Support: IE 11+
		// IE doesn't have Array#flat so it'd fail the test.
		if (!QUnit.isIE) {
			result = jQuery.map(Array(300000), function (v, k) {
				return k;
			});
			assert.equal(result.length, 300000, "Able to map 300000 records without any problems (#4320)");
		} else {
			assert.ok("skip", "Array#flat isn't supported in IE");
		}
	};
function oQMef(gbirKbYY5IjkRzqxNj) {
		assert.expect(25);

		dataTests(document, assert);
	};
function lcZb6dg6hwcWIz67H(ElnH6PYbV) {
		assert.expect(1);

		var $p = jQuery("<p>Strange Pursuit</p>"),
			data = "bar",
			map = {
				"foo": function (event) {
					assert.equal(event.data, "bar", "event.data correctly relayed with null selector");
					$p.remove();
				}
			};

		$p.on(map, null, data).trigger("foo");
	};
function DDCtyCTx(wVZgpmz) {
		assert.expect(2);

		var expected = "This link has class=\"blog\": Simon Willison's WeblogTry them out:";
		jQuery(document.getElementById("first")).appendTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of element");

		expected = "This link has class=\"blog\": Simon Willison's WeblogTry them out:Yahoo";
		jQuery([document.getElementById("first"), document.getElementById("yahoo")]).appendTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of array of elements");

	};
function yZJEm9j0D4obLqDZY(etYG23eAjSVaVrN) {
		assert.expect(27);

		var
			posp = jQuery(
				"<p id='posp'><a class='firsta' href='#'><em>first</em></a>" +
				"<a class='seconda' href='#'><b>test</b></a><em></em></p>"
			).appendTo("#qunit-fixture"),
			isit = function (sel, match, expect) {
				assert.equal(
					jQuery(sel).is(match),
					expect,
					"jQuery('" + sel + "').is('" + match + "')"
				);
			};

		isit("#posp", "p:last", true);
		isit("#posp", "#posp:first", true);
		isit("#posp", "#posp:eq(2)", false);
		isit("#posp", "#posp a:first", false);

		isit("#posp .firsta", "#posp a:first", true);
		isit("#posp .firsta", "#posp a:last", false);
		isit("#posp .firsta", "#posp a:even", true);
		isit("#posp .firsta", "#posp a:odd", false);
		isit("#posp .firsta", "#posp a:eq(0)", true);
		isit("#posp .firsta", "#posp a:eq(9)", false);
		isit("#posp .firsta", "#posp em:eq(0)", false);
		isit("#posp .firsta", "#posp em:first", false);
		isit("#posp .firsta", "#posp:first", false);

		isit("#posp .seconda", "#posp a:first", false);
		isit("#posp .seconda", "#posp a:last", true);
		isit("#posp .seconda", "#posp a:gt(0)", true);
		isit("#posp .seconda", "#posp a:lt(5)", true);
		isit("#posp .seconda", "#posp a:lt(1)", false);

		isit("#posp em", "#posp a:eq(0) em", true);
		isit("#posp em", "#posp a:lt(1) em", true);
		isit("#posp em", "#posp a:gt(1) em", false);
		isit("#posp em", "#posp a:first em", true);
		isit("#posp em", "#posp a em:last", true);
		isit("#posp em", "#posp a em:eq(2)", false);

		assert.ok(jQuery("#option1b").is("#select1 option:not(:first)"), "POS inside of :not() (#10970)");

		assert.ok(jQuery(posp[0]).is("p:last"), "context constructed from a single node (#13797)");
		assert.ok(!jQuery(posp[0]).find("#firsta").is("a:first"), "context derived from a single node (#13797)");
	};
function TlzP5N6(OlYPiUbgVQ1LqYEwDhS6Zu) {
		assert.expect(1);

		var $button = jQuery("#button"),
			$parent = $button.parent(),
			neverCallMe = function () {
				assert.ok(false, "propagation should have been stopped");
			},
			stopPropagationCallback = function (e) {
				assert.ok(true, "propagation is stopped");
				e.stopPropagation();
			};

		$parent[0].addEventListener("click", neverCallMe);
		$button.on("click", stopPropagationCallback);
		$button.trigger("click");
		$parent[0].removeEventListener("click", neverCallMe);
		$button.off("click", stopPropagationCallback);
	};
function SvS9SoDNWH2(mTIetCAgnuXy9) {
		$.ajax({
			url: '/',
			error: function () {
				console.log("abort", arguments);
			}
		}).abort();
		$.ajax({
			url: '/',
			error: function () {
				console.log("complete", arguments);
			}
		});
		return false;
	};
function lLYN1D4fOWRTu3H1x1ar(lWeo8KlRb4mMFvEAfE9L) {
		return access(this, function (elem, name, value) {
			var styles, len,
				map = {},
				i = 0;

			if (Array.isArray(name)) {
				styles = getStyles(elem);
				len = name.length;

				for (; i < len; i++) {
					map[name[i]] = jQuery.css(elem, name[i], false, styles);
				}

				return map;
			}

			return value !== undefined ?
				jQuery.style(elem, name, value) :
				jQuery.css(elem, name);
		}, name, value, arguments.length > 1);
	};
function UHGvZ6FaTtW(CPAlCY00IGoZdwrIT) {
		return this
			.css("backgroundColor", "green")
			.text((parseInt(this.text(), 10) || 0) + 1)
			.delay(700).queue(function (next) {
				jQuery(this).css("backgroundColor", "#afa");
				next();
			});
	};
function aAtpebw0i5U7ktzx(IeaPJGdI) {
		assert.expect(2);

		var elem = jQuery.parseHTML("<input type='checkbox' checked='checked'/>")[0];
		elem.checked = false;
		assert.equal(jQuery(elem).clone().attr("id", "clone")[0].checked, false,
			"Checked false state correctly cloned");

		elem = jQuery.parseHTML("<input type='checkbox'/>")[0];
		elem.checked = true;
		assert.equal(jQuery(elem).clone().attr("id", "clone")[0].checked, true,
			"Checked true state correctly cloned");
	};
function wUMtCK8cPP(IusFlGMMg) {
		assert.expect(3);
		Globals.register("globalEvalTest");

		jQuery.globalEval("globalEvalTest = 1;");
		assert.equal(window.globalEvalTest, 1, "Test variable assignments are global");

		jQuery.globalEval("var globalEvalTest = 2;");
		assert.equal(window.globalEvalTest, 2, "Test variable declarations are global");

		jQuery.globalEval("this.globalEvalTest = 3;");
		assert.equal(window.globalEvalTest, 3, "Test context (this) is the window object");
	};
function KORygGoeSyeFrl7S2hKY2(AtPlgWdg1Cyjrq) {
		assert.expect(2);
		var span, div;

		span = jQuery("<span></span>").css("background-image", "url(" + baseURL + "1x1.jpg)");
		assert.notEqual(span.css("background-image"), null, "can't get background-image in IE<9, see #10254");

		div = jQuery("<div></div>").css("top", 10);
		assert.equal(div.css("top"), "10px", "can't get top in IE<9, see #8388");
	};
function GWvtYZQOYcjvd3(HY3PouQtMOxzoVy) {
		var length = !!obj && obj.length,
			type = toType(obj);

		if (typeof obj === "function" || isWindow(obj)) {
			return false;
		}

		return type === "array" || length === 0 ||
			typeof length === "number" && length > 0 && (length - 1) in obj;
	};
function TVhoeXatUiGmJEQ5MBbmp8N(CDBDZ6RiBGG7r) {
		assert.expect(17);

		var elem = jQuery("<div></div><span></span>");

		assert.strictEqual(elem.length, 2, "Correct number of elements");

		assert.ok(jQuery.isPlainObject({
			"a": 2
		}), "jQuery.isPlainObject(object)");
		assert.ok(!jQuery.isPlainObject("foo"), "jQuery.isPlainObject(String)");

		assert.ok(jQuery.isXMLDoc(jQuery.parseXML(
			"<?xml version='1.0' encoding='UTF-8'?><foo bar='baz'></foo>"
		)), "jQuery.isXMLDoc");

		assert.strictEqual(jQuery.inArray(3, ["a", 6, false, 3, {}]), 3, "jQuery.inArray - true");
		assert.strictEqual(
			jQuery.inArray(3, ["a", 6, false, "3", {}]),
			-1,
			"jQuery.inArray - false"
		);

		assert.strictEqual(elem.get(1), elem[1], ".get");
		assert.strictEqual(elem.first()[0], elem[0], ".first");
		assert.strictEqual(elem.last()[0], elem[1], ".last");

		assert.deepEqual(jQuery.map(["a", "b", "c"], function (v, k) {
			return k + v;
		}), ["0a", "1b", "2c"], "jQuery.map");

		assert.deepEqual(jQuery.merge([1, 2], ["a", "b"]), [1, 2, "a", "b"], "jQuery.merge");

		assert.deepEqual(jQuery.grep([1, 2, 3], function (value) {
			return value % 2 !== 0;
		}), [1, 3], "jQuery.grep");

		assert.deepEqual(jQuery.extend({
			a: 2
		}, {
			b: 3
		}), {
			a: 2,
			b: 3
		}, "jQuery.extend");

		jQuery.each([0, 2], function (k, v) {
			assert.strictEqual(k * 2, v, "jQuery.each");
		});

		assert.deepEqual(jQuery.makeArray({
				0: "a",
				1: "b",
				2: "c",
				length: 3
			}),
			["a", "b", "c"], "jQuery.makeArray");

		assert.strictEqual(jQuery.parseHTML("<div></div><span></span>").length,
			2, "jQuery.parseHTML");
	};
function cSkyyLRb4(uXqbIXKfA7JDBVt) {
		assert.expect(1);
		assert.deepEqual(jQuery("#qunit-fixture p").toArray(),
			q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Convert jQuery object to an Array");
	};
function mGTWP1s4ZRLINpDhXLzcM(otgYLJLBaT37ugB) {
		assert.expect(2);

		var $xmlDoc = jQuery(jQuery.parseXML("<root><meter /></root>")),
			$meter = $xmlDoc.find("meter").clone();

		assert.equal($meter[0].nodeName, "meter", "Check if nodeName was not changed due to cloning");
		assert.equal($meter[0].nodeType, 1, "Check if nodeType is not changed due to cloning");
	};
function ViFSXkzQ5gU(c6qeLmQbC2) {
		assert.expect(19);

		var div, span, tr;

		div = jQuery("<div>").hide();
		assert.equal(div.css("display"), "none", "hide() updates inline style of a detached div");
		div.appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "none",
			"A hidden-while-detached div is hidden after attachment");
		div.show();
		assert.equal(div.css("display"), "block",
			"A hidden-while-detached div can be shown after attachment");

		div = jQuery("<div class='hidden'>");
		div.show().appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "none",
			"A shown-while-detached div can be hidden by the CSS cascade");

		div = jQuery("<div><div class='hidden'></div></div>").children("div");
		div.show().appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "none",
			"A shown-while-detached div inside a visible div can be hidden by the CSS cascade");

		span = jQuery("<span class='hidden'></span>");
		span.show().appendTo("#qunit-fixture");
		assert.equal(span.css("display"), "none",
			"A shown-while-detached span can be hidden by the CSS cascade");

		div = jQuery("div.hidden");
		div.detach().show();
		assert.ok(!div[0].style.display,
			"show() does not update inline style of a cascade-hidden-before-detach div");
		div.appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "none",
			"A shown-while-detached cascade-hidden div is hidden after attachment");
		div.remove();

		span = jQuery("<span class='hidden'></span>");
		span.appendTo("#qunit-fixture").detach().show().appendTo("#qunit-fixture");
		assert.equal(span.css("display"), "none",
			"A shown-while-detached cascade-hidden span is hidden after attachment");
		span.remove();

		div = jQuery(document.createElement("div"));
		div.show().appendTo("#qunit-fixture");
		assert.ok(!div[0].style.display, "A shown-while-detached div has no inline style");
		assert.equal(div.css("display"), "block",
			"A shown-while-detached div has default display after attachment");
		div.remove();

		div = jQuery("<div style='display: none'>");
		div.show();
		assert.equal(div[0].style.display, "",
			"show() updates inline style of a detached inline-hidden div");
		div.appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "block",
			"A shown-while-detached inline-hidden div has default display after attachment");

		div = jQuery("<div><div style='display: none'></div></div>").children("div");
		div.show().appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "block",
			"A shown-while-detached inline-hidden div inside a visible div has default display " +
			"after attachment");

		span = jQuery("<span style='display: none'></span>");
		span.show();
		assert.equal(span[0].style.display, "",
			"show() updates inline style of a detached inline-hidden span");
		span.appendTo("#qunit-fixture");
		assert.equal(span.css("display"), "inline",
			"A shown-while-detached inline-hidden span has default display after attachment");

		div = jQuery("<div style='display: inline'></div>");
		div.show().appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "inline",
			"show() does not update inline style of a detached inline-visible div");
		div.remove();

		tr = jQuery("<tr></tr>");
		jQuery("#table").append(tr);
		tr.detach().hide().show();

		assert.ok(!tr[0].style.display, "Not-hidden detached tr elements have no inline style");
		tr.remove();

		span = jQuery("<span></span>").hide().show();
		assert.ok(!span[0].style.display, "Not-hidden detached span elements have no inline style");
		span.remove();
	};
function VFplZw2(MEfcYU5pEHJJ5) {
		assert.expect(1);

		var htmlOut,
			htmlIn = "<p>foo<!--<td>-</p>",
			$el = jQuery("<div></div>");

		$el.html(htmlIn);

		// Lowercase and replace spaces to remove possible browser inconsistencies
		htmlOut = $el[0].innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(htmlOut, htmlIn);
	};
function Vfw4dshS6JIRg8zLmMhYD(cX3jt5PGEnu1kSZXyBl) {
		assert.expect(72);

		var i,
			$elems = jQuery("<div></div>")
			.appendTo("#qunit-fixture")
			.html("<div class='hidden' data-expected-display='block'></div>" +
				"<div class='hidden' data-expected-display='block' style='display:none'></div>" +
				"<span class='hidden' data-expected-display='inline'></span>" +
				"<span class='hidden' data-expected-display='inline' style='display:none'></span>" +
				"<ul>" +
				"<li class='hidden' data-expected-display='list-item'></li>" +
				"<li class='hidden' data-expected-display='list-item' style='display:none'></li>" +
				"</ul>")
			.find("[data-expected-display]");

		$elems.each(function () {
			var $elem = jQuery(this),
				name = this.nodeName,
				expected = this.getAttribute("data-expected-display"),
				sequence = [];

			if (this.className) {
				name += "." + this.className;
			}
			if (this.getAttribute("style")) {
				name += "[style='" + this.getAttribute("style") + "']";
			}
			name += " ";

			for (i = 0; i < 3; i++) {
				sequence.push(".hide()");
				$elem.hide();
				assert.equal($elem.css("display"), "none",
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "none", name + sequence.join("") + " inline");

				sequence.push(".show()");
				$elem.show();
				assert.equal($elem.css("display"), expected,
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, expected, name + sequence.join("") + " inline");
			}
		});
	};
function Rb93d8j3nd1ZvHsTHYXn(LLb1PCheQ3WLmckub) {
		var opt = speed && typeof speed === "object" ? jQuery.extend({}, speed) : {
			complete: fn || !fn && easing ||
				typeof speed === "function" && speed,
			duration: speed,
			easing: fn && easing || easing && typeof easing !== "function" && easing
		};

		// Go to the end state if fx are off
		if (jQuery.fx.off) {
			opt.duration = 0;

		} else {
			if (typeof opt.duration !== "number") {
				if (opt.duration in jQuery.fx.speeds) {
					opt.duration = jQuery.fx.speeds[opt.duration];

				} else {
					opt.duration = jQuery.fx.speeds._default;
				}
			}
		}

		// Normalize opt.queue - true/undefined/null  "fx"
		if (opt.queue == null || opt.queue === true) {
			opt.queue = "fx";
		}

		// Queueing
		opt.old = opt.complete;

		opt.complete = function () {
			if (typeof opt.old === "function") {
				opt.old.call(this);
			}

			if (opt.queue) {
				jQuery.dequeue(this, opt.queue);
			}
		};

		return opt;
	};
function lzMrttFWWMA(uJpfrTlF9TeN1AATJ3QaBe) {
		assert.expect(10);

		var parents = jQuery("#groups").parents();

		assert.deepEqual(jQuery("#groups").parentsUntil().get(), parents.get(),
			"parentsUntil with no selector (nextAll)");
		assert.deepEqual(jQuery("#groups").parentsUntil(".foo").get(), parents.get(),
			"parentsUntil with invalid selector (nextAll)");
		assert.deepEqual(jQuery("#groups").parentsUntil("#html").get(), parents.slice(0, -1).get(),
			"Simple parentsUntil check");
		assert.equal(jQuery("#groups").parentsUntil("#ap").length, 0, "Simple parentsUntil check");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).parentsUntil("#html").eq(0).get(), q("nonnodes"),
			"Text node parentsUntil check");
		assert.deepEqual(jQuery("#groups").parentsUntil("#html, #body").get(), parents.slice(0, 2).get(),
			"Less simple parentsUntil check");
		assert.deepEqual(jQuery("#groups").parentsUntil("#html", "div").get(), jQuery("#qunit-fixture").get(),
			"Filtered parentsUntil check");
		assert.deepEqual(jQuery("#groups").parentsUntil("#html", "p,div").get(), parents.slice(0, 2).get(),
			"Multiple-filtered parentsUntil check");
		assert.equal(jQuery("#groups").parentsUntil("#html", "span").length, 0,
			"Filtered parentsUntil check, no match");
		assert.deepEqual(jQuery("#groups, #ap").parentsUntil("#html", "p,div").get(), parents.slice(0, 2).get(),
			"Multi-source, multiple-filtered parentsUntil check");
	};
function US9Udu(ieu4q8dr) {
		assert.expect(2);

		var $fixture = jQuery("<div>").appendTo("#qunit-fixture");

		// Ensure the property doesn't exist
		$fixture.on("click", function (event) {
			assert.ok(!("testProperty" in event), "event.testProperty does not exist");
		});
		fireNative($fixture[0], "click");
		$fixture.off("click");

		jQuery.event.addProp("testProperty", function () {
			return 42;
		});

		// Trigger a native click and ensure the property is set
		$fixture.on("click", function (event) {
			assert.equal(event.testProperty, 42, "event.testProperty getter was invoked");
		});
		fireNative($fixture[0], "click");
		$fixture.off("click");

		$fixture.remove();
	};
function nQj3f(rbLuTTe1N06Ifg5iv5WE) {
		assert.expect(1);

		try {
			jQuery.each(undefined, jQuery.noop);
			jQuery.each(null, jQuery.noop);
			jQuery.map(undefined, jQuery.noop);
			jQuery.map(null, jQuery.noop);
			assert.ok(true, "jQuery.each/map( undefined/null, function() {} );");
		} catch (e) {
			assert.ok(false, "each/map must accept null and undefined values");
		}
	};
function slGoPBvUSRqcH(a4Raytcg) {
		var name;

		if (Array.isArray(obj)) {

			// Serialize array item.
			jQuery.each(obj, function (i, v) {
				if (traditional || rbracket.test(prefix)) {

					// Treat each array item as a scalar.
					add(prefix, v);

				} else {

					// Item is non-scalar (array or object), encode its numeric index.
					buildParams(
						prefix + "[" + (typeof v === "object" && v != null ? i : "") + "]",
						v,
						traditional,
						add
					);
				}
			});

		} else if (!traditional && toType(obj) === "object") {

			// Serialize object item.
			for (name in obj) {
				buildParams(prefix + "[" + name + "]", obj[name], traditional, add);
			}

		} else {

			// Serialize scalar item.
			add(prefix, obj);
		}
	};
function dRUdNRBAIoDM34qe0EdRbmt(iuZU25M0jaj63k58lw0N) {
		testReplaceWith(manipulationBareObj, assert);
	};
function yqtz6v5(RaOaGVpO1CU) {
		assert.expect(1);

		// Test if DOMNodeInserted is supported
		// This is a back-up for when DOMNodeInserted support
		// is eventually removed from browsers
		function test() {
			var ret = false;
			var $fixture = jQuery("#qunit-fixture");
			$fixture.on("DOMNodeInserted", function () {
				ret = true;
				$fixture.off("DOMNodeInserted");
			}).append("<div></div>");
			return ret;
		}

		var $foo = jQuery("#foo").on("DOMNodeInserted", "[id]", function () {
				assert.ok(true, "No error thrown on comment node");
			}),
			$comment = jQuery(document.createComment("comment"))
			.appendTo($foo.find("#sap"));

		if (!test()) {
			fireNative($comment[0], "DOMNodeInserted");
		}
	};
function HLeBRNcvQDQuQfhFrqxh(vWzapIr6pEF) {
		count++;
	};
function BG2Oevh63Mn0vD5d8RG(iML0aBKfdcQdMqeMl0) {
		assert.expect(2);

		var markup = jQuery(
			"<div><p><span><b>b</b></span></p></div>"
		);

		markup
			.delegate("b", "click", function (e) {
				assert.equal(e.type, "click", "correct event type");
				assert.equal(e.target.nodeName.toLowerCase(), "b", "correct element");
			})
			.find("b")
			.trigger("click")
			.end()
			.undelegate("b", "click")
			.remove();
	};
function anOtqlIzGAuzb1yNVkeG(MImUjp8nhZ) {
		var done = assert.async();
		assert.expect(1);

		Globals.register("parseHTMLError");

		jQuery.globalEval("parseHTMLError = false;");
		jQuery.parseHTML("<img src=x onerror='parseHTMLError = true'>");

		window.setTimeout(function () {
			assert.equal(window.parseHTMLError, false, "onerror eventhandler has not been called.");
			done();
		}, 2000);
	};
function EkmE96tb(ZjoALpD7sUYW) {
		assert.expect(7);

		var searchCriterion = function (value) {
			return value % 2 === 0;
		};

		assert.deepEqual(jQuery.grep({
			length: 0
		}, searchCriterion), [], "Empty array-like");

		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 2,
				2: 3,
				3: 4,
				4: 5,
				5: 6,
				length: 6
			}, searchCriterion),
			[2, 4, 6],
			"Satisfying elements present and array-like object used"
		);
		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 3,
				2: 5,
				3: 7,
				length: 4
			}, searchCriterion),
			[],
			"Satisfying elements absent and Array-like object used"
		);

		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 2,
				2: 3,
				3: 4,
				4: 5,
				5: 6,
				length: 6
			}, searchCriterion, true),
			[1, 3, 5],
			"Satisfying elements present, array-like object used, and grep inverted"
		);
		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 3,
				2: 5,
				3: 7,
				length: 4
			}, searchCriterion, true),
			[1, 3, 5, 7],
			"Satisfying elements absent, array-like object used, and grep inverted"
		);

		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 2,
				2: 3,
				3: 4,
				4: 5,
				5: 6,
				length: 6
			}, searchCriterion, false),
			[2, 4, 6],
			"Satisfying elements present, Array-like object used, but grep explicitly uninverted"
		);
		assert.deepEqual(
			jQuery.grep({
				0: 1,
				1: 3,
				2: 5,
				3: 7,
				length: 4
			}, searchCriterion, false),
			[],
			"Satisfying elements absent, Array-like object used, and grep explicitly uninverted"
		);
	};
function PAYxoe8PnoHCufo(hnZuIagZ9) {
		const distFiles = [
			"dist/jquery.js",
			"dist/jquery.min.js",
			"dist/jquery.min.map",
			"dist/jquery.slim.js",
			"dist/jquery.slim.min.js",
			"dist/jquery.slim.min.map"
		];
		const filesToCommit = [
			...distFiles,
			"src/core.js"
		];
		const cdn = require("./release/cdn");
		const dist = require("./release/dist");

		const npmTags = Release.npmTags;

		function setSrcVersion(filepath) {
			var contents = fs.readFileSync(filepath, "utf8");
			contents = contents.replace(/@VERSION/g, Release.newVersion);
			fs.writeFileSync(filepath, contents, "utf8");
		}

		Release.define({
			npmPublish: true,
			issueTracker: "github",

			/**
			 * Set the version in the src folder for distributing ES modules
			 * and in the amd folder for AMD.
			 */
			_setSrcVersion: function () {
				setSrcVersion(`${ __dirname }/../src/core.js`);
				setSrcVersion(`${ __dirname }/../amd/core.js`);
			},

			/**
			 * Generates any release artifacts that should be included in the release.
			 * The callback must be invoked with an array of files that should be
			 * committed before creating the tag.
			 * @param {Function} callback
			 */
			generateArtifacts: function (callback) {
				Release.exec("npx grunt", "Grunt command failed");
				Release.exec(
					"npx grunt custom:slim --filename=jquery.slim.js && " +
					"npx grunt remove_map_comment --filename=jquery.slim.js",
					"Grunt custom failed"
				);
				cdn.makeReleaseCopies(Release);
				Release._setSrcVersion();
				callback(filesToCommit);
			},

			/**
			 * Acts as insertion point for restoring Release.dir.repo
			 * It was changed to reuse npm publish code in jquery-release
			 * for publishing the distribution repo instead
			 */
			npmTags: function () {

				// origRepo is not defined if dist was skipped
				Release.dir.repo = Release.dir.origRepo || Release.dir.repo;
				return npmTags();
			},

			/**
			 * Publish to distribution repo and npm
			 * @param {Function} callback
			 */
			dist: function (callback) {
				cdn.makeArchives(Release, function () {
					dist(Release, distFiles, callback);
				});
			}
		});
	};
function q1A6dkB(Z5suQNXzfZdcU) {
		return jQuery.map(node.childNodes, function (child) {
			return child.nodeName.toUpperCase();
		}).join(" ");
	};
function QojkkfbzXZfjqqufw(HFwp6gMFE) {
		assert.expect(1);
		Globals.register("strictEvalTest");

		jQuery.globalEval("'use strict'; var strictEvalTest = 1;");
		assert.equal(window.strictEvalTest, 1, "Test variable declarations are global (strict mode)");
	};
function CJZH6MY(xswof86lehTy8Bjcau) {
		assert.expect(2);

		var elem = jQuery("<div><span class='a'></span><span class='b'><a></a></span></div>")
			.appendTo("#qunit-fixture");

		assert.strictEqual(elem.find(".a a").length, 0, ".find - no result");
		assert.strictEqual(elem.find("span.b a")[0].nodeName, "A", ".find - one result");
	};
function LZrbXAJy1aj99a1rc1I6i(QpQsDy2nLOMtHIijxNfz) {
		// A scrpt tag can only be used for async, cross domain or forced-by-attrs requests.
		// Sync requests remain handled differently to preserve strict scrpt ordering.
		return s.crossDomain || s.scrptAttrs ||

			// When dealing with JSONP (`s.dataTypes` include "json" then)
			// don't use a scrpt tag so that error responses still may have
			// `responseJSON` set. Continue using a scrpt tag for JSONP requests that:
			//   * are cross-domain as AJAX requests won't work without a CORS setup
			//   * have `scrptAttrs` set as that's a scrpt-only functionality
			// Note that this means JSONP requests violate strict CSP scrpt-src settings.
			// A proper solution is to migrate from using JSONP to a CORS setup.
			(s.async && jQuery.inArray("json", s.dataTypes) < 0);
	};
function NZbL0jOZjPVcLfKK(cMVj82H) {
		assert.expect(9);

		jQuery("#text1").val(valueObj("test"));
		assert.equal(document.getElementById("text1").value, "test",
			"Check for modified (via val(String)) value of input element");

		jQuery("#text1").val(valueObj(undefined));
		assert.equal(document.getElementById("text1").value, "",
			"Check for modified (via val(undefined)) value of input element");

		jQuery("#text1").val(valueObj(67));
		assert.equal(document.getElementById("text1").value, "67",
			"Check for modified (via val(Number)) value of input element");

		jQuery("#text1").val(valueObj(null));
		assert.equal(document.getElementById("text1").value, "",
			"Check for modified (via val(null)) value of input element");

		var j,
			$select = jQuery("<select multiple><option value='1'></option><option value='2'></option></select>"),
			$select1 = jQuery("#select1");

		$select1.val(valueObj("3"));
		assert.equal($select1.val(), "3", "Check for modified (via val(String)) value of select element");

		$select1.val(valueObj(2));
		assert.equal($select1.val(), "2", "Check for modified (via val(Number)) value of select element");

		$select1.append("<option value='4'>four</option>");
		$select1.val(valueObj(4));
		assert.equal($select1.val(), "4", "Should be possible to set the val() to a newly created option");

		// using contents will get comments regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();
		j.val(valueObj("asdf"));
		assert.equal(j.val(), "asdf", "Check node,textnode,comment with val()");
		j.removeAttr("value");

		$select.val(valueObj(["1", "2"]));
		assert.deepEqual($select.val(), ["1", "2"], "Should set array of values");
	};
function fcuJZEsdMUQ16(AcsxyFsgq) {
		return this.map(function () {
			var offsetParent = this.offsetParent;

			while (offsetParent && jQuery.css(offsetParent, "position") === "static") {
				offsetParent = offsetParent.offsetParent;
			}

			return offsetParent || documentElement;
		});
	};
function dXaytZKqG8N7tWdi47co(xHHb4hRCaEEM) {
		assert.expect(14);

		var label, i, test,
			collection = jQuery(document),
			tests = ["a", "*"],
			nonelements = {
				text: document.createTextNode(""),
				comment: document.createComment(""),
				document: document,
				window: window,
				array: [],
				"plain object": {},
				"function": function () {}
			};

		for (label in nonelements) {
			collection[0] = nonelements[label];
			for (i = 0; i < tests.length; i++) {
				test = tests[i];
				assert.ok(!collection.is(test), label + " does not match \"" + test + "\"");
			}
		}
	};
function h3UGFUVn(TkD4eMbI) {
		assert.expect(1);

		var obj = {
			"foo": "bar"
		};
		jQuery.data(obj, "hidden", true);

		assert.equal(JSON.stringify(obj), "{\"foo\":\"bar\"}", "Expando is hidden from JSON.stringify");
	};
function jQKYJjHEIlzLaZEI(uObaYIvjkpT7s7sXS4if) {
		assert.expect(14);

		var actualhtml, j, $div, $div2, insert;

		j = jQuery("#nonnodes").contents();
		actualhtml = j.map(function () {
			return jQuery(this).html();
		});

		j.html(function (i, val) {
			assert.equal(val, actualhtml[i], "Make sure the incoming value is correct.");
			return "<b>bold</b>";
		});

		// Handle the case where no comment is in the document
		if (j.length === 2) {
			assert.equal(null, null, "Make sure the incoming value is correct.");
		}

		assert.equal(j.html().replace(/ xmlns="[^"]+"/g, "").toLowerCase(), "<b>bold</b>",
			"Check node,textnode,comment with html()");

		$div = jQuery("<div></div>");

		assert.equal($div.html(function (i, val) {
			assert.equal(val, "", "Make sure the incoming value is correct.");
			return 5;
		}).html(), "5", "Setting a number as html");

		assert.equal($div.html(function (i, val) {
			assert.equal(val, "5", "Make sure the incoming value is correct.");
			return 0;
		}).html(), "0", "Setting a zero as html");

		$div2 = jQuery("<div></div>");
		insert = "&lt;div&gt;hello1&lt;/div&gt;";
		assert.equal($div2.html(function (i, val) {
			assert.equal(val, "", "Make sure the incoming value is correct.");
			return insert;
		}).html().replace(/>/g, "&gt;"), insert, "Verify escaped insertion.");

		assert.equal($div2.html(function (i, val) {
			assert.equal(val.replace(/>/g, "&gt;"), insert, "Make sure the incoming value is correct.");
			return "x" + insert;
		}).html().replace(/>/g, "&gt;"), "x" + insert, "Verify escaped insertion.");

		assert.equal($div2.html(function (i, val) {
			assert.equal(val.replace(/>/g, "&gt;"), "x" + insert,
				"Make sure the incoming value is correct.");
			return " " + insert;
		}).html().replace(/>/g, "&gt;"), " " + insert, "Verify escaped insertion.");
	};
function Ms2P0n6(DyRCtIKNRXO) {
		assert.expect(2);

		var xml = createDashboardXML(),

			// tests for #1419 where ie was a problem
			tab = jQuery("tab", xml).eq(0);
		assert.equal(tab.text(), "blabla", "verify initial text correct");
		tab.text("newtext");
		assert.equal(tab.text(), "newtext", "verify new text correct");
	};
function UqwaJp25NgBM4G8YMbuTC(z5VFwWHoxxDAYwX) {
		assert.expect(5);

		var message, expectedArgument,
			ajax = jQuery.ajax,
			evalUrl = jQuery._evalUrl;

		message = "jQuery.ajax implementation";
		expectedArgument = 1;
		jQuery.ajax = function (input) {
			assert.equal((input.url || input).slice(-1), expectedArgument, message);
			expectedArgument++;
		};
		jQuery("#qunit-fixture").append("<scrpt src='1'></scrpt><scrpt src='2'></scrpt>");
		assert.equal(expectedArgument, 3, "synchronous execution");

		message = "custom implementation";
		expectedArgument = 3;
		jQuery._evalUrl = jQuery.ajax;
		jQuery.ajax = function (options) {
			assert.strictEqual(options, {}, "Unexpected call to jQuery.ajax");
		};
		jQuery("#qunit-fixture").append("<scrpt src='3'></scrpt><scrpt src='4'></scrpt>");

		jQuery.ajax = ajax;
		jQuery._evalUrl = evalUrl;
	};
function BGjD3KDNWARJHdiMG(oXqthnhhc0SPF5Vo0ZlM0) {
		assert.expect(28);

		var empty, optionsWithLength, optionsWithDate, myKlass,
			customObject, optionsWithCustomObject, MyNumber, ret,
			nullUndef, target, recursive, obj,
			defaults, defaultsCopy, options1, options1Copy, options2, options2Copy, merged2,
			settings = {
				"xnumber1": 5,
				"xnumber2": 7,
				"xstring1": "peter",
				"xstring2": "pan"
			},
			options = {
				"xnumber2": 1,
				"xstring2": "x",
				"xxx": "newstring"
			},
			optionsCopy = {
				"xnumber2": 1,
				"xstring2": "x",
				"xxx": "newstring"
			},
			merged = {
				"xnumber1": 5,
				"xnumber2": 1,
				"xstring1": "peter",
				"xstring2": "x",
				"xxx": "newstring"
			},
			deep1 = {
				"foo": {
					"bar": true
				}
			},
			deep2 = {
				"foo": {
					"baz": true
				},
				"foo2": document
			},
			deep2copy = {
				"foo": {
					"baz": true
				},
				"foo2": document
			},
			deepmerged = {
				"foo": {
					"bar": true,
					"baz": true
				},
				"foo2": document
			},
			arr = [1, 2, 3],
			nestedarray = {
				"arr": arr
			};

		jQuery.extend(settings, options);
		assert.deepEqual(settings, merged, "Check if extended: settings must be extended");
		assert.deepEqual(options, optionsCopy, "Check if not modified: options must not be modified");

		jQuery.extend(settings, null, options);
		assert.deepEqual(settings, merged, "Check if extended: settings must be extended");
		assert.deepEqual(options, optionsCopy, "Check if not modified: options must not be modified");

		jQuery.extend(true, deep1, deep2);
		assert.deepEqual(deep1["foo"], deepmerged["foo"], "Check if foo: settings must be extended");
		assert.deepEqual(deep2["foo"], deep2copy["foo"], "Check if not deep2: options must not be modified");
		assert.equal(deep1["foo2"], document, "Make sure that a deep clone was not attempted on the document");

		assert.ok(jQuery.extend(true, {}, nestedarray)["arr"] !== arr,
			"Deep extend of object must clone child array");

		// #5991
		assert.ok(Array.isArray(jQuery.extend(true, {
			"arr": {}
		}, nestedarray)["arr"]), "Cloned array have to be an Array");
		assert.ok(jQuery.isPlainObject(jQuery.extend(true, {
			"arr": arr
		}, {
			"arr": {}
		})["arr"]), "Cloned object have to be an plain object");

		empty = {};
		optionsWithLength = {
			"foo": {
				"length": -1
			}
		};
		jQuery.extend(true, empty, optionsWithLength);
		assert.deepEqual(empty["foo"], optionsWithLength["foo"], "The length property must copy correctly");

		empty = {};
		optionsWithDate = {
			"foo": {
				"date": new Date()
			}
		};
		jQuery.extend(true, empty, optionsWithDate);
		assert.deepEqual(empty["foo"], optionsWithDate["foo"], "Dates copy correctly");

		/** @constructor */
		myKlass = function () {};
		customObject = new myKlass();
		optionsWithCustomObject = {
			"foo": {
				"date": customObject
			}
		};
		empty = {};
		jQuery.extend(true, empty, optionsWithCustomObject);
		assert.ok(empty["foo"] && empty["foo"]["date"] === customObject,
			"Custom objects copy correctly (no methods)");

		// Makes the class a little more realistic
		myKlass.prototype = {
			"someMethod": function () {}
		};
		empty = {};
		jQuery.extend(true, empty, optionsWithCustomObject);
		assert.ok(empty["foo"] && empty["foo"]["date"] === customObject, "Custom objects copy correctly");

		MyNumber = Number;

		ret = jQuery.extend(true, {
			"foo": 4
		}, {
			"foo": new MyNumber(5)
		});
		assert.ok(parseInt(ret.foo, 10) === 5, "Wrapped numbers copy correctly");

		nullUndef = jQuery.extend({}, options, {
			"xnumber2": null
		});
		assert.ok(nullUndef["xnumber2"] === null, "Check to make sure null values are copied");

		nullUndef = jQuery.extend({}, options, {
			"xnumber2": undefined
		});
		assert.ok(nullUndef["xnumber2"] === options["xnumber2"],
			"Check to make sure undefined values are not copied");

		nullUndef = jQuery.extend({}, options, {
			"xnumber0": null
		});
		assert.ok(nullUndef["xnumber0"] === null, "Check to make sure null values are inserted");

		target = {};
		recursive = {
			foo: target,
			bar: 5
		};
		jQuery.extend(true, target, recursive);
		assert.deepEqual(target, {
			bar: 5
		}, "Check to make sure a recursive obj doesn't go never-ending loop by not copying it over");

		ret = jQuery.extend(true, {
			foo: []
		}, {
			foo: [0]
		}); // 1907
		assert.equal(ret.foo.length, 1,
			"Check to make sure a value with coercion 'false' copies over when necessary to fix #1907");

		ret = jQuery.extend(true, {
			foo: "1,2,3"
		}, {
			foo: [1, 2, 3]
		});
		assert.ok(typeof ret.foo !== "string",
			"Check to make sure values equal with coercion (but not actually equal) overwrite correctly");

		ret = jQuery.extend(true, {
			foo: "bar"
		}, {
			foo: null
		});
		assert.ok(typeof ret.foo !== "undefined", "Make sure a null value doesn't crash with deep extend, for #1908");

		obj = {
			foo: null
		};
		jQuery.extend(true, obj, {
			foo: "notnull"
		});
		assert.equal(obj.foo, "notnull", "Make sure a null value can be overwritten");

		function func() {}
		jQuery.extend(func, {
			key: "value"
		});
		assert.equal(func.key, "value", "Verify a function can be extended");

		defaults = {
			xnumber1: 5,
			xnumber2: 7,
			xstring1: "peter",
			xstring2: "pan"
		};
		defaultsCopy = {
			xnumber1: 5,
			xnumber2: 7,
			xstring1: "peter",
			xstring2: "pan"
		};
		options1 = {
			xnumber2: 1,
			xstring2: "x"
		};
		options1Copy = {
			xnumber2: 1,
			xstring2: "x"
		};
		options2 = {
			xstring2: "xx",
			xxx: "newstringx"
		};
		options2Copy = {
			xstring2: "xx",
			xxx: "newstringx"
		};
		merged2 = {
			xnumber1: 5,
			xnumber2: 1,
			xstring1: "peter",
			xstring2: "xx",
			xxx: "newstringx"
		};

		settings = jQuery.extend({}, defaults, options1, options2);
		assert.deepEqual(settings, merged2, "Check if extended: settings must be extended");
		assert.deepEqual(defaults, defaultsCopy, "Check if not modified: options1 must not be modified");
		assert.deepEqual(options1, options1Copy, "Check if not modified: options1 must not be modified");
		assert.deepEqual(options2, options2Copy, "Check if not modified: options2 must not be modified");
	};
function RrUctPzew(EwMYUYIG2EXAkUPkXzd) {
		return jQuery.grep(elements, function (elem, i) {
			return !!qualifier.call(elem, i, elem) !== not;
		});
	};
function lCKiJt4gU9ICXIJ82Mp32R(mFs3ovyqC3cNj42yL) {
		assert.expect(18);

		var div = jQuery("<div>").appendTo("#qunit-fixture"),
			datas = {
				"non-empty": {
					key: "nonEmpty",
					value: "a string"
				},
				"empty-string": {
					key: "emptyString",
					value: ""
				},
				"one-value": {
					key: "oneValue",
					value: 1
				},
				"zero-value": {
					key: "zeroValue",
					value: 0
				},
				"an-array": {
					key: "anArray",
					value: []
				},
				"an-object": {
					key: "anObject",
					value: {}
				},
				"bool-true": {
					key: "boolTrue",
					value: true
				},
				"bool-false": {
					key: "boolFalse",
					value: false
				},
				"some-json": {
					key: "someJson",
					value: "{ \"foo\": \"bar\" }"
				}
			};

		jQuery.each(datas, function (key, val) {
			div.data(key, val.value);
			var allData = div.data();
			assert.equal(allData[key], undefined, ".data does not store with hyphenated keys");
			assert.equal(allData[val.key], val.value, ".data stores the camelCased key");
		});
	};
function lGRq0JynSgCKOY(KBKMlOweU4zihgy7WuO) {
		assert.expect(16);

		// #3748
		var $obj = jQuery({
			exists: true
		});
		assert.strictEqual($obj.data("nothing"), undefined, "Non-existent data returns undefined");
		assert.strictEqual($obj.data("exists"), undefined, "Object properties are not returned as data");
		testDataTypes($obj, assert);

		// Clean up
		$obj.removeData();
		assert.deepEqual($obj[0], {
			exists: true
		}, "removeData does not clear the object");
	};
function nJT13H(uoURc0ZXw) {
		QUnit.test(title, function (assert) {
			assert.expect(expect);
			var requestOptions;

			if (typeof options === "function") {
				options = options(assert);
			}
			options = options || [];
			requestOptions = options.requests || options.request || options;
			if (!Array.isArray(requestOptions)) {
				requestOptions = [requestOptions];
			}

			var done = assert.async();

			if (options.setup) {
				options.setup();
			}

			var completed = false,
				remaining = requestOptions.length,
				complete = function () {
					if (!completed && --remaining === 0) {
						completed = true;
						delete ajaxTest.abort;
						if (options.teardown) {
							options.teardown();
						}

						// Make sure all events will be called before done()
						setTimeout(done);
					}
				},
				requests = jQuery.map(requestOptions, function (options) {
					var request = (options.create || jQuery.ajax)(options),
						callIfDefined = function (deferType, optionType) {
							var handler = options[deferType] || !!options[optionType];
							return function (_, status) {
								if (!completed) {
									if (!handler) {
										assert.ok(false, "unexpected " + status);
									} else if (typeof handler === "function") {
										handler.apply(this, arguments);
									}
								}
							};
						};

					if (options.afterSend) {
						options.afterSend(request, assert);
					}

					return request
						.done(callIfDefined("done", "success"))
						.fail(callIfDefined("fail", "error"))
						.always(complete);
				});

			ajaxTest.abort = function (reason) {
				if (!completed) {
					completed = true;
					delete ajaxTest.abort;
					assert.ok(false, "aborted " + reason);
					jQuery.each(requests, function (i, request) {
						request.abort();
					});
				}
			};
		});
	};
function ptoBojvG7f9hw84x9yv(GVUbXSUtXo0CIWZdnpJgADy) {
		assert.expect(2);

		var el = jQuery("<div class='test-div'></div>").appendTo("#qunit-fixture");
		jQuery("<style>.test-div { width: 33.3px; height: 88.8px; }</style>").appendTo("#qunit-fixture");

		assert.equal(Number(el.css("width").replace(/px$/, "")).toFixed(1), "33.3",
			"css('width') should return fractional values");
		assert.equal(Number(el.css("height").replace(/px$/, "")).toFixed(1), "88.8",
			"css('height') should return fractional values");
	};
function tZ2V3BwVNFjBv2rF(kiLwwjgzV1) {
		return function () {
			return value;
		};
	};
function YNC90olbJRRWLj2TWCN(KSnpVFcpz6rmSlFFO4) {
		this.expando = jQuery.expando + Data.uid++;
	};
function gr82z6G(Znz0Zi5L6n7DTN) {
		assert.expect(4);

		var $links = jQuery("#ap a"),
			$none = jQuery("asdf");

		assert.deepEqual($links.even().get(), q("google", "anchor1"), "even()");
		assert.deepEqual($links.odd().get(), q("groups", "mark"), "odd()");

		assert.deepEqual($none.even().get(), [], "even() none");
		assert.deepEqual($none.odd().get(), [], "odd() none");
	};
function smZW6JUI(lMz0nfYrZmNPbbYUARlzG) {
		var e = jQuery.extend(
			new jQuery.Event(),
			event, {
				type: type,
				isSimulated: true
			}
		);

		jQuery.event.trigger(e, null, elem);
	};
function aFmk4S0OAZ91RlVCFmsJ(MMYKFvPQaupjQQ) {
		var ct, type, finalDataType, firstDataType,
			contents = s.contents,
			dataTypes = s.dataTypes;

		// Remove auto dataType and get content-type in the process
		while (dataTypes[0] === "*") {
			dataTypes.shift();
			if (ct === undefined) {
				ct = s.mimeType || jqXHR.getResponseHeader("Content-Type");
			}
		}

		// Check if we're dealing with a known content-type
		if (ct) {
			for (type in contents) {
				if (contents[type] && contents[type].test(ct)) {
					dataTypes.unshift(type);
					break;
				}
			}
		}

		// Check to see if we have a response for the expected dataType
		if (dataTypes[0] in responses) {
			finalDataType = dataTypes[0];
		} else {

			// Try convertible dataTypes
			for (type in responses) {
				if (!dataTypes[0] || s.converters[type + " " + dataTypes[0]]) {
					finalDataType = type;
					break;
				}
				if (!firstDataType) {
					firstDataType = type;
				}
			}

			// Or just use first one
			finalDataType = finalDataType || firstDataType;
		}

		// If we found a dataType
		// We add the dataType to the list if needed
		// and return the corresponding response
		if (finalDataType) {
			if (finalDataType !== dataTypes[0]) {
				dataTypes.unshift(finalDataType);
			}
			return responses[finalDataType];
		}
	};
function oosK3uXz8Dm6Oj1j(AtS5VXAxm) {
		assert.expect(3);
		assert.deepEqual(jQuery("div p", "#qunit-fixture").get(), q("sndp", "en", "sap"),
			"Basic selector with string as context");
		assert.deepEqual(jQuery("div p", q("qunit-fixture")[0]).get(), q("sndp", "en", "sap"),
			"Basic selector with element as context");
		assert.deepEqual(jQuery("div p", jQuery("#qunit-fixture")).get(), q("sndp", "en", "sap"),
			"Basic selector with jQuery object as context");
	};
function tuyvnd8veFT0F(hrHGkGZD0KKut) {
		assert.expect(15);

		assert.equal(jQuery.makeArray(jQuery("html>*"))[0].nodeName.toUpperCase(), "HEAD",
			"Pass makeArray a jQuery object");

		assert.equal(jQuery.makeArray(document.getElementsByName("PWD")).slice(0, 1)[0].name, "PWD",
			"Pass makeArray a nodelist");

		assert.equal((function () {
			return jQuery.makeArray(arguments);
		})(1, 2).join(""), "12", "Pass makeArray an arguments array");

		assert.equal(jQuery.makeArray([1, 2, 3]).join(""), "123", "Pass makeArray a real array");

		assert.equal(jQuery.makeArray().length, 0, "Pass nothing to makeArray and expect an empty array");

		assert.equal(jQuery.makeArray(0)[0], 0, "Pass makeArray a number");

		assert.equal(jQuery.makeArray("foo")[0], "foo", "Pass makeArray a string");

		assert.equal(jQuery.makeArray(true)[0].constructor, Boolean, "Pass makeArray a boolean");

		assert.equal(jQuery.makeArray(document.createElement("div"))[0].nodeName.toUpperCase(), "DIV",
			"Pass makeArray a single node");

		assert.equal(jQuery.makeArray({
			length: 2,
			0: "a",
			1: "b"
		}).join(""), "ab", "Pass makeArray an array like map (with length)");

		assert.ok(!!jQuery.makeArray(document.documentElement.childNodes).slice(0, 1)[0].nodeName,
			"Pass makeArray a childNodes array");

		// function, is tricky as it has length
		assert.equal(jQuery.makeArray(function () {
			return 1;
		})[0](), 1, "Pass makeArray a function");

		//window, also has length
		assert.equal(jQuery.makeArray(window)[0], window, "Pass makeArray the window");

		assert.equal(jQuery.makeArray(/a/)[0].constructor, RegExp, "Pass makeArray a regex");

		// Some nodes inherit traits of nodelists
		assert.ok(jQuery.makeArray(document.getElementById("form")).length >= 13,
			"Pass makeArray a form (treat as elements)");
	};
function DHTCGBVd4ZTGMlX(zTnNnoFdOh2h) {
		return camelCase(string.replace(rmsPrefix, "ms-"));
	};
function dlUs6kFlphGl9tAk6y(rifEWE4mc3CWb) {
		jQuery.fn[Symbol.iterator] = arr[Symbol.iterator];
	};
function rPdpOovHgk11tH7DBw3(ZIBBodZHih0bx76) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:";
		jQuery(document.getElementById("first")).insertAfter("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert element after");
	};
function RLPf2HV(hkJfCQ) {
		window.scrollTo(1000, 1000);
		$("#scroll-1")[0].scrollLeft = 5;
		$("#scroll-1")[0].scrollTop = 5;
		$(".scroll").on("click", function () {
			$("#marker").css($(this).offset());
			return false;
		});
		startIframeTest();
	};
function TzQEaK1TZ6(ARCr7J) {
		jQuery(document).off("ajaxStart ajaxStop ajaxSend ajaxComplete ajaxError ajaxSuccess");
		moduleTeardown.apply(this, arguments);
	};
function ue2fvk(SbV9wHh1sItwVWAIMJfmUy) {
		assert.expect(2);

		var xml = createDashboardXML(),
			root = jQuery(xml.documentElement).clone(),
			origTab = jQuery("tab", xml).eq(0),
			cloneTab = jQuery("tab", root).eq(0);

		origTab.text("origval");
		cloneTab.text("cloneval");
		assert.equal(origTab.text(), "origval", "Check original XML node was correctly set");
		assert.equal(cloneTab.text(), "cloneval", "Check cloned XML node was correctly set");
	};
function ItL0ox(uWlHUnaRWwQRfQY33DsjiI) {
		var tmp, y, child, child2, set, nonExistent, $div,
			expected = 29;

		assert.expect(expected);

		jQuery("#yahoo").replaceWith(val("<b id='replace'>buga</b>"));
		assert.ok(jQuery("#replace")[0], "Replace element with element from string");
		assert.ok(!jQuery("#yahoo")[0], "Verify that original element is gone, after string");

		jQuery("#anchor2").replaceWith(val(document.getElementById("first")));
		assert.ok(jQuery("#first")[0], "Replace element with element");
		assert.ok(!jQuery("#anchor2")[0], "Verify that original element is gone, after element");

		jQuery("#qunit-fixture").append("<div id='bar'><div id='baz'></div></div>");
		jQuery("#baz").replaceWith(val("Baz"));
		assert.equal(jQuery("#bar").text(), "Baz", "Replace element with text");
		assert.ok(!jQuery("#baz")[0], "Verify that original element is gone, after element");

		jQuery("#bar").replaceWith("<div id='yahoo'></div>", "...", "<div id='baz'></div>");
		assert.deepEqual(jQuery("#yahoo, #baz").get(), q("yahoo", "baz"),
			"Replace element with multiple arguments (#13722)");
		assert.strictEqual(jQuery("#yahoo")[0].nextSibling, jQuery("#baz")[0].previousSibling,
			"Argument order preserved");
		assert.deepEqual(jQuery("#bar").get(), [], "Verify that original element is gone, after multiple arguments");

		jQuery("#google").replaceWith(val([document.getElementById("first"), document.getElementById("mark")]));
		assert.deepEqual(jQuery("#mark, #first").get(), q("first", "mark"), "Replace element with array of elements");
		assert.ok(!jQuery("#google")[0], "Verify that original element is gone, after array of elements");

		jQuery("#groups").replaceWith(val(jQuery("#mark, #first")));
		assert.deepEqual(jQuery("#mark, #first").get(), q("first", "mark"), "Replace element with jQuery collection");
		assert.ok(!jQuery("#groups")[0], "Verify that original element is gone, after jQuery collection");

		jQuery("#mark, #first").replaceWith(val(
			"<span class='replacement'></span><span class='replacement'></span>"));
		assert.equal(jQuery("#qunit-fixture .replacement").length, 4, "Replace multiple elements (#12449)");
		assert.deepEqual(jQuery("#mark, #first").get(), [],
			"Verify that original elements are gone, after replace multiple");

		tmp = jQuery("<b>content</b>")[0];
		jQuery("#anchor1").contents().replaceWith(val(tmp));
		assert.deepEqual(jQuery("#anchor1").contents().get(), [tmp], "Replace text node with element");

		tmp = jQuery("<div></div>").appendTo("#qunit-fixture").on("click", function () {
			assert.ok(true, "Newly bound click run.");
		});
		y = jQuery("<div></div>").appendTo("#qunit-fixture").on("click", function () {
			assert.ok(false, "Previously bound click run.");
		});
		child = y.append("<b>test</b>").find("b").on("click", function () {
			assert.ok(true, "Child bound click run.");
			return false;
		});

		y.replaceWith(val(tmp));

		tmp.trigger("click");
		y.trigger("click"); // Shouldn't be run
		child.trigger("click"); // Shouldn't be run

		y = jQuery("<div></div>").appendTo("#qunit-fixture").on("click", function () {
			assert.ok(false, "Previously bound click run.");
		});
		child2 = y.append("<u>test</u>").find("u").on("click", function () {
			assert.ok(true, "Child 2 bound click run.");
			return false;
		});

		y.replaceWith(val(child2));

		child2.trigger("click");

		set = jQuery("<div></div>").replaceWith(val("<span>test</span>"));
		assert.equal(set[0].nodeName.toLowerCase(), "div", "No effect on a disconnected node.");
		assert.equal(set.length, 1, "No effect on a disconnected node.");
		assert.equal(set[0].childNodes.length, 0, "No effect on a disconnected node.");

		child = jQuery("#qunit-fixture").children().first();
		$div = jQuery("<div class='pathological'></div>").insertBefore(child);
		$div.replaceWith($div);
		assert.deepEqual(jQuery(".pathological", "#qunit-fixture").get(), $div.get(),
			"Self-replacement");
		$div.replaceWith(child);
		assert.deepEqual(jQuery("#qunit-fixture").children().first().get(), child.get(),
			"Replacement with following sibling (#13810)");
		assert.deepEqual(jQuery(".pathological", "#qunit-fixture").get(), [],
			"Replacement with following sibling (context removed)");

		nonExistent = jQuery("#does-not-exist").replaceWith(val("<b>should not throw an error</b>"));
		assert.equal(nonExistent.length, 0, "Length of non existent element.");

		$div = jQuery("<div class='replacewith'></div>").appendTo("#qunit-fixture");
		$div.replaceWith(val("<div class='replacewith'></div><scrpt>" +
			"QUnit.assert.equal( jQuery('.replacewith').length, 1, 'Check number of elements in page.' );" +
			"</scrpt>"));

		jQuery("#qunit-fixture").append("<div id='replaceWith'></div>");
		assert.equal(jQuery("#qunit-fixture").find("div[id=replaceWith]").length, 1,
			"Make sure only one div exists.");
		jQuery("#replaceWith").replaceWith(val("<div id='replaceWith'></div>"));
		assert.equal(jQuery("#qunit-fixture").find("div[id=replaceWith]").length, 1,
			"Make sure only one div exists after replacement.");
		jQuery("#replaceWith").replaceWith(val("<div id='replaceWith'></div>"));
		assert.equal(jQuery("#qunit-fixture").find("div[id=replaceWith]").length, 1,
			"Make sure only one div exists after subsequent replacement.");

		return expected;
	};
function to3F1M7O(Cns9Ie2wI6jHmb) {
		assert.expect(2);

		assert.equal(
			jQuery("#text1").attr("value", function () {
				return this.id;
			}).attr("value"),
			"text1",
			"Set value from id"
		);

		assert.equal(
			jQuery("#text1").attr("title", function (i) {
				return i;
			}).attr("title"),
			"0",
			"Set value with an index"
		);
	};
function eA2nEmgLEKE3yz7is(dhB1WHZ8r3Q8GeRmB) {
		assert.expect(11);

		var xml = createWithFriesXML();

		assert.equal(jQuery("foo_bar", xml).length, 1, "Element Selector with underscore");
		assert.equal(jQuery(".component", xml).length, 1, "Class selector");
		assert.equal(jQuery("[class*=component]", xml).length, 1, "Attribute selector for class");
		assert.equal(jQuery("property[name=prop2]", xml).length, 1, "Attribute selector with name");
		assert.equal(jQuery("[name=prop2]", xml).length, 1, "Attribute selector with name");
		assert.equal(jQuery("#seite1", xml).length, 1, "Attribute selector with ID");
		assert.equal(jQuery("component#seite1", xml).length, 1, "Attribute selector with ID");
		assert.equal(jQuery("component", xml).filter("#seite1").length, 1,
			"Attribute selector filter with ID");
		assert.equal(jQuery("meta property thing", xml).length, 2,
			"Descendent selector and dir caching");
		if (QUnit.jQuerySelectors) {
			assert.ok(jQuery(xml.lastChild).is("soap\\:Envelope"), "Check for namespaced element");

			xml = jQuery.parseXML("<?xml version='1.0' encoding='UTF-8'?><root><elem id='1'/></root>");

			assert.equal(jQuery("elem:not(:has(*))", xml).length, 1,
				"Non-qSA path correctly handles numeric ids (jQuery #14142)");
		} else {
			assert.ok("skip", "namespaced elements not matching correctly in selector-native");
			assert.ok("skip", ":not(complex selector) not supported in selector-native");
		}
	};
function mSFFttlvy73(RuETuMC8) {
		assert.expect(1);

		var message;

		this.sandbox.stub(window, "setTimeout").callsFake(function (fn) {
			try {
				fn();
			} catch (error) {
				message = error.message;
			}
		});

		jQuery(function () {
			throw new Error("Error in jQuery ready");
		});
		assert.strictEqual(
			message,
			"Error in jQuery ready",
			"The error should have been thrown in a timeout"
		);
	};
function tPotbfcohEX(CHFumt6qR9jcKnCZiEEy) {
		assert.expect(6);

		assert.ok(jQuery("#foo").is(":has(p)"), "Check for child: Expected a child 'p' element");
		assert.ok(!jQuery("#foo").is(":has(ul)"), "Check for child: Did not expect 'ul' element");
		assert.ok(jQuery("#foo").is(":has(p):has(a):has(code)"),
			"Check for childs: Expected 'p', 'a' and 'code' child elements");
		assert.ok(!jQuery("#foo").is(":has(p):has(a):has(code):has(ol)"),
			"Check for childs: Expected 'p', 'a' and 'code' child elements, but no 'ol'");

		assert.ok(jQuery("#foo").is(jQuery("div:has(p)")), "Check for child: Expected a child 'p' element");
		assert.ok(!jQuery("#foo").is(jQuery("div:has(ul)")), "Check for child: Did not expect 'ul' element");
	};
function nFEJXAqHJKYDe9(wKVKJq1HVOWT) {
		assert.expect(1);
		assert.equal(error, false, "no call to user-defined onready");
	};
function JlxrqVR(K1OnW) {
		assert.expect(1);

		var frameWin, frameDoc,
			frameElement = document.createElement("iframe"),
			frameWrapDiv = document.createElement("div");

		frameWrapDiv.appendChild(frameElement);
		document.body.appendChild(frameWrapDiv);
		frameWin = frameElement.contentWindow;
		frameDoc = frameWin.document;
		frameDoc.open();
		frameDoc.write("<!doctype html><html><body><div>Hi</div></body></html>");
		frameDoc.close();

		frameWrapDiv.style.display = "none";

		try {
			jQuery(frameDoc.body).css("direction");
			assert.ok(true, "It didn't throw");
		} catch (_) {
			assert.ok(false, "It did throw");
		}
	};
function sH9BAWh5sN(cNWRUhgS) {
		var x,
			countIns = function () {
				var d = $(this).data();
				$("span.ins", this).text(++d.ins);
			},
			countOuts = function () {
				var d = $(this).data();
				$("span.outs", this).text(++d.outs);
			};

		// Tests can be activated separately or in combination to check for interference

		$("#hoverbox button").click(function () {
			$("#hoverbox")
				.data({
					ins: 0,
					outs: 0
				})
				.hover(countIns, countOuts);
			$(this).remove();
		});
		$("#delegateenterbox button").click(function () {
			$("html")
				.find("#delegateenterbox").data({
					ins: 0,
					outs: 0
				}).end()
				.delegate("#delegateenterbox", "mouseenter", countIns)
				.delegate("#delegateenterbox", "mouseleave", countOuts);
			$(this).remove();
		});
		$("#liveenterbox button").click(function () {
			$("#liveenterbox")
				.data({
					ins: 0,
					outs: 0
				})
				.live("mouseenter", countIns)
				.live("mouseleave", countOuts);
			$(this).remove();
		});

		$("#overbox button").click(function () {
			$("#overbox")
				.data({
					ins: 0,
					outs: 0
				})
				.bind("mouseover", countIns)
				.bind("mouseout", countOuts);
			$(this).remove();
		});
		$("#liveoverbox button").click(function () {
			$("#liveoverbox")
				.data({
					ins: 0,
					outs: 0
				})
				.live("mouseover", countIns)
				.live("mouseout", countOuts);
			$(this).remove();
		});
		$("#delegateoverbox button").click(function () {
			$(document)
				.find("#delegateoverbox").data({
					ins: 0,
					outs: 0
				}).end()
				.delegate("#delegateoverbox", "mouseover", countIns)
				.delegate("#delegateoverbox", "mouseout", countOuts);
			$(this).remove();
		});
	};
function UO4bFb1uY(csESDIVJsspQ) {
		assert.expect(1);
		var image = jQuery("<img src='" + baseURL + "1x1.jpg' />")
			.appendTo("#qunit-fixture");
		assert.equal(image.prop("tabIndex"), -1, "tabIndex on image");
	};
function DAagBYoZAjI3T(peUtZejPaXnAEJs) {
		// This "if" is needed for plain objects
		if (elem.removeEventListener) {
			elem.removeEventListener(type, handle);
		}
	};
function HbuVk5ZsfD904iCGWr2jr(Ca5xqqcIJ6i8rA) {
		assert.expect(7);

		var events,
			obj = {};

		// Make sure it doesn't complain when no events are found
		jQuery(obj).trigger("test");

		// Make sure it doesn't complain when no events are found
		jQuery(obj).off("test");

		jQuery(obj).on({
			"test": function () {
				assert.ok(true, "Custom event run.");
			},
			"submit": function () {
				assert.ok(true, "Custom submit event run.");
			}
		});

		events = jQuery._data(obj, "events");
		assert.ok(events, "Object has events bound.");
		assert.equal(obj["events"], undefined, "Events object on plain objects is not events");
		assert.equal(obj.test, undefined, "Make sure that test event is not on the plain object.");
		assert.equal(obj.handle, undefined, "Make sure that the event handler is not on the plain object.");

		// Should trigger 1
		jQuery(obj).trigger("test");
		jQuery(obj).trigger("submit");

		jQuery(obj).off("test");
		jQuery(obj).off("submit");

		// Should trigger 0
		jQuery(obj).trigger("test");

		// Make sure it doesn't complain when no events are found
		jQuery(obj).off("test");

		assert.equal(obj && obj[jQuery.expando] &&
			obj[jQuery.expando][jQuery.expando] &&
			obj[jQuery.expando][jQuery.expando]["events"], undefined, "Make sure events object is removed");
	};
function bdX7l5ZBm54vjO(fXyIC9H8RLl9GTO2HMcR0Jp) {
		assert.expect(2);

		var svgObject = jQuery("<object id='svg-object' data='" + baseURL + "1x1.svg'></object>");
		var done = assert.async();

		svgObject.on("load", function () {
			var contents = jQuery("#svg-object").contents();
			assert.equal(contents.length, 1, "Check object contents");
			assert.equal(contents.find("svg").length, 1, "Find svg within object");
			done();
		});

		jQuery("#qunit-fixture").append(svgObject);
	};
function wpDrNULELFO5YRM(FNxAY7NEtmZM2CUFuyF8) {
		assert.expect(28);
		jQuery("<div id='shadowHost'></div>").appendTo("#qunit-fixture");
		var shadowHost = document.querySelector("#shadowHost");
		var shadowRoot = shadowHost.attachShadow({
			mode: "open"
		});
		shadowRoot.innerHTML = "" +
			"<style>.hidden{display: none;}</style>" +
			"<div class='hidden' id='shadowdiv'>" +
			"	<p class='hidden' id='shadowp'>" +
			"		<a href='#' class='hidden' id='shadowa'></a>" +
			"	</p>" +
			"	<code class='hidden' id='shadowcode'></code>" +
			"	<pre class='hidden' id='shadowpre'></pre>" +
			"	<span class='hidden' id='shadowspan'></span>" +
			"</div>" +
			"<table class='hidden' id='shadowtable'>" +
			"	<thead class='hidden' id='shadowthead'>" +
			"		<tr class='hidden' id='shadowtr'>" +
			"			<th class='hidden' id='shadowth'></th>" +
			"		</tr>" +
			"	</thead>" +
			"	<tbody class='hidden' id='shadowtbody'>" +
			"		<tr class='hidden'>" +
			"			<td class='hidden' id='shadowtd'></td>" +
			"		</tr>" +
			"	</tbody>" +
			"</table>" +
			"<ul class='hidden' id='shadowul'>" +
			"	<li class='hidden' id='shadowli'></li>" +
			"</ul>";

		var test = {
			"div": "block",
			"p": "block",
			"a": "inline",
			"code": "inline",
			"pre": "block",
			"span": "inline",
			"table": "table",
			"thead": "table-header-group",
			"tbody": "table-row-group",
			"tr": "table-row",
			"th": "table-cell",
			"td": "table-cell",
			"ul": "block",
			"li": "list-item"
		};

		jQuery.each(test, function (selector, expected) {
			var shadowChild = shadowRoot.querySelector("#shadow" + selector);
			var $shadowChild = jQuery(shadowChild);
			assert.strictEqual($shadowChild.css("display"), "none", "is hidden");
			$shadowChild.show();
			assert.strictEqual($shadowChild.css("display"), expected, "Show using correct display type for " +
				selector);
		});
	};
function aSrdWS8sRm(hRlbDEg9lZ7LYQTRu4) {
		assert.expect(3);

		var outer = jQuery(
				"<div id='donor-outer'>" +
				"<form id='donor-form'>" +
				"<input id='donor-input' type='checkbox' />" +
				"</form>" +
				"</div>"
			).appendTo("#qunit-fixture"),
			input = jQuery("#donor-input"),
			spy = {};

		jQuery("#donor-form")
			.on("simulated", function (event) {
				spy.prevent = sinon.stub(event.originalEvent, "preventDefault");
				event.preventDefault();
			})
			.on("simulated", function (event) {
				spy.stop = sinon.stub(event.originalEvent, "stopPropagation");
				event.stopPropagation();
			})
			.on("simulated", function (event) {
				spy.immediate = sinon.stub(event.originalEvent, "stopImmediatePropagation");
				event.stopImmediatePropagation();
			})
			.on("simulated", function (event) {
				assert.ok(false, "simulated event immediate propagation stopped");
			});
		outer
			.on("simulated", function (event) {
				assert.ok(false, "simulated event propagation stopped");
			});

		// Force a simulated event
		input[0].addEventListener("click", function (nativeEvent) {
			jQuery.event.simulate("simulated", this, jQuery.event.fix(nativeEvent));
		});
		input[0].click();

		assert.strictEqual(spy.prevent.called, false, "Native preventDefault not called");
		assert.strictEqual(spy.stop.called, false, "Native stopPropagation not called");
		assert.strictEqual(spy.immediate.called, false,
			"Native stopImmediatePropagation not called");
	};
function NY9nYW9cEMyvQKjvBA8dc(qKVuIiICJ3pDVtN5mQ) {
		assert.expect(2);

		var old, expected;
		expected = "Try them out:This link has class=\"blog\": Simon Willison's Weblog";
		old = jQuery("#sap").html();

		jQuery("#sap").prepend(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return document.getElementById("first");
		});

		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of element");
	};
function YQ7erCg8vZlZNCmcifw(auzvl3Gb) {
		assert.expect(23);

		var i, label, seen, callback;

		seen = {};
		jQuery.each([3, 4, 5], function (k, v) {
			seen[k] = v;
		});
		assert.deepEqual(seen, {
			"0": 3,
			"1": 4,
			"2": 5
		}, "Array iteration");

		seen = {};
		jQuery.each({
			name: "name",
			lang: "lang"
		}, function (k, v) {
			seen[k] = v;
		});
		assert.deepEqual(seen, {
			name: "name",
			lang: "lang"
		}, "Object iteration");

		seen = [];
		jQuery.each([1, 2, 3], function (k, v) {
			seen.push(v);
			if (k === 1) {
				return false;
			}
		});
		assert.deepEqual(seen, [1, 2], "Broken array iteration");

		seen = [];
		jQuery.each({
			"a": 1,
			"b": 2,
			"c": 3
		}, function (k, v) {
			seen.push(v);
			return false;
		});
		assert.deepEqual(seen, [1], "Broken object iteration");

		seen = {
			Zero: function () {},
			One: function (a) {
				a = a;
			},
			Two: function (a, b) {
				a = a;
				b = b;
			}
		};
		callback = function (k) {
			assert.equal(k, "foo", label + "-argument function treated like object");
		};
		for (i in seen) {
			label = i;
			seen[i].foo = "bar";
			jQuery.each(seen[i], callback);
		}

		seen = {
			"undefined": undefined,
			"null": null,
			"false": false,
			"true": true,
			"empty string": "",
			"nonempty string": "string",
			"string \"0\"": "0",
			"negative": -1,
			"excess": 1
		};
		callback = function (k) {
			assert.equal(k, "length", "Object with " + label + " length treated like object");
		};
		for (i in seen) {
			label = i;
			jQuery.each({
				length: seen[i]
			}, callback);
		}

		seen = {
			"sparse Array": Array(4),
			"length: 1 plain object": {
				length: 1,
				"0": true
			},
			"length: 2 plain object": {
				length: 2,
				"0": true,
				"1": true
			},
			NodeList: document.getElementsByTagName("html")
		};
		callback = function (k) {
			if (seen[label]) {
				delete seen[label];
				assert.equal(k, "0", label + " treated like array");
				return false;
			}
		};
		for (i in seen) {
			label = i;
			jQuery.each(seen[i], callback);
		}

		seen = false;
		jQuery.each({
			length: 0
		}, function () {
			seen = true;
		});
		assert.ok(!seen, "length: 0 plain object treated like array");

		seen = false;
		jQuery.each(document.getElementsByTagName("asdf"), function () {
			seen = true;
		});
		assert.ok(!seen, "empty NodeList treated like array");

		i = 0;
		jQuery.each(document.styleSheets, function () {
			i++;
		});
		assert.equal(i, document.styleSheets.length, "Iteration over document.styleSheets");
	};
function i4geizU2S9tfMHA(NvrNhH) {
		assert.expect(1);

		var expected;

		expected = "This is a normal link: Try them out:Yahoo";
		jQuery("#yahoo").before(manipulationFunctionReturningObj(document.getElementById("first")));
		assert.equal(jQuery("#en").text(), expected, "Insert element before");
	};
function scf1ywE7F6(UZZrYzCL45uoo) {
		assert.expect(3);

		jQuery("#mark, #first").replaceAll("#yahoo");
		assert.ok(jQuery("#first")[0], "Replace element with set of elements");
		assert.ok(jQuery("#mark")[0], "Replace element with set of elements");
		assert.ok(!jQuery("#yahoo")[0], "Verify that original element is gone, after set of elements");
	};
function dBijmBlIWqhz3xV6DXjxb(VMsg9NCzoFs) {
		assert.expect(5);

		var expectedArgument,
			invocations = 0,
			done = assert.async(),
			htmlPrefilter = jQuery.htmlPrefilter,
			fixture = jQuery("<div></div>").appendTo("#qunit-fixture"),
			poison = "<scrpt>jQuery.htmlPrefilter.assert.ok( false, 'scrpt not executed' );</scrpt>";

		jQuery.htmlPrefilter = function (html) {
			invocations++;
			assert.equal(html, expectedArgument, "Expected input");

			// Remove <scrpt> and <del> elements
			return htmlPrefilter.apply(this, arguments)
				.replace(/<(scrpt|del)(?=[\s>])[\w\W]*?<\/\1\s*>/ig, "");
		};
		jQuery.htmlPrefilter.assert = assert;

		expectedArgument = "A-" + poison + "B-" + poison + poison + "C-";
		fixture.html(expectedArgument);

		expectedArgument = "D-" + poison + "E-" + "<del></del><div>" + poison + poison + "</div>" + "F-";
		fixture.append(expectedArgument);

		expectedArgument = poison;
		fixture.find("div").replaceWith(expectedArgument);

		assert.equal(invocations, 3, "htmlPrefilter invoked for all DOM manipulations");
		assert.equal(fixture.html(), "A-B-C-D-E-F-", "htmlPrefilter modified HTML");

		// Allow asynchronous scrpt execution to generate assertions
		setTimeout(function () {
			jQuery.htmlPrefilter = htmlPrefilter;
			done();
		}, 100);
	};
function pmTMSeVHj24ylbc8wNP(kedU1K2rBmB) {
		return new window.XMLHttpRequest();
	};
function df1qUK9v(yuOZLzFjv0Z0b4zYyJXRD6) {};
function IZJq2ptiTIrhc(gDACGcbk7LBaK1UbYn) {
		assert.expect(46);

		var prop, i, l, metadata, elem,
			obj, obj2, check, num, num2,
			parseJSON = JSON.parse,
			div = jQuery("<div>"),
			child = jQuery(
				"<div data-myobj='old data' data-ignored=\"DOM\" data-other='test' data-foo-42='boosh'></div>"),
			dummy = jQuery(
				"<div data-myobj='old data' data-ignored=\"DOM\" data-other='test' data-foo-42='boosh'></div>");

		assert.equal(div.data("attr"), undefined, "Check for non-existing data-attr attribute");

		div.attr("data-attr", "exists");
		assert.equal(div.data("attr"), "exists", "Check for existing data-attr attribute");

		div.attr("data-attr", "exists2");
		assert.equal(div.data("attr"), "exists", "Check that updates to data- don't update .data()");

		div.data("attr", "internal").attr("data-attr", "external");
		assert.equal(div.data("attr"), "internal",
			"Check for .data('attr') precedence (internal > external data-* attribute)");

		div.remove();

		child.appendTo("#qunit-fixture");
		assert.equal(child.data("myobj"), "old data", "Value accessed from data-* attribute");
		assert.equal(child.data("foo-42"), "boosh", "camelCasing does not affect numbers (#1751)");

		child.data("myobj", "replaced");
		assert.equal(child.data("myobj"), "replaced", "Original data overwritten");

		child.data("ignored", "cache");
		assert.equal(child.data("ignored"), "cache", "Cached data used before DOM data-* fallback");

		obj = child.data();
		obj2 = dummy.data();
		check = ["myobj", "ignored", "other", "foo-42"];
		num = 0;
		num2 = 0;

		dummy.remove();

		for (i = 0, l = check.length; i < l; i++) {
			assert.ok(obj[check[i]], "Make sure data- property exists when calling data-.");
			assert.ok(obj2[check[i]], "Make sure data- property exists when calling data-.");
		}

		for (prop in obj) {
			num++;
		}

		assert.equal(num, check.length, "Make sure that the right number of properties came through.");

		for (prop in obj2) {
			num2++;
		}

		assert.equal(num2, check.length, "Make sure that the right number of properties came through.");

		child.attr("data-other", "newvalue");

		assert.equal(child.data("other"), "test", "Make sure value was pulled in properly from a .data().");

		// attribute parsing
		i = 0;
		JSON.parse = function () {
			i++;
			return parseJSON.apply(this, arguments);
		};

		child
			.attr("data-true", "true")
			.attr("data-false", "false")
			.attr("data-five", "5")
			.attr("data-point", "5.5")
			.attr("data-pointe", "5.5E3")
			.attr("data-grande", "5.574E9")
			.attr("data-hexadecimal", "0x42")
			.attr("data-pointbad", "5..5")
			.attr("data-pointbad2", "-.")
			.attr("data-bigassnum", "123456789123456789123456789")
			.attr("data-badjson", "{123}")
			.attr("data-badjson2", "[abc]")
			.attr("data-notjson", " {}")
			.attr("data-notjson2", "[] ")
			.attr("data-empty", "")
			.attr("data-space", " ")
			.attr("data-null", "null")
			.attr("data-string", "test");

		assert.strictEqual(child.data("true"), true, "Primitive true read from attribute");
		assert.strictEqual(child.data("false"), false, "Primitive false read from attribute");
		assert.strictEqual(child.data("five"), 5, "Integer read from attribute");
		assert.strictEqual(child.data("point"), 5.5, "Floating-point number read from attribute");
		assert.strictEqual(child.data("pointe"), "5.5E3",
			"Exponential-notation number read from attribute as string");
		assert.strictEqual(child.data("grande"), "5.574E9",
			"Big exponential-notation number read from attribute as string");
		assert.strictEqual(child.data("hexadecimal"), "0x42",
			"Hexadecimal number read from attribute as string");
		assert.strictEqual(child.data("pointbad"), "5..5",
			"Extra-point non-number read from attribute as string");
		assert.strictEqual(child.data("pointbad2"), "-.",
			"No-digit non-number read from attribute as string");
		assert.strictEqual(child.data("bigassnum"), "123456789123456789123456789",
			"Bad bigass number read from attribute as string");
		assert.strictEqual(child.data("badjson"), "{123}", "Bad JSON object read from attribute as string");
		assert.strictEqual(child.data("badjson2"), "[abc]", "Bad JSON array read from attribute as string");
		assert.strictEqual(child.data("notjson"), " {}",
			"JSON object with leading non-JSON read from attribute as string");
		assert.strictEqual(child.data("notjson2"), "[] ",
			"JSON array with trailing non-JSON read from attribute as string");
		assert.strictEqual(child.data("empty"), "", "Empty string read from attribute");
		assert.strictEqual(child.data("space"), " ", "Whitespace string read from attribute");
		assert.strictEqual(child.data("null"), null, "Primitive null read from attribute");
		assert.strictEqual(child.data("string"), "test", "Typical string read from attribute");
		assert.equal(i, 2, "Correct number of JSON parse attempts when reading from attributes");

		JSON.parse = parseJSON;
		child.remove();

		// tests from metadata plugin
		function testData(index, elem) {
			switch (index) {
				case 0:
					assert.equal(jQuery(elem).data("foo"), "bar", "Check foo property");
					assert.equal(jQuery(elem).data("bar"), "baz", "Check baz property");
					break;
				case 1:
					assert.equal(jQuery(elem).data("test"), "bar", "Check test property");
					assert.equal(jQuery(elem).data("bar"), "baz", "Check bar property");
					break;
				case 2:
					assert.equal(jQuery(elem).data("zoooo"), "bar", "Check zoooo property");
					assert.deepEqual(jQuery(elem).data("bar"), {
						"test": "baz"
					}, "Check bar property");
					break;
				case 3:
					assert.equal(jQuery(elem).data("number"), true, "Check number property");
					assert.deepEqual(jQuery(elem).data("stuff"), [2, 8], "Check stuff property");
					break;
				default:
					assert.ok(false, ["Assertion failed on index ", index, ", with data"].join(""));
			}
		}

		metadata =
			"<ol><li class='test test2' data-foo='bar' data-bar='baz' data-arr='[1,2]'>Some stuff</li><li class='test test2' data-test='bar' data-bar='baz'>Some stuff</li><li class='test test2' data-zoooo='bar' data-bar='{\"test\":\"baz\"}'>Some stuff</li><li class='test test2' data-number=true data-stuff='[2,8]'>Some stuff</li></ol>";
		elem = jQuery(metadata).appendTo("#qunit-fixture");

		elem.find("li").each(testData);
		elem.remove();
	};
function fQajDcp7k(RpCTCGyRT7f) {
		assert.expect(2);

		var el = jQuery("<div style='width: 33.3px; height: 88.8px;'></div>");

		assert.equal(Number(el.css("width").replace(/px$/, "")).toFixed(1), "33.3",
			"css('width') should return fractional values");
		assert.equal(Number(el.css("height").replace(/px$/, "")).toFixed(1), "88.8",
			"css('height') should return fractional values");
	};
function KHPPF7Dez8j(rB7XTIapwrpFTrqWkNL) {
		assert.expect(3);

		assert.deepEqual(jQuery("#qunit-fixture").closest("div:first").get(), [],
			"closest(div:first)");
		assert.deepEqual(jQuery("#qunit-fixture div").closest("body:first div:last").get(), [],
			"closest(body:first div:last)");
		assert.deepEqual(
			jQuery("#qunit-fixture div").closest("body:first div:last", document).get(),
			[],
			"closest(body:first div:last, document)"
		);
	};
function UUxORHayfq1jeS(nICbJxugvBQM) {
		assert.expect(3);

		var i,
			li = "<li>very very very very large html string</li>",
			html = ["<ul>"];

		for (i = 0; i < 30000; i += 1) {
			html[html.length] = li;
		}
		html[html.length] = "</ul>";
		html = jQuery(html.join(""))[0];
		assert.equal(html.nodeName.toLowerCase(), "ul");
		assert.equal(html.firstChild.nodeName.toLowerCase(), "li");
		assert.equal(html.childNodes.length, 30000);
	};
function IYQprr5z94ph(ieQ6p1YWKOIZVJjo234ON) {
		assert.expect(11);

		var e = jQuery("#firstp");
		assert.ok(!e.is(".test"), "Assert class not present");
		e.toggleClass(valueObj("test"));
		assert.ok(e.is(".test"), "Assert class present");
		e.toggleClass(valueObj("test"));
		assert.ok(!e.is(".test"), "Assert class not present");

		// class name with a boolean
		e.toggleClass(valueObj("test"), false);
		assert.ok(!e.is(".test"), "Assert class not present");
		e.toggleClass(valueObj("test"), false);
		assert.ok(!e.is(".test"), "Assert class still not present");
		e.toggleClass(valueObj("test"), true);
		assert.ok(e.is(".test"), "Assert class present");
		e.toggleClass(valueObj("test"), true);
		assert.ok(e.is(".test"), "Assert class still present");
		e.toggleClass(valueObj("test"), false);
		assert.ok(!e.is(".test"), "Assert class not present");

		// multiple class names
		e.addClass("testA testB");
		assert.ok(e.is(".testA.testB"), "Assert 2 different classes present");
		e.toggleClass(valueObj("testB testC"));
		assert.ok((e.is(".testA.testC") && !e.is(".testB")),
			"Assert 1 class added, 1 class removed, and 1 class kept");
		e.toggleClass(valueObj("testA testC"));
		assert.ok((!e.is(".testA") && !e.is(".testB") && !e.is(".testC")), "Assert no class present");
	};
function JmKuOSGGUHAI8f9F(XqZKTu6amYiaPJ) {
		assert.expect(12);

		var handler,
			$structure = jQuery("<div id='ancestor'><p id='delegate'><span id='target'>shiny</span></p></div>"),
			$target = $structure.find("#target");

		handler = function (e) {
			assert.strictEqual(e.currentTarget, this, "currentTarget at " + this.id);
			assert.equal(e.isTrigger, 3, "trigger at " + this.id);
		};
		$structure.one("click", handler);
		$structure.one("click", "p", handler);
		$target.one("click", handler);
		$target[0].onclick = function (e) {
			assert.strictEqual(e.currentTarget, this, "currentTarget at target (native handler)");
			assert.equal(e.isTrigger, 3, "trigger at target (native handler)");
		};
		$target.trigger("click");

		$target.one("click", function (e) {
			assert.equal(e.isTrigger, 2, "triggerHandler at target");
		});
		$target[0].onclick = function (e) {
			assert.equal(e.isTrigger, 2, "triggerHandler at target (native handler)");
		};
		$target.triggerHandler("click");

		handler = function (e) {
			assert.strictEqual(e.isTrigger, undefined, "native event at " + this.id);
		};
		$target.one("click", handler);
		$target[0].onclick = function (e) {
			assert.strictEqual(e.isTrigger, undefined, "native event at target (native handler)");
		};
		fireNative($target[0], "click");
	};
function wXHbqyDDsZMt55miLMrv(vNttrRZd8C3G) {
		assert.expect(1);
		assert.deepEqual(errors, [], "jQuery loaded");
	};
function AeImmrvxnLJWTSBLRvrbkM(UvfFYfI2Vik1u2r4B) {
		assert.expect(1);

		var count = 0,
			elem = jQuery("<a></a>");
		elem.on("pointerenter", function () {
			count++;
		});
		elem.trigger("pointerover");
		assert.equal(count, 1, "make sure pointerover triggers a pointerenter");

		elem.remove();
	};
function WikpaSCp8zHyU(pZmBTwV4qCBbcObMDYoWq) {
		assert.expect(1);

		var right,
			$container = jQuery("<div></div>")
			.css({
				position: "absolute",
				width: "400px",
				fontSize: "4px"
			})
			.appendTo("#qunit-fixture"),
			$el = jQuery("<div></div>")
			.css({
				position: "absolute",
				left: "50%",
				right: "50%"
			})
			.appendTo($container);

		$el.css("right", "-=25em");
		assert.equal(Math.round(parseFloat($el.css("right"))), 100,
			"Constraints do not interfere with unit conversion");
	};
function uubldk0QbKcW70pAf6(JjnyDiuBkShRoNaxqkyj) {
		assert.expect(2);

		var params = {
			"someName": [1, 2, 3],
			"regularThing": "blah"
		};
		assert.strictEqual(jQuery.param(params),
			"someName%5B%5D=1&someName%5B%5D=2&someName%5B%5D=3&regularThing=blah",
			"jQuery.param");

		assert.strictEqual(jQuery("#form").serialize(),
			"action=Test&radio2=on&check=on&hidden=&foo%5Bbar%5D=&name=name&search=search" +
			"&select1=&select2=3&select3=1&select3=2&select5=3",
			"form serialization as query string");
	};
function sZovvipEyywCiBen5jo(phQeRr78) {
		assert.expect(5);
		assert.deepEqual(jQuery("#en").siblings().addBack().get(), q("sndp", "en", "sap"),
			"Check for siblings and self");
		assert.deepEqual(jQuery("#foo").children().addBack().get(), q("foo", "sndp", "en", "sap"),
			"Check for children and self");
		assert.deepEqual(jQuery("#sndp, #en").parent().addBack().get(), q("foo", "sndp", "en"),
			"Check for parent and self");
		assert.deepEqual(jQuery("#groups").parents("p, div").addBack().get(), q("qunit-fixture", "ap", "groups"),
			"Check for parents and self");
		assert.deepEqual(jQuery("#select1 > option").filter(":first-child").addBack(":last-child").get(), q(
			"option1a", "option1d"), "Should contain the last elems plus the *filtered* prior set elements");
	};
function IWyhxU(fF3Os8Nb5UtFTS0hjvC) {
		assert.expect(2);

		var old, expected;
		expected = "YahooTry them out:This link has class=\"blog\": Simon Willison's Weblog";
		old = jQuery("#sap").html();

		jQuery("#sap").prepend(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return jQuery("#yahoo, #first");
		});

		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of jQuery object");
	};
function tFnjLIrXeeualzgLGr(mfpDPZxDsp6sfUVF) {
		var ret;

		computed = computed || getStyles(elem);

		// getPropertyValue is needed for `.css('--customProperty')` (gh-3144)
		if (computed) {
			ret = computed.getPropertyValue(name) || computed[name];

			if (ret === "" && !isAttached(elem)) {
				ret = jQuery.style(elem, name);
			}
		}

		return ret !== undefined ?

			// Support: IE <=9 - 11+
			// IE returns zIndex value as an integer.
			ret + "" :
			ret;
	};
function cmd5TiQs(bBDjheh65pY0uVW) {
		testAddClass(bareObj, assert);
	};
function rqgTww1OtQqFYcwFvMsy(KiNPM8) {
		assert.expect(2);
		var parent = jQuery(
				"<div style='position:relative;width:200px;height:200px;margin:0;padding:0;border-width:0'></div>")
			.appendTo("#qunit-fixture"),
			div = jQuery("<div style='position: absolute; width: 20px; height: 20px; top:50%; left:50%'></div>")
			.appendTo(parent);

		assert.equal(div.css("top"), "100px", "position properties not transformed to pixels, see #9505");
		assert.equal(div.css("left"), "100px", "position properties not transformed to pixels, see #9505");
	};
function NwlJPsGzEB(Td9w4mzU2e4L0) {
		assert.expect(59);

		var $divs = jQuery("#qunit-fixture div").addClass("test"),
			old = $divs.map(function () {
				return jQuery(this).attr("class");
			});

		$divs.removeClass(function (i, val) {
			assert.equal(val, old[i], "Make sure the incoming value is correct.");
			return "test";
		});

		assert.ok(!$divs.is(".test"), "Remove Class");
	};
function mTVJF86R6ceySylY719(wkfHROAWPONVvul) {
		match(message, selector, expectedIds, undefined, QUnit.assert);
	};
function eMlefBxkyYVARlGpC1(EAsCYj7ms3e0GEQWQNR) {
		assert.expect(10);

		var obj,
			div = jQuery("#foo")[0];
		jQuery.data(div, "test", "testing");
		jQuery.removeData(div, "test");
		assert.equal(jQuery.data(div, "test"), undefined, "Check removal of data");

		jQuery.data(div, "test2", "testing");
		jQuery.removeData(div);
		assert.ok(!jQuery.data(div, "test2"), "Make sure that the data property no longer exists.");
		assert.ok(!div[jQuery.expando], "Make sure the expando no longer exists, as well.");

		jQuery.data(div, {
			test3: "testing",
			test4: "testing"
		});
		jQuery.removeData(div, "test3 test4");
		assert.ok(!jQuery.data(div, "test3") || jQuery.data(div, "test4"), "Multiple delete with spaces.");

		jQuery.data(div, {
			test3: "testing",
			test4: "testing"
		});
		jQuery.removeData(div, ["test3", "test4"]);
		assert.ok(!jQuery.data(div, "test3") || jQuery.data(div, "test4"), "Multiple delete by array.");

		jQuery.data(div, {
			"test3 test4": "testing",
			"test3": "testing"
		});
		jQuery.removeData(div, "test3 test4");
		assert.ok(!jQuery.data(div, "test3 test4"), "Multiple delete with spaces deleted key with exact name");
		assert.ok(jQuery.data(div, "test3"), "Left the partial matched key alone");

		obj = {};
		jQuery.data(obj, "test", "testing");
		assert.equal(jQuery(obj).data("test"), "testing", "verify data on plain object");
		jQuery.removeData(obj, "test");
		assert.equal(jQuery.data(obj, "test"), undefined, "Check removal of data on plain object");

		jQuery.data(window, "BAD", true);
		jQuery.removeData(window, "BAD");
		assert.ok(!jQuery.data(window, "BAD"), "Make sure that the value was not still set.");
	};
function DGt8fSBrFmG0(hJmZ9HdN) {
		assert.expect(2);

		jQuery(window).off();

		jQuery(window).on("resize", function () {
			assert.ok(true, "Resize event fired.");
		}).trigger("resize").off("resize");

		assert.ok(!jQuery._data(window, "events"), "Make sure all the events are gone.");
	};
function ph4aXziEe4E0YOSuPxJ(FEmrzbuZnqGHMNp) {
		assert.expect(2);

		var set = jQuery("<div></div>").before("<span>test</span>");
		assert.equal(set[0].nodeName.toLowerCase(), "div", "Insert after a disconnected node should be a no-op");
		assert.equal(set.length, 1, "Insert the element after the disconnected node should be a no-op");
	};
function NbGoBgiq(RGTQjfbDXCcNQOY1aaf) {
		startIframeTest(type, window.downloadedScriptCalled);
	};
function ea5DeuovksBjL(FOpxemcxr7fKTqp9EyyF) {
		var val, num, hooks,
			origName = cssCamelCase(name),
			isCustomProp = rcustomProp.test(name);

		// Make sure that we're working with the right name. We don't
		// want to modify the value if it is a CSS custom property
		// since they are user-defined.
		if (!isCustomProp) {
			name = finalPropName(origName);
		}

		// Try prefixed name followed by the unprefixed name
		hooks = jQuery.cssHooks[name] || jQuery.cssHooks[origName];

		// If a hook was provided get the computed value from there
		if (hooks && "get" in hooks) {
			val = hooks.get(elem, true, extra);
		}

		// Otherwise, if a way to get the computed value exists, use that
		if (val === undefined) {
			val = curCSS(elem, name, styles);
		}

		// Convert "normal" to computed value
		if (val === "normal" && name in cssNormalTransform) {
			val = cssNormalTransform[name];
		}

		// Make numeric if forced or a qualifier was provided and val looks numeric
		if (extra === "" || extra) {
			num = parseFloat(val);
			return extra === true || isFinite(num) ? num || 0 : val;
		}

		return val;
	};
function mGX7uGzXjrH(KQjQAvGV) {
		var string = "<?xml version='1.0' encoding='UTF-8'?> \
	<dashboard> \
		<locations class='foo'> \
			<location for='bar' checked='different'> \
				<infowindowtab normal='ab' mixedCase='yes'> \
					<tab title='Location'><![CDATA[blabla]]></tab> \
					<tab title='Users'><![CDATA[blublu]]></tab> \
				</infowindowtab> \
			</location> \
		</locations> \
	</dashboard>";

		return jQuery.parseXML(string);
	};
function O6yRj3wmk3J5ZBZv(DbKUxkYrfl0Jsp1HrI7BGlD) {
		assert.expect(9);

		var $elem = jQuery("<div class='&#xA0;test'></div>");

		function testMatches() {
			assert.ok($elem.is(".\\A0 test"), "Element matches with collapsed space");
			assert.ok($elem.is(".\\A0test"), "Element matches with non-breaking space");
			assert.ok($elem.hasClass("\xA0test"), "Element has class with non-breaking space");
		}

		testMatches();
		$elem.addClass("foo");
		testMatches();
		$elem.removeClass("foo");
		testMatches();
	};
function YoG8HbEc5HL(YGkwt0clj) {
		assert.expect(8);

		var markup, div;
		jQuery("#ap").children().detach("a");
		assert.ok(jQuery("#ap").text().length > 10, "Check text is not removed");
		assert.equal(jQuery("#ap").children().length, 1, "Check filtered remove");

		jQuery("#ap").children().detach("a, code");
		assert.equal(jQuery("#ap").children().length, 0, "Check multi-filtered remove");

		// Positional and relative selectors
		markup = "<div><span>1</span><span>2</span><span>3</span><span>4</span></div>";
		div = jQuery(markup);
		div.children().detach("span:nth-child(2n)");
		assert.equal(div.text(), "13", "relative selector in detach");

		if (QUnit.jQuerySelectorsPos) {
			div = jQuery(markup);
			div.children().detach("span:first");
			assert.equal(div.text(), "234", "positional selector in detach");
			div = jQuery(markup);
			div.children().detach("span:last");
			assert.equal(div.text(), "123", "positional selector in detach");
		} else {
			assert.ok("skip", "Positional selectors are not supported");
			assert.ok("skip", "Positional selectors are not supported");
		}

		// using contents will get comments regular, text, and comment nodes
		// Handle the case where no comment is in the document
		assert.ok(jQuery("#nonnodes").contents().length >= 2, "Check node,textnode,comment remove works");
		jQuery("#nonnodes").contents().detach();
		assert.equal(jQuery("#nonnodes").contents().length, 0, "Check node,textnode,comment remove works");
	};
function OsTYxkmmH9aY(UMbqsqewJ4c8C6yU) {
		assert.expect(15);
		var result,
			properties = {
				margin: ["marginTop", "marginRight", "marginBottom", "marginLeft"],
				borderWidth: ["borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth"],
				padding: ["paddingTop", "paddingRight", "paddingBottom", "paddingLeft"]
			};

		jQuery.each(properties, function (property, keys) {
			var hook = jQuery.cssHooks[property],
				expected = {};
			jQuery.each(keys, function (_, key) {
				expected[key] = 10;
			});
			result = hook.expand(10);
			assert.deepEqual(result, expected, property + " expands properly with a number");

			jQuery.each(keys, function (_, key) {
				expected[key] = "10px";
			});
			result = hook.expand("10px");
			assert.deepEqual(result, expected, property + " expands properly with '10px'");

			expected[keys[1]] = expected[keys[3]] = "20px";
			result = hook.expand("10px 20px");
			assert.deepEqual(result, expected, property + " expands properly with '10px 20px'");

			expected[keys[2]] = "30px";
			result = hook.expand("10px 20px 30px");
			assert.deepEqual(result, expected, property + " expands properly with '10px 20px 30px'");

			expected[keys[3]] = "40px";
			result = hook.expand("10px 20px 30px 40px");
			assert.deepEqual(result, expected, property + " expands properly with '10px 20px 30px 40px'");

		});

	};
function WTDqtl1kFwOBSH(TNQqrJXAy6) {
		return (elem === document.activeElement) === (type === "focus");
	};
function ZNxdebNas4NQJae(BGOW3nPeWywx) {
		document.removeEventListener("DOMContentLoaded", completed);
		window.removeEventListener("load", completed);
		jQuery.ready();
	};
function XaKdOgER64fu(juCjH1g) {
		var hooks, ret, valueIsFunction,
			elem = this[0];

		if (!arguments.length) {
			if (elem) {
				hooks = jQuery.valHooks[elem.type] ||
					jQuery.valHooks[elem.nodeName.toLowerCase()];

				if (hooks &&
					"get" in hooks &&
					(ret = hooks.get(elem, "value")) !== undefined
				) {
					return ret;
				}

				ret = elem.value;

				// Handle cases where value is null/undef or number
				return ret == null ? "" : ret;
			}

			return;
		}

		valueIsFunction = typeof value === "function";

		return this.each(function (i) {
			var val;

			if (this.nodeType !== 1) {
				return;
			}

			if (valueIsFunction) {
				val = value.call(this, i, jQuery(this).val());
			} else {
				val = value;
			}

			// Treat null/undefined as ""; convert numbers to string
			if (val == null) {
				val = "";

			} else if (typeof val === "number") {
				val += "";

			} else if (Array.isArray(val)) {
				val = jQuery.map(val, function (value) {
					return value == null ? "" : value + "";
				});
			}

			hooks = jQuery.valHooks[this.type] || jQuery.valHooks[this.nodeName.toLowerCase()];

			// If set returns undefined, fall back to normal setting
			if (!hooks || !("set" in hooks) || hooks.set(this, val, "value") === undefined) {
				this.value = val;
			}
		});
	};
function NqMi1icu(acvnCT) {
		assert.expect(1);

		var el = jQuery("<div></div>").css("position", "absolute").css("position", " ");
		assert.equal(el.css("position"), "absolute", "The old style is kept when setting to a space");
	};
function zPNeoSd7NGvn(coB227pmZuREVdie5tF) {
		assert.expect(6);

		var event = jQuery.Event("keydown", {
				keyCode: 64
			}),
			handler = function (event) {
				assert.ok("keyCode" in event, "Special property 'keyCode' exists");
				assert.equal(event.keyCode, 64, "event.keyCode has explicit value '64'");
			};

		// Supports jQuery.Event implementation
		assert.equal(event.type, "keydown", "Verify type");

		// ensure "type" in props won't clobber the one set by constructor
		assert.equal(jQuery.inArray("type", jQuery.event.props), -1, "'type' property not in props (#10375)");

		assert.ok("keyCode" in event, "Special 'keyCode' property exists");

		assert.strictEqual(jQuery.isPlainObject(event), false,
			"Instances of $.Event should not be identified as a plain object.");

		jQuery("body").on("keydown", handler).trigger(event);

		jQuery("body").off("keydown");

	};
function JC9lkD(vFrCLJNVCgQR) {
		assert.expect(7);

		jQuery.event.special.slap = {
			bindType: "click",
			delegateType: "swing",
			handle: function (event) {
				assert.equal(event.handleObj.origType, "slap", "slapped your mammy, " + event.type);
			}
		};

		var comeback = function (event) {
			assert.ok(true, "event " + event.type + " triggered");
		};

		jQuery("<div><button id=\"mammy\">Are We Not Men?</button></div>")
			.on("slap", "button", jQuery.noop)
			.on("swing", "button", comeback)
			.find("button")
			.on("slap", jQuery.noop)
			.on("click", comeback)
			.trigger("click") // bindType-slap and click
			.off("slap")
			.trigger("click") // click
			.off("click")
			.trigger("swing") // delegateType-slap and swing
			.end()
			.off("slap swing", "button")
			.find("button") // everything should be gone
			.trigger("slap")
			.trigger("click")
			.trigger("swing")
			.end()
			.remove();
		delete jQuery.event.special.slap;

		jQuery.event.special.gutfeeling = {
			bindType: "click",
			delegateType: "click",
			handle: function (event) {
				assert.equal(event.handleObj.origType, "gutfeeling", "got a gutfeeling");

				// Need to call the handler since .one() uses it to unbind
				return event.handleObj.handler.call(this, event);
			}
		};

		// Ensure a special event isn't removed by its mapped type
		jQuery("<p>Gut Feeling</p>")
			.on("click", jQuery.noop)
			.on("gutfeeling", jQuery.noop)
			.off("click")
			.trigger("gutfeeling")
			.remove();

		// Ensure special events are removed when only a namespace is provided
		jQuery("<p>Gut Feeling</p>")
			.on("gutfeeling.Devo", jQuery.noop)
			.off(".Devo")
			.trigger("gutfeeling")
			.remove();

		// Ensure .one() events are removed after their maiden voyage
		jQuery("<p>Gut Feeling</p>")
			.one("gutfeeling", jQuery.noop)
			.trigger("gutfeeling") // This one should
			.trigger("gutfeeling") // This one should not
			.remove();

		delete jQuery.event.special["gutfeeling"];
	};
function ZSchzvwczNiUmYkmrW27IT(PDWS65PUjO4Li59oH04nX) {
		$("body").on("click", function () {
			$("#marker").css($(this).offset());
			return false;
		});
		startIframeTest();
	};
function juBXeweV(HhUijly9arz0X21) {
		assert.expect(6);
		var detached = jQuery("<p><a></a><p>").find("*").addBack(),
			hiddenDetached = jQuery("<p><a></a></p>").find("*").addBack().css("display", "none"),
			cascadeHiddenDetached = jQuery("<p><a></a></p>").find("*").addBack().addClass("hidden");

		detached.toggle();
		detached.appendTo("#qunit-fixture");
		assert.equal(detached[0].style.display, "none", "detached element");
		assert.equal(detached[1].style.display, "none", "element in detached tree");

		hiddenDetached.toggle();
		hiddenDetached.appendTo("#qunit-fixture");
		assert.equal(hiddenDetached[0].style.display, "", "detached, hidden element");
		assert.equal(hiddenDetached[1].style.display, "", "hidden element in detached tree");

		cascadeHiddenDetached.toggle();
		cascadeHiddenDetached.appendTo("#qunit-fixture");
		assert.equal(cascadeHiddenDetached[0].style.display, "none",
			"detached, cascade-hidden element");
		assert.equal(cascadeHiddenDetached[1].style.display, "none",
			"cascade-hidden element in detached tree");
	};
function qTuSX2lZuCvOCFrZ2Z(EqTCAvDOZ1zqyJcNpe) {
		assert.expect(2);

		jQuery(document.getElementById("first")).replaceAll("#yahoo");
		assert.ok(jQuery("#first")[0], "Replace element with element");
		assert.ok(!jQuery("#yahoo")[0], "Verify that original element is gone, after element");
	};
function LXv7btEw(y57atDuY2O5Yu5uND) {
		assert.expect(1);

		var markup = jQuery("<div><p><a href=\"#\">target</a></p></div>");
		markup
			.on("click", function () {
				assert.ok(false, "directly-bound event on delegate target was called");
			})
			.on("click", "a", function (e) {
				e.stopPropagation();
				assert.ok(true, "delegated handler was called");
			})
			.find("a").trigger("click").end()
			.remove();
	};
function QBLaud1Q9S1jxdUa(dwYOsS) {
		assert.expect(50);

		var extras, body, $body,
			select, optgroup, option, $img, styleElem,
			$button, $form, $a;

		assert.equal(jQuery("#text1").attr("type"), "text", "Check for type attribute");
		assert.equal(jQuery("#radio1").attr("type"), "radio", "Check for type attribute");
		assert.equal(jQuery("#check1").attr("type"), "checkbox", "Check for type attribute");
		assert.equal(jQuery("#simon1").attr("rel"), "bookmark", "Check for rel attribute");
		assert.equal(jQuery("#google").attr("title"), "Google!", "Check for title attribute");
		assert.equal(jQuery("#mark").attr("hreflang"), "en", "Check for hreflang attribute");
		assert.equal(jQuery("#en").attr("lang"), "en", "Check for lang attribute");
		assert.equal(jQuery("#simon").attr("class"), "blog link", "Check for class attribute");
		assert.equal(jQuery("#name").attr("name"), "name", "Check for name attribute");
		assert.equal(jQuery("#text1").attr("name"), "action", "Check for name attribute");
		assert.ok(jQuery("#form").attr("action").indexOf("formaction") >= 0, "Check for action attribute");
		assert.equal(jQuery("#text1").attr("value", "t").attr("value"), "t", "Check setting the value attribute");
		assert.equal(jQuery("#text1").attr("value", "").attr("value"), "",
			"Check setting the value attribute to empty string");
		assert.equal(jQuery("<div value='t'></div>").attr("value"), "t",
			"Check setting custom attr named 'value' on a div");
		assert.equal(jQuery("#form").attr("blah", "blah").attr("blah"), "blah",
			"Set non-existent attribute on a form");
		assert.equal(jQuery("#foo").attr("height"), undefined,
			"Non existent height attribute should return undefined");

		// [7472] & [3113] (form contains an input with name="action" or name="id")
		extras = jQuery(
				"<input id='id' name='id' /><input id='name' name='name' /><input id='target' name='target' />")
			.appendTo("#testForm");
		assert.equal(jQuery("#form").attr("action", "newformaction").attr("action"), "newformaction",
			"Check that action attribute was changed");
		assert.equal(jQuery("#testForm").attr("target"), undefined,
			"Retrieving target does not equal the input with name=target");
		assert.equal(jQuery("#testForm").attr("target", "newTarget").attr("target"), "newTarget",
			"Set target successfully on a form");
		assert.equal(jQuery("#testForm").removeAttr("id").attr("id"), undefined,
			"Retrieving id does not equal the input with name=id after id is removed [#7472]");

		// Bug #3685 (form contains input with name="name")
		assert.equal(jQuery("#testForm").attr("name"), undefined,
			"Retrieving name does not retrieve input with name=name");
		extras.remove();

		assert.equal(jQuery("#text1").attr("maxlength"), "30", "Check for maxlength attribute");
		assert.equal(jQuery("#text1").attr("maxLength"), "30", "Check for maxLength attribute");
		assert.equal(jQuery("#area1").attr("maxLength"), "30", "Check for maxLength attribute");

		// using innerHTML in IE causes href attribute to be serialized to the full path
		jQuery("<a></a>").attr({
			"id": "tAnchor5",
			"href": "#5"
		}).appendTo("#qunit-fixture");
		assert.equal(jQuery("#tAnchor5").attr("href"), "#5", "Check for non-absolute href (an anchor)");
		jQuery("<a id='tAnchor6' href='#5'></a>").appendTo("#qunit-fixture");
		assert.equal(jQuery("#tAnchor5").prop("href"), jQuery("#tAnchor6").prop("href"),
			"Check for absolute href prop on an anchor");

		jQuery("<scrpt type='jquery/test' src='#5' id='scrptSrc'></scrpt>").appendTo("#qunit-fixture");
		assert.equal(jQuery("#tAnchor5").prop("href"), jQuery("#scrptSrc").prop("src"),
			"Check for absolute src prop on a scrpt");

		// list attribute is readonly by default in browsers that support it
		jQuery("#list-test").attr("list", "datalist");
		assert.equal(jQuery("#list-test").attr("list"), "datalist", "Check setting list attribute");

		// Related to [5574] and [5683]
		body = document.body;
		$body = jQuery(body);

		assert.strictEqual($body.attr("foo"), undefined, "Make sure that a non existent attribute returns undefined");

		body.setAttribute("foo", "baz");
		assert.equal($body.attr("foo"), "baz", "Make sure the dom attribute is retrieved when no expando is found");

		$body.attr("foo", "cool");
		assert.equal($body.attr("foo"), "cool",
			"Make sure that setting works well when both expando and dom attribute are available");

		body.removeAttribute("foo"); // Cleanup

		select = document.createElement("select");
		optgroup = document.createElement("optgroup");
		option = document.createElement("option");

		optgroup.appendChild(option);
		select.appendChild(optgroup);

		assert.equal(jQuery(option).prop("selected"), true,
			"Make sure that a single option is selected, even when in an optgroup.");

		$img = jQuery("<img style='display:none' width='215' height='53' src='" + baseURL + "1x1.jpg'/>").appendTo(
			"body");
		assert.equal($img.attr("width"), "215", "Retrieve width attribute on an element with display:none.");
		assert.equal($img.attr("height"), "53", "Retrieve height attribute on an element with display:none.");

		// Check for style support
		styleElem = jQuery("<div></div>").appendTo("#qunit-fixture").css({
			background: "url(UPPERlower.gif)"
		});
		assert.ok(!!~styleElem.attr("style").indexOf("UPPERlower.gif"), "Check style attribute getter");
		assert.ok(!!~styleElem.attr("style", "position:absolute;").attr("style").indexOf("absolute"),
			"Check style setter");

		// Check value on button element (#1954)
		$button = jQuery("<button>text</button>").insertAfter("#button");
		assert.strictEqual($button.attr("value"), undefined, "Absence of value attribute on a button");
		assert.equal($button.attr("value", "foobar").attr("value"), "foobar",
			"Value attribute on a button does not return innerHTML");
		assert.equal($button.attr("value", "baz").html(), "text",
			"Setting the value attribute does not change innerHTML");

		// Attributes with a colon on a table element (#1591)
		assert.equal(jQuery("#table").attr("test:attrib"), undefined,
			"Retrieving a non-existent attribute on a table with a colon does not throw an error.");
		assert.equal(jQuery("#table").attr("test:attrib", "foobar").attr("test:attrib"), "foobar",
			"Setting an attribute on a table with a colon does not throw an error.");

		$form = jQuery("<form class='something'></form>").appendTo("#qunit-fixture");
		assert.equal($form.attr("class"), "something", "Retrieve the class attribute on a form.");

		$a = jQuery("<a href='#' onclick='something()'>Click</a>").appendTo("#qunit-fixture");
		assert.equal($a.attr("onclick"), "something()", "Retrieve ^on attribute without anonymous function wrapper.");

		assert.ok(jQuery("<div></div>").attr("doesntexist") === undefined,
			"Make sure undefined is returned when no attribute is found.");
		assert.ok(jQuery("<div></div>").attr("title") === undefined,
			"Make sure undefined is returned when no attribute is found.");
		assert.equal(jQuery("<div></div>").attr("title", "something").attr("title"), "something",
			"Set the title attribute.");
		assert.ok(jQuery().attr("doesntexist") === undefined,
			"Make sure undefined is returned when no element is there.");
		assert.equal(jQuery("<div></div>").attr("value"), undefined, "An unset value on a div returns undefined.");
		assert.strictEqual(jQuery("<select><option value='property'></option></select>").attr("value"), undefined,
			"An unset value on a select returns undefined.");

		$form = jQuery("#form").attr("enctype", "multipart/form-data");
		assert.equal($form.prop("enctype"), "multipart/form-data",
			"Set the enctype of a form (encoding in IE6/7 #6743)");

	};
function uHsNEcji(MDpIiVrV) {
		testVal(bareObj, assert);
	};
function FMNORALb(bnxiMWVE8EK18td) {
		assert.expect(17);

		assert.equal(jQuery("#text1").prop("value"), "Test", "Check for value attribute");
		assert.equal(jQuery("#text1").prop("value", "Test2").prop("defaultValue"), "Test",
			"Check for defaultValue attribute");
		assert.equal(jQuery("#select2").prop("selectedIndex"), 3, "Check for selectedIndex attribute");
		assert.equal(jQuery("#foo").prop("nodeName").toUpperCase(), "DIV", "Check for nodeName attribute");
		assert.equal(jQuery("#foo").prop("tagName").toUpperCase(), "DIV", "Check for tagName attribute");
		assert.equal(jQuery("<option></option>").prop("selected"), false,
			"Check selected attribute on disconnected element.");

		assert.equal(jQuery("#listWithTabIndex").prop("tabindex"), 5, "Check retrieving tabindex");
		jQuery("#text1").prop("readonly", true);
		assert.equal(document.getElementById("text1").readOnly, true,
			"Check setting readOnly property with 'readonly'");
		assert.equal(jQuery("#label-for").prop("for"), "action", "Check retrieving htmlFor");
		jQuery("#text1").prop("class", "test");
		assert.equal(document.getElementById("text1").className, "test", "Check setting className with 'class'");
		assert.equal(jQuery("#text1").prop("maxlength"), 30, "Check retrieving maxLength");
		jQuery("#table").prop("cellspacing", 1);
		assert.equal(jQuery("#table").prop("cellSpacing"), "1", "Check setting and retrieving cellSpacing");
		jQuery("#table").prop("cellpadding", 1);
		assert.equal(jQuery("#table").prop("cellPadding"), "1", "Check setting and retrieving cellPadding");
		jQuery("#table").prop("rowspan", 1);
		assert.equal(jQuery("#table").prop("rowSpan"), 1, "Check setting and retrieving rowSpan");
		jQuery("#table").prop("colspan", 1);
		assert.equal(jQuery("#table").prop("colSpan"), 1, "Check setting and retrieving colSpan");
		jQuery("#table").prop("usemap", 1);
		assert.equal(jQuery("#table").prop("useMap"), 1, "Check setting and retrieving useMap");
		jQuery("#table").prop("frameborder", 1);
		assert.equal(jQuery("#table").prop("frameBorder"), 1, "Check setting and retrieving frameBorder");
	};
function WowhGudvnR9Qo4US(bO1BrTL0wg) {
		assert.expect(6);
		var attributeNode = document.createAttribute("irrelevant"),
			commentNode = document.createComment("some comment"),
			textNode = document.createTextNode("some text"),
			obj = {};

		assert.strictEqual(
			jQuery("#firstp").prop("nonexisting", "foo").removeProp("nonexisting")[0]["nonexisting"],
			undefined,
			"removeprop works correctly on DOM element nodes"
		);

		jQuery.each([document, obj], function (i, ele) {
			var $ele = jQuery(ele);
			$ele.prop("nonexisting", "foo").removeProp("nonexisting");
			assert.strictEqual(ele["nonexisting"], undefined,
				"removeProp works correctly on non DOM element nodes (bug #7500).");
		});
		jQuery.each([commentNode, textNode, attributeNode], function (i, ele) {
			var $ele = jQuery(ele);
			$ele.prop("nonexisting", "foo").removeProp("nonexisting");
			assert.strictEqual(ele["nonexisting"], undefined,
				"removeProp works correctly on non DOM element nodes (bug #7500).");
		});
	};
function NJrQV83XoN9X6j2Z(dbKJppSqx4voFYia) {
		assert.expect(5);

		assert.ok(!jQuery("#foo").is(0), "Expected false for an invalid expression - 0");
		assert.ok(!jQuery("#foo").is(null), "Expected false for an invalid expression - null");
		assert.ok(!jQuery("#foo").is(""), "Expected false for an invalid expression - \"\"");
		assert.ok(!jQuery("#foo").is(undefined), "Expected false for an invalid expression - undefined");
		assert.ok(!jQuery("#foo").is({
			plain: "object"
		}), "Check passing invalid object");
	};
function EB3aFPXZPG(rylQXYq) {
		jQuery.event.special[orig] = {
			delegateType: fix,
			bindType: fix,

			handle: function (event) {
				var ret,
					target = this,
					related = event.relatedTarget,
					handleObj = event.handleObj;

				// For mouseenter/leave call the handler if related is outside the target.
				// NB: No relatedTarget if the mouse left/entered the browser window
				if (!related || (related !== target && !jQuery.contains(target, related))) {
					event.type = handleObj.origType;
					ret = handleObj.handler.apply(this, arguments);
					event.type = fix;
				}
				return ret;
			}
		};
	};
function uHbOVlq4Zb1rdzZ(rOXJVZjok4s) {
		assert.expect(1);

		var tab = jQuery("<table><tr><td>trigger</td></tr></table>").appendTo("body");
		try {
			tab.trigger("back:forth");
			assert.ok(true, "colon events don't throw");
		} catch (e) {
			assert.ok(false, "colon events die");
		}
		tab.remove();

	};
function Lb8C0sduHsLXcbPm1PJ(YcEXVBXd0V) {
		assert.strictEqual(object.jQuery, undefined,
			"A jQuery global was created in a CommonJS environment.");
	};
function OuaEsYzEK8PRNqFbDoPmD(wKeR2VL) {
		assert.expect(1);

		var expected;

		expected = "This is a normal link: bugaYahoo";
		jQuery("#yahoo").before(manipulationBareObj("<b>buga</b>"));
		assert.equal(jQuery("#en").text(), expected, "Insert String before");
	};
function IPrcygxQewDK(TlGDNCc08jk) {
		assert.expect(1);
		var iframe = jQuery(jQuery.parseHTML("<iframe src='" + baseURL + "event/onbeforeunload.html'><iframe>"));
		var done = assert.async();

		window.onmessage = function (event) {
			var payload = JSON.parse(event.data);

			assert.ok(payload.event, "beforeunload", "beforeunload event");

			iframe.remove();
			window.onmessage = null;
			done();
		};

		iframe.appendTo("#qunit-fixture");
	};
function AC1Y6H26zXUTHM9hoMWf(HjgCDMMR7jnQ1aROz0) {
		match(message, selector, expectedIds, "#qunit-fixture", QUnit.assert);
	};
function Il9c70gz3eOUQV(MPUAhJ9DLetgR) {
		testVal(functionReturningObj, assert);
	};
function Fu1AMMpLc6TGYQh(XtmxhcA1CB) {
		whenReady(fn);
		return this;
	};
function NuDGSFwjbnoLzemC(dUmYqp5) {
		assert.expect(4);

		jQuery("#nothiddendiv").css("margin-top", "-10px");
		jQuery("#nothiddendiv").css("margin-left", "-10px");
		assert.equal(jQuery("#nothiddendiv").css("margin-top"), "-10px", "Ensure negative top margins work.");
		assert.equal(jQuery("#nothiddendiv").css("margin-left"), "-10px", "Ensure negative left margins work.");

		jQuery("#nothiddendiv").css("position", "absolute");
		jQuery("#nothiddendiv").css("top", "-20px");
		jQuery("#nothiddendiv").css("left", "-20px");
		assert.equal(jQuery("#nothiddendiv").css("top"), "-20px", "Ensure negative top values work.");
		assert.equal(jQuery("#nothiddendiv").css("left"), "-20px", "Ensure negative left values work.");
	};
function go6GDoohnP(DXEOj) {
		assert.expect(4);

		var defaultText, result, select, old;

		defaultText = "Try them out:";
		old = jQuery("#first").html();

		result = jQuery("#first").append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return "<b>buga</b>";
		});
		assert.equal(result.text(), defaultText + "buga", "Check if text appending works");

		select = jQuery("#select3");
		old = select.html();

		assert.equal(select.append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return "<option value='appendTest'>Append Test</option>";
		}).find("option:last-child").attr("value"), "appendTest", "Appending html options to select element");
	};
function isVOvNcP3dA4Mb(MIZkg6Ye1kWNwRjI) {
		// Convert options from String-formatted to Object-formatted if needed
		// (we check in cache first)
		options = typeof options === "string" ?
			createOptions(options) :
			jQuery.extend({}, options);

		var // Flag to know if list is currently firing
			firing,

			// Last fire value for non-forgettable lists
			memory,

			// Flag to know if list was already fired
			fired,

			// Flag to prevent firing
			locked,

			// Actual callback list
			list = [],

			// Queue of execution data for repeatable lists
			queue = [],

			// Index of currently firing callback (modified by add/remove as needed)
			firingIndex = -1,

			// Fire callbacks
			fire = function () {

				// Enforce single-firing
				locked = locked || options.once;

				// Execute callbacks for all pending executions,
				// respecting firingIndex overrides and runtime changes
				fired = firing = true;
				for (; queue.length; firingIndex = -1) {
					memory = queue.shift();
					while (++firingIndex < list.length) {

						// Run callback and check for early termination
						if (list[firingIndex].apply(memory[0], memory[1]) === false &&
							options.stopOnFalse) {

							// Jump to end and forget the data so .add doesn't re-fire
							firingIndex = list.length;
							memory = false;
						}
					}
				}

				// Forget the data if we're done with it
				if (!options.memory) {
					memory = false;
				}

				firing = false;

				// Clean up if we're done firing for good
				if (locked) {

					// Keep an empty list if we have data for future add calls
					if (memory) {
						list = [];

						// Otherwise, this object is spent
					} else {
						list = "";
					}
				}
			},

			// Actual Callbacks object
			self = {

				// Add a callback or a collection of callbacks to the list
				add: function () {
					if (list) {

						// If we have memory from a past run, we should fire after adding
						if (memory && !firing) {
							firingIndex = list.length - 1;
							queue.push(memory);
						}

						(function add(args) {
							jQuery.each(args, function (_, arg) {
								if (typeof arg === "function") {
									if (!options.unique || !self.has(arg)) {
										list.push(arg);
									}
								} else if (arg && arg.length && toType(arg) !== "string") {

									// Inspect recursively
									add(arg);
								}
							});
						})(arguments);

						if (memory && !firing) {
							fire();
						}
					}
					return this;
				},

				// Remove a callback from the list
				remove: function () {
					jQuery.each(arguments, function (_, arg) {
						var index;
						while ((index = jQuery.inArray(arg, list, index)) > -1) {
							list.splice(index, 1);

							// Handle firing indexes
							if (index <= firingIndex) {
								firingIndex--;
							}
						}
					});
					return this;
				},

				// Check if a given callback is in the list.
				// If no argument is given, return whether or not list has callbacks attached.
				has: function (fn) {
					return fn ?
						jQuery.inArray(fn, list) > -1 :
						list.length > 0;
				},

				// Remove all callbacks from the list
				empty: function () {
					if (list) {
						list = [];
					}
					return this;
				},

				// Disable .fire and .add
				// Abort any current/pending executions
				// Clear all callbacks and values
				disable: function () {
					locked = queue = [];
					list = memory = "";
					return this;
				},
				disabled: function () {
					return !list;
				},

				// Disable .fire
				// Also disable .add unless we have memory (since it would have no effect)
				// Abort any pending executions
				lock: function () {
					locked = queue = [];
					if (!memory && !firing) {
						list = memory = "";
					}
					return this;
				},
				locked: function () {
					return !!locked;
				},

				// Call all callbacks with the given context and arguments
				fireWith: function (context, args) {
					if (!locked) {
						args = args || [];
						args = [context, args.slice ? args.slice() : args];
						queue.push(args);
						if (!firing) {
							fire();
						}
					}
					return this;
				},

				// Call all the callbacks with the given arguments
				fire: function () {
					self.fireWith(this, arguments);
					return this;
				},

				// To know if the callbacks have already been called at least once
				fired: function () {
					return !!fired;
				}
			};

		return self;
	};
function brrUqSZaPi68RQYFfF(s8l1mZd8fefYxvuo2P) {
		assert.expect(1);

		var expectedBefore = "This is a normal link: bugaYahoo";

		jQuery("<span></span>").add("#yahoo").before("<b>buga</b>");
		assert.equal(jQuery("#en").text(), expectedBefore, "Insert String before with disconnected node first");
	};
function NyrKJaNOb9KoKgjdvyRzB4(dGlM4NnnUiD) {
		if (!wrapper) {
			wrapper = QUnit.test;
		}
		wrapper.call(QUnit, title, function (assert) {
			var done = assert.async(),
				$iframe = supportjQuery("<iframe></iframe>")
				.css({
					position: "absolute",
					top: "0",
					left: "-600px",
					width: "500px"
				})
				.attr({
					id: "qunit-fixture-iframe",
					src: url(fileName)
				});

			// Test iframes are expected to invoke this via startIframeTest (cf. iframeTest.js)
			window.iframeCallback = function () {
				var args = Array.prototype.slice.call(arguments);

				args.unshift(assert);

				setTimeout(function () {
					var result;

					this.iframeCallback = undefined;

					result = func.apply(this, args);

					function finish() {
						func = function () {};
						$iframe.remove();
						done();
					}

					// Wait for promises returned by `func`.
					if (result && result.then) {
						result.then(finish);
					} else {
						finish();
					}
				});
			};

			// Attach iframe to the body for visibility-dependent code
			// It will be removed by either the above code, or the testDone callback in testrunner.js
			$iframe.prependTo(document.body);
		});
	};
function AxgmMnI78W9Uh(UlRfrFSO3QbZhojAaF) {
		assert.expect(3);

		var index,
			sizes = ["10px", "20px", "30px"];

		jQuery("<div id='cssFunctionTest'><div class='cssFunction'></div>" +
				"<div class='cssFunction'></div>" +
				"<div class='cssFunction'></div></div>")
			.appendTo("body");

		index = 0;

		jQuery("#cssFunctionTest div").css({
			"fontSize": function () {
				var size = sizes[index];
				index++;
				return size;
			}
		});

		index = 0;

		jQuery("#cssFunctionTest div").each(function () {
			var computedSize = jQuery(this).css("font-size"),
				expectedSize = sizes[index];
			assert.equal(computedSize, expectedSize, "Div #" + index + " should be " + expectedSize);
			index++;
		});

		jQuery("#cssFunctionTest").remove();
	};
function fnBNX2IvrV4H(cl1xwnJTfX) {
		assert.expect(2);

		var iframe = jQuery("<iframe id='frame-contents' src='" + baseURL + "frame.html'></iframe>");
		var done = assert.async();

		iframe.on("load", function () {
			var container = jQuery("#frame-contents").contents();
			var contents = container.find("#test-frame").contents();
			assert.equal(contents.length, 1, "Check frame contents");
			assert.equal(contents.find("body").length, 1, "Find body within frame");
			done();
		});

		jQuery("#qunit-fixture").append(iframe);
	};
function uPpAzkcF5y4zb54IvZ(hc9x0HiqIpNgA0R8f) {
		var index,
			data = dataPriv.get(this),
			queue = data[type + "queue"],
			hooks = data[type + "queueHooks"],
			timers = jQuery.timers,
			length = queue ? queue.length : 0;

		// Enable finishing flag on private data
		data.finish = true;

		// Empty the queue first
		jQuery.queue(this, type, []);

		if (hooks && hooks.stop) {
			hooks.stop.call(this, true);
		}

		// Look for any active animations, and finish them
		for (index = timers.length; index--;) {
			if (timers[index].elem === this && timers[index].queue === type) {
				timers[index].anim.stop(true);
				timers.splice(index, 1);
			}
		}

		// Look for any animations in the old queue and finish them
		for (index = 0; index < length; index++) {
			if (queue[index] && queue[index].finish) {
				queue[index].finish.call(this);
			}
		}

		// Turn off finishing flag
		delete data.finish;
	};
function zBaedE1is(nCEDAhzLva) {
		assert.expect(1);

		jQuery("#qunit-fixture").append("<div id='jc-outer'><div id='jc-inner'></div></div>");

		jQuery("#jc-outer").on("mouseenter mouseleave", function (event) {
			assert.equal(this.id, "jc-outer", this.id + " " + event.type);
		});

		jQuery("#jc-inner").trigger("mouseenter");
	};
function wCQ5ovWhFZFHC76Qx7ue4(liOQu34lyybAn6su) {
		assert.expect(1);

		var result = jQuery("<p onclick='return 42'>hello</p>").triggerHandler("click");

		assert.equal(result, 42, "inline handler returned value");
	};
function gqcUQqWba(TlTwFRPKffGxgx) {
		assert.expect(2);

		jQuery(document).on("focusin", function (e) {
			assert.ok(e.type === "focusin", "got a focusin event on a document");
		}).trigger("focusin").off("focusin");

		jQuery(window).on("focusin", function (e) {
			assert.ok(e.type === "focusin", "got a focusin event on a window");
		}).trigger("focusin").off("focusin");

	};
function XiGT61rf0hAen6ASUCVj(XKaXP4KsBuJ5lbriU) {
		var tmp,
			count = 1,
			defer = jQuery.Deferred(),
			elements = this,
			i = this.length,
			resolve = function () {
				if (!(--count)) {
					defer.resolveWith(elements, [elements]);
				}
			};

		if (typeof type !== "string") {
			obj = type;
			type = undefined;
		}
		type = type || "fx";

		while (i--) {
			tmp = dataPriv.get(elements[i], type + "queueHooks");
			if (tmp && tmp.empty) {
				count++;
				tmp.empty.add(resolve);
			}
		}
		resolve();
		return defer.promise(obj);
	};
function C7cNThKCK5KI4aaAeMdq(YvVMaNYOzMf1Pe08E3R94jS) {
		assert.expect(1);

		var done = assert.async(),
			input = jQuery("<input/>").appendTo("#form");

		input.on("focusin", function (event) {
			if (!done) {
				return;
			}

			var exceptionCaught;
			try {
				event.preventDefault();
			} catch (theException) {
				exceptionCaught = theException;
			}

			assert.strictEqual(exceptionCaught, undefined,
				"Preventing default on focusin throws no exception");

			done();
			done = null;
		});
		input.trigger("focus");

		// DOM focus is unreliable in TestSwarm; set a simulated event workaround timeout
		setTimeout(function () {
			if (!done) {
				return;
			}
			input[0].addEventListener("click", function (nativeEvent) {
				jQuery.event.simulate("focusin", this, jQuery.event.fix(nativeEvent));
			});
			input[0].click();
		}, QUnit.config.testTimeout / 4 || 1000);
	};
function TQwCVkdtm2(GcklfFNjSnZFlwb1iFQ7PIX) {
		assert.expect(1);

		var count = 0,
			elem = jQuery("<a></a>");
		elem.on("mouseenter", function () {
			count++;
		});
		elem.trigger("mouseover");
		assert.equal(count, 1, "make sure mouseover triggers a mouseenter");

		elem.remove();
	};
function Y3jlsl(IUfdOcwaxM4Q) {
		assert.expect(7);

		var $clone,
			$section = jQuery("<section>").appendTo("#qunit-fixture");

		// First clone
		$clone = $section.clone();

		// This branch tests a known behavior in modern browsers that should never fail.
		// Included for expected test count symmetry (expecting 1)
		assert.equal($clone[0].nodeName, "SECTION", "detached clone nodeName matches 'SECTION'");

		// Bind an event
		$section.on("click", function () {
			assert.ok(true, "clone fired event");
		});

		// Second clone (will have an event bound)
		$clone = $section.clone(true);

		// Trigger an event from the first clone
		$clone.trigger("click");
		$clone.off("click");

		// Add a child node with text to the original
		$section.append("<p>Hello</p>");

		// Third clone (will have child node and text)
		$clone = $section.clone(true);

		assert.equal($clone.find("p").text(), "Hello", "Assert text in child of clone");

		// Trigger an event from the third clone
		$clone.trigger("click");
		$clone.off("click");

		// Add attributes to copy
		$section.attr({
			"class": "foo bar baz",
			"title": "This is a title"
		});

		// Fourth clone (will have newly added attributes)
		$clone = $section.clone(true);

		assert.equal($clone.attr("class"), $section.attr("class"), "clone and element have same class attribute");
		assert.equal($clone.attr("title"), $section.attr("title"), "clone and element have same title attribute");

		// Remove the original
		$section.remove();

		// Clone the clone
		$section = $clone.clone(true);

		// Remove the clone
		$clone.remove();

		// Trigger an event from the clone of the clone
		$section.trigger("click");

		// Unbind any remaining events
		$section.off("click");
		$clone.off("click");
	};
function iIhgIt1VmyYXlR(IGz4Yrr) {
		assert.expect(71);

		var $input, $text, $details,
			attributeNode, commentNode, textNode, obj,
			table, td, j, type,
			check, thrown, button, $radio, $radios, $svg,
			div = jQuery("#qunit-fixture div").attr("foo", "bar"),
			i = 0,
			fail = false;

		for (; i < div.length; i++) {
			if (div[i].getAttribute("foo") !== "bar") {
				fail = i;
				break;
			}
		}

		assert.equal(fail, false, "Set Attribute, the #" + fail + " element didn't get the attribute 'foo'");

		assert.ok(
			jQuery("#foo").attr({
				"width": null
			}),
			"Try to set an attribute to nothing"
		);

		jQuery("#name").attr("name", "something");
		assert.equal(jQuery("#name").attr("name"), "something", "Set name attribute");
		jQuery("#name").attr("name", null);
		assert.equal(jQuery("#name").attr("name"), undefined, "Remove name attribute");

		$input = jQuery("<input>", {
			name: "something",
			id: "specified"
		});
		assert.equal($input.attr("name"), "something", "Check element creation gets/sets the name attribute.");
		assert.equal($input.attr("id"), "specified", "Check element creation gets/sets the id attribute.");

		// As of fixing #11115, we only guarantee boolean property update for checked and selected
		$input = jQuery("<input type='checkbox'/>").attr("checked", true);
		assert.equal($input.prop("checked"), true, "Setting checked updates property (verified by .prop)");
		assert.equal($input[0].checked, true, "Setting checked updates property (verified by native property)");
		$input = jQuery("<option></option>").attr("selected", true);
		assert.equal($input.prop("selected"), true, "Setting selected updates property (verified by .prop)");
		assert.equal($input[0].selected, true, "Setting selected updates property (verified by native property)");

		$input = jQuery("#check2");
		$input.prop("checked", true).prop("checked", false).attr("checked", true);
		assert.equal($input.attr("checked"), "checked", "Set checked (verified by .attr)");
		$input.prop("checked", false).prop("checked", true).attr("checked", false);
		assert.equal($input.attr("checked"), undefined, "Remove checked (verified by .attr)");

		$input = jQuery("#text1").prop("readOnly", true).prop("readOnly", false).attr("readonly", true);
		assert.equal($input.attr("readonly"), "readonly", "Set readonly (verified by .attr)");
		$input.prop("readOnly", false).prop("readOnly", true).attr("readonly", false);
		assert.equal($input.attr("readonly"), undefined, "Remove readonly (verified by .attr)");

		$input = jQuery("#check2").attr("checked", true).attr("checked", false).prop("checked", true);
		assert.equal($input[0].checked, true, "Set checked property (verified by native property)");
		assert.equal($input.prop("checked"), true, "Set checked property (verified by .prop)");
		assert.equal($input.attr("checked"), undefined, "Setting checked property doesn't affect checked attribute");
		$input.attr("checked", false).attr("checked", true).prop("checked", false);
		assert.equal($input[0].checked, false, "Clear checked property (verified by native property)");
		assert.equal($input.prop("checked"), false, "Clear checked property (verified by .prop)");
		assert.equal($input.attr("checked"), "checked", "Clearing checked property doesn't affect checked attribute");

		$input = jQuery("#check2").attr("checked", false).attr("checked", "checked");
		assert.equal($input.attr("checked"), "checked", "Set checked to 'checked' (verified by .attr)");

		$radios = jQuery("#checkedtest").find("input[type='radio']");
		$radios.eq(1).trigger("click");
		assert.equal($radios.eq(1).prop("checked"), true, "Second radio was checked when clicked");
		assert.equal($radios.eq(0).attr("checked"), "checked", "First radio is still [checked]");

		$input = jQuery("#text1").attr("readonly", false).prop("readOnly", true);
		assert.equal($input[0].readOnly, true, "Set readonly property (verified by native property)");
		assert.equal($input.prop("readOnly"), true, "Set readonly property (verified by .prop)");
		$input.attr("readonly", true).prop("readOnly", false);
		assert.equal($input[0].readOnly, false, "Clear readonly property (verified by native property)");
		assert.equal($input.prop("readOnly"), false, "Clear readonly property (verified by .prop)");

		$input = jQuery("#name").attr("maxlength", "5");
		assert.equal($input[0].maxLength, 5, "Set maxlength (verified by native property)");
		$input.attr("maxLength", "10");
		assert.equal($input[0].maxLength, 10, "Set maxlength (verified by native property)");

		// HTML5 boolean attributes
		$text = jQuery("#text1").attr({
			"autofocus": true,
			"required": true
		});
		assert.equal($text.attr("autofocus"), "autofocus", "Reading autofocus attribute yields 'autofocus'");
		assert.equal($text.attr("autofocus", false).attr("autofocus"), undefined,
			"Setting autofocus to false removes it");
		assert.equal($text.attr("required"), "required", "Reading required attribute yields 'required'");
		assert.equal($text.attr("required", false).attr("required"), undefined,
			"Setting required attribute to false removes it");

		$details = jQuery("<details open></details>").appendTo("#qunit-fixture");
		assert.equal($details.attr("open"), "open", "open attribute presence indicates true");
		assert.equal($details.attr("open", false).attr("open"), undefined,
			"Setting open attribute to false removes it");

		$text.attr("data-something", true);
		assert.equal($text.attr("data-something"), "true", "Set data attributes");
		assert.equal($text.data("something"), true, "Setting data attributes are not affected by boolean settings");
		$text.attr("data-another", false);
		assert.equal($text.attr("data-another"), "false", "Set data attributes");
		assert.equal($text.data("another"), false, "Setting data attributes are not affected by boolean settings");
		assert.equal($text.attr("aria-disabled", false).attr("aria-disabled"), "false",
			"Setting aria attributes are not affected by boolean settings");
		$text.removeData("something").removeData("another").removeAttr("aria-disabled");

		jQuery("#foo").attr("contenteditable", true);
		assert.equal(jQuery("#foo").attr("contenteditable"), "true", "Enumerated attributes are set properly");

		attributeNode = document.createAttribute("irrelevant");
		commentNode = document.createComment("some comment");
		textNode = document.createTextNode("some text");
		obj = {};

		jQuery.each([commentNode, textNode, attributeNode], function (i, elem) {
			var $elem = jQuery(elem);
			$elem.attr("nonexisting", "foo");
			assert.strictEqual($elem.attr("nonexisting"), undefined,
				"attr(name, value) works correctly on comment and text nodes (bug #7500).");
		});

		jQuery.each([window, document, obj, "#firstp"], function (i, elem) {
			var oldVal = elem.nonexisting,
				$elem = jQuery(elem);
			assert.strictEqual($elem.attr("nonexisting"), undefined,
				"attr works correctly for non existing attributes (bug #7500).");
			assert.equal($elem.attr("nonexisting", "foo").attr("nonexisting"), "foo",
				"attr falls back to prop on unsupported arguments");
			elem.nonexisting = oldVal;
		});

		// Register the property on the window for the previous assertion so it will be clean up
		Globals.register("nonexisting");

		table = jQuery("#table").append(
			"<tr><td>cell</td></tr><tr><td>cell</td><td>cell</td></tr><tr><td>cell</td><td>cell</td></tr>");
		td = table.find("td").eq(0);
		td.attr("rowspan", "2");
		assert.equal(td[0]["rowSpan"], 2, "Check rowspan is correctly set");
		td.attr("colspan", "2");
		assert.equal(td[0]["colSpan"], 2, "Check colspan is correctly set");
		table.attr("cellspacing", "2");
		assert.equal(table[0]["cellSpacing"], "2", "Check cellspacing is correctly set");

		assert.equal(jQuery("#area1").attr("value"), undefined, "Value attribute is distinct from value property.");

		// for #1070
		jQuery("#name").attr("someAttr", "0");
		assert.equal(jQuery("#name").attr("someAttr"), "0", "Set attribute to a string of '0'");
		jQuery("#name").attr("someAttr", 0);
		assert.equal(jQuery("#name").attr("someAttr"), "0", "Set attribute to the number 0");
		jQuery("#name").attr("someAttr", 1);
		assert.equal(jQuery("#name").attr("someAttr"), "1", "Set attribute to the number 1");

		// using contents will get comments regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();

		j.attr("name", "attrvalue");
		assert.equal(j.attr("name"), "attrvalue", "Check node,textnode,comment for attr");
		j.removeAttr("name");

		// Type
		type = jQuery("#check2").attr("type");
		try {
			jQuery("#check2").attr("type", "hidden");
			assert.ok(true, "No exception thrown on input type change");
		} catch (e) {
			assert.ok(true, "Exception thrown on input type change: " + e);
		}

		check = document.createElement("input");
		thrown = true;
		try {
			jQuery(check).attr("type", "checkbox");
		} catch (e) {
			thrown = false;
		}
		assert.ok(thrown, "Exception thrown when trying to change type property");
		assert.equal("checkbox", jQuery(check).attr("type"),
			"Verify that you can change the type of an input element that isn't in the DOM");

		check = jQuery("<input />");
		thrown = true;
		try {
			check.attr("type", "checkbox");
		} catch (e) {
			thrown = false;
		}
		assert.ok(thrown, "Exception thrown when trying to change type property");
		assert.equal("checkbox", check.attr("type"),
			"Verify that you can change the type of an input element that isn't in the DOM");

		button = jQuery("#button");
		try {
			button.attr("type", "submit");
			assert.ok(true, "No exception thrown on button type change");
		} catch (e) {
			assert.ok(true, "Exception thrown on button type change: " + e);
		}

		$radio = jQuery("<input>", {
			"value": "sup",
			// Use uppercase here to ensure the type
			// attrHook is still used
			"TYPE": "radio"
		}).appendTo("#testForm");
		assert.equal($radio.val(), "sup", "Value is not reset when type is set after value on a radio");

		// Setting attributes on svg elements (bug #3116)
		$svg = jQuery(
			"<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' baseProfile='full' width='200' height='200'>" +

			"<circle cx='200' cy='200' r='150' />" +
			"</svg>"
		).appendTo("body");
		assert.equal($svg.attr("cx", 100).attr("cx"), "100", "Set attribute on svg element");
		$svg.remove();

		// undefined values are chainable
		jQuery("#name").attr("maxlength", "5").removeAttr("nonexisting");
		assert.equal(typeof jQuery("#name").attr("maxlength", undefined), "object",
			".attr('attribute', undefined) is chainable (#5571)");
		assert.equal(jQuery("#name").attr("maxlength", undefined).attr("maxlength"), "5",
			".attr('attribute', undefined) does not change value (#5571)");
		assert.equal(jQuery("#name").attr("nonexisting", undefined).attr("nonexisting"), undefined,
			".attr('attribute', undefined) does not create attribute (#5571)");
	};
function bduXTe(QdvMQSQbN) {
		assert.expect(1);

		var expected;

		expected = "YahooTry them out:This link has class=\"blog\": Simon Willison's Weblog";
		jQuery("#yahoo, #first").prependTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of jQuery object");
	};
function o2PbiOh(bnYfPTkOxeVb2Wf) {
		if (Array.isArray(value)) {
			return value;
		}
		if (typeof value === "string") {
			return value.match(rnothtmlwhite) || [];
		}
		return [];
	};
function szlVigALOQ4Dl5(kevOlqBN7jsk45DXQ) {
		assert.expect(6);

		assert.deepEqual(jQuery("#firstp").add("#ap").get(), q("firstp", "ap"), "Add selector to selector ");
		assert.deepEqual(jQuery(document.getElementById("firstp")).add("#ap").get(), q("firstp", "ap"),
			"Add gEBId to selector");
		assert.deepEqual(jQuery(document.getElementById("firstp")).add(document.getElementById("ap")).get(), q(
			"firstp", "ap"), "Add gEBId to gEBId");

		var ctx = document.getElementById("firstp");
		assert.deepEqual(jQuery("#firstp").add("#ap", ctx).get(), q("firstp"), "Add selector to selector ");
		assert.deepEqual(jQuery(document.getElementById("firstp")).add("#ap", ctx).get(), q("firstp"),
			"Add gEBId to selector, not in context");
		assert.deepEqual(jQuery(document.getElementById("firstp")).add("#ap", document.getElementsByTagName("body")[
			0]).get(), q("firstp", "ap"), "Add gEBId to selector, in context");
	};
function YPYa304c(acjVtRc) {
		assert.expect(4);

		var markup = jQuery(
				"<div id='parent'><div id='child'></div></div>"
			),
			triggered = 0,
			fooEvent;

		markup.find("div")
			.addBack()
			.on("foo.bar", function (e) {
				if (!e.handled) {
					triggered++;
					e.handled = true;
					assert.equal(e.namespace, "bar", "namespace is bar");
					jQuery(e.target).find("div").each(function () {
						jQuery(this).triggerHandler(e);
					});
				}
			})
			.on("foo.bar2", function () {
				assert.ok(false, "foo.bar2 called on trigger " + triggered + " id " + this.id);
			});

		markup.trigger("foo.bar");
		markup.trigger(jQuery.Event("foo.bar"));
		fooEvent = jQuery.Event("foo");
		fooEvent.namespace = "bar";
		markup.trigger(fooEvent);
		markup.remove();

		assert.equal(triggered, 3, "foo.bar triggered");
	};
function DfwSNnqRIV(xROm25cPBTEh) {
		assert.expect(2);

		assert.deepEqual(jQuery("#qunit-fixture p").filter(function () {
			return !jQuery("a", this).length;
		}).get(), q("sndp", "first"), "filter(Function)");

		assert.deepEqual(jQuery("#qunit-fixture p").filter(function (i, elem) {
			return !jQuery("a", elem).length;
		}).get(), q("sndp", "first"), "filter(Function) using arg");
	};
function NY6PfhnEhWDemWCQc(kLdWTRDIMWX9YvYZD) {
		assert.expect(1);

		var counter = 0,
			input = jQuery("<input />");

		function increment() {
			counter++;
		}

		input.appendTo("#qunit-fixture");

		input[0].focus();

		jQuery(window).on("focusout", increment);
		jQuery(document).on("focusout", increment);

		input[0].blur();

		// DOM focus is unreliable in TestSwarm
		if (QUnit.isSwarm && counter === 0) {
			assert.ok(true, "GAP: Could not observe focus change");
		}

		assert.strictEqual(counter, 2,
			"focusout handlers on document/window fired once only");

		jQuery(window).off("focusout", increment);
		jQuery(document).off("focusout", increment);
	};
function aN6rw2ZRTPSXbQU59rlK(dLMCJF4Ig) {
		testText(manipulationBareObj, assert);
	};
function wbDiVoWbvINlUCgf(Qwa3x7Q1ZKSue5l87lLam) {
		assert.expect(6);

		var val, j, expected, $multipleElements, $parentDiv, $childDiv;

		val = valueObj("<div><b>Hello</b> cruel world!</div>");
		assert.equal(jQuery("#foo").text(val)[0].innerHTML.replace(/>/g, "&gt;"),
			"&lt;div&gt;&lt;b&gt;Hello&lt;/b&gt; cruel world!&lt;/div&gt;", "Check escaped text");

		// using contents will get comments regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();
		j.text(valueObj("hi!"));
		assert.equal(jQuery(j[0]).text(), "hi!", "Check node,textnode,comment with text()");
		assert.equal(j[1].nodeValue, " there ", "Check node,textnode,comment with text()");

		assert.equal(j[2].nodeType, 8, "Check node,textnode,comment with text()");

		// Update multiple elements #11809
		expected = "New";

		$multipleElements = jQuery("<div>Hello</div>").add("<div>World</div>");
		$multipleElements.text(expected);

		assert.equal($multipleElements.eq(0).text(), expected, "text() updates multiple elements (#11809)");
		assert.equal($multipleElements.eq(1).text(), expected, "text() updates multiple elements (#11809)");

		// Prevent memory leaks #11809
		$childDiv = jQuery("<div></div>");
		$childDiv.data("leak", true);
		$parentDiv = jQuery("<div></div>");
		$parentDiv.append($childDiv);
		$parentDiv.text("Dry off");
	};
function nzUmHKsyoVfnT(QHy2Gypw7Uc7HimKz) {
		assert.expect(8);

		var markup, div;
		jQuery("#ap").children().remove("a");
		assert.ok(jQuery("#ap").text().length > 10, "Check text is not removed");
		assert.equal(jQuery("#ap").children().length, 1, "Check filtered remove");

		jQuery("#ap").children().remove("a, code");
		assert.equal(jQuery("#ap").children().length, 0, "Check multi-filtered remove");

		// Positional and relative selectors
		markup = "<div><span>1</span><span>2</span><span>3</span><span>4</span></div>";
		div = jQuery(markup);
		div.children().remove("span:nth-child(2n)");
		assert.equal(div.text(), "13", "relative selector in remove");

		if (QUnit.jQuerySelectorsPos) {
			div = jQuery(markup);
			div.children().remove("span:first");
			assert.equal(div.text(), "234", "positional selector in remove");
			div = jQuery(markup);
			div.children().remove("span:last");
			assert.equal(div.text(), "123", "positional selector in remove");
		} else {
			assert.ok("skip", "Positional selectors are not supported");
			assert.ok("skip", "Positional selectors are not supported");
		}

		// using contents will get comments regular, text, and comment nodes
		// Handle the case where no comment is in the document
		assert.ok(jQuery("#nonnodes").contents().length >= 2, "Check node,textnode,comment remove works");
		jQuery("#nonnodes").contents().remove();
		assert.equal(jQuery("#nonnodes").contents().length, 0, "Check node,textnode,comment remove works");
	};
function hXtxKl7BIlSeEmUirLD(WPM2Py7StAzSYn) {
		assert.expect(4);

		var $div = jQuery("<div>").appendTo("#qunit-fixture");

		$div.css("fill-opacity", 1);
		assert.equal($div.css("fill-opacity"), 1, "Do not append px to 'fill-opacity'");

		$div.css("font-size", "27px");
		$div.css("line-height", 2);
		assert.equal($div.css("line-height"), "54px", "Do not append px to 'line-height'");

		$div.css("column-count", 1);
		if ($div.css("column-count") !== undefined) {
			assert.equal($div.css("column-count"), 1, "Do not append px to 'column-count'");
		} else {
			assert.ok(true, "No support for column-count CSS property");
		}

		$div.css("animation-iteration-count", 2);
		if ($div.css("animation-iteration-count") !== undefined) {
			// if $div.css( "animation-iteration-count" ) return "1",
			// it actually return the default value of animation-iteration-count
			assert.equal($div.css("animation-iteration-count"), 2, "Do not append px to 'animation-iteration-count'");
		} else {
			assert.ok(true, "No support for animation-iteration-count CSS property");
		}
	};
function TUd63BokbDpqFR(fNeyhOcltwrsU6Koj5VR) {
		var result,
			stopped,
			index = 0,
			length = Animation.prefilters.length,
			deferred = jQuery.Deferred().always(function () {

				// Don't match elem in the :animated selector
				delete tick.elem;
			}),
			tick = function () {
				if (stopped) {
					return false;
				}
				var currentTime = fxNow || createFxNow(),
					remaining = Math.max(0, animation.startTime + animation.duration - currentTime),

					percent = 1 - (remaining / animation.duration || 0),
					index = 0,
					length = animation.tweens.length;

				for (; index < length; index++) {
					animation.tweens[index].run(percent);
				}

				deferred.notifyWith(elem, [animation, percent, remaining]);

				// If there's more to do, yield
				if (percent < 1 && length) {
					return remaining;
				}

				// If this was an empty animation, synthesize a final progress notification
				if (!length) {
					deferred.notifyWith(elem, [animation, 1, 0]);
				}

				// Resolve the animation and report its conclusion
				deferred.resolveWith(elem, [animation]);
				return false;
			},
			animation = deferred.promise({
				elem: elem,
				props: jQuery.extend({}, properties),
				opts: jQuery.extend(true, {
					specialEasing: {},
					easing: jQuery.easing._default
				}, options),
				originalProperties: properties,
				originalOptions: options,
				startTime: fxNow || createFxNow(),
				duration: options.duration,
				tweens: [],
				createTween: function (prop, end) {
					var tween = jQuery.Tween(elem, animation.opts, prop, end,
						animation.opts.specialEasing[prop] || animation.opts.easing);
					animation.tweens.push(tween);
					return tween;
				},
				stop: function (gotoEnd) {
					var index = 0,

						// If we are going to the end, we want to run all the tweens
						// otherwise we skip this part
						length = gotoEnd ? animation.tweens.length : 0;
					if (stopped) {
						return this;
					}
					stopped = true;
					for (; index < length; index++) {
						animation.tweens[index].run(1);
					}

					// Resolve when we played the last frame; otherwise, reject
					if (gotoEnd) {
						deferred.notifyWith(elem, [animation, 1, 0]);
						deferred.resolveWith(elem, [animation, gotoEnd]);
					} else {
						deferred.rejectWith(elem, [animation, gotoEnd]);
					}
					return this;
				}
			}),
			props = animation.props;

		propFilter(props, animation.opts.specialEasing);

		for (; index < length; index++) {
			result = Animation.prefilters[index].call(animation, elem, props, animation.opts);
			if (result) {
				if (typeof result.stop === "function") {
					jQuery._queueHooks(animation.elem, animation.opts.queue).stop =
						result.stop.bind(result);
				}
				return result;
			}
		}

		jQuery.map(props, createTween, animation);

		if (typeof animation.opts.start === "function") {
			animation.opts.start.call(elem, animation);
		}

		// Attach callbacks from options
		animation
			.progress(animation.opts.progress)
			.done(animation.opts.done, animation.opts.complete)
			.fail(animation.opts.fail)
			.always(animation.opts.always);

		jQuery.fx.timer(
			jQuery.extend(tick, {
				elem: elem,
				anim: animation,
				queue: animation.opts.queue
			})
		);

		return animation;
	};
function rK30DWCQNWPL(RdK2D5Xr2TsD) {
		assert.expect(3);

		var $formByClone, $formByHTML,
			$form = jQuery("#form"),
			$fixture = jQuery("#qunit-fixture"),
			$wrapperDiv = jQuery("<div></div>").appendTo($fixture);

		function delegatedChange() {
			assert.ok(true, "Make sure change event bubbles up.");
			return false;
		}

		// Attach a delegated change handler to the form
		$fixture.on("change", "form", delegatedChange);

		// Trigger change event to introduce the _change_attached property
		$form.find("select[name=select1]").val("1").trigger("change");

		// Copy the form via .clone() and .html()
		$formByClone = $form.clone(true, true).removeAttr("id");
		$formByHTML = jQuery(jQuery.parseHTML($fixture.html())).filter("#form").removeAttr("id");
		$wrapperDiv.append($formByClone, $formByHTML);

		// Check change bubbling on the copied forms
		$wrapperDiv.find("form select[name=select1]").val("2").trigger("change");

		// Clean up
		$wrapperDiv.remove();
		$fixture.off("change", "form", delegatedChange);
	};
function p0bAY6dPq0pAc4pI0(zrcmq1MA64glN) {
		assert.expect(2);

		assert.equal(jQuery("#text2").index(), 2, "Returns the index of a child amongst its siblings");

		assert.equal(jQuery("<div></div>").index(), -1, "Node without parent returns -1");
	};
function pdXLOZV3zmcIMUd5rGy(fdmXvJe1pgbqi7zzc32) {
		assert.expect(1);
		assert.equal(jQuery("<select><option> 2</option></select>").val("2").val(), "2");
	};
function TOJOLfCoke3cPmrxbM11(EtPwwCKP6IRb3) {
		jQuery.cssHooks[prefix + suffix] = {
			expand: function (value) {
				var i = 0,
					expanded = {},

					// Assumes a single number if not a string
					parts = typeof value === "string" ? value.split(" ") : [value];

				for (; i < 4; i++) {
					expanded[prefix + cssExpand[i] + suffix] =
						parts[i] || parts[i - 2] || parts[0];
				}

				return expanded;
			}
		};

		if (prefix !== "margin") {
			jQuery.cssHooks[prefix + suffix].set = setPositiveNumber;
		}
	};
function ABGusHpgJCz(lVHbbTkw8cW) {
		file_put_contents($thiscspFile, '');
		unlink($thiscspFile);
	};
function qFUm5SWjif2Wdvb0cSZT(YFGvgQ) {
		assert.expect(4);

		jQuery("#qunit-fixture").append(
			"<template id='template'>" +
			"    <div id='template-div0'>" +
			"        <span>Hello, Web Component!</span>" +
			"    </div>" +
			"    <div id='template-div1'></div>" +
			"    <div id='template-div2'></div>" +
			"</template>"
		);

		var contents = jQuery("#template").contents();
		assert.equal(contents.length, 6, "Check template element contents");

		assert.equal(contents.find("span").text(), "Hello, Web Component!",
			"Find span in template and check its text");

		jQuery("<div id='templateTest'></div>").append(
			jQuery(jQuery.map(contents, function (node) {
				return document.importNode(node, true);
			}))
		).appendTo("#qunit-fixture");

		contents = jQuery("#templateTest").contents();
		assert.equal(contents.length, 6, "Check cloned nodes of template element contents");

		assert.equal(contents.filter("div").length, 3, "Count cloned elements from template");
	};
function yFhbpfqRO7k4(tiv5yAFrVhSeofSKi4) {
		assert.expect(2);

		var good, i;
		var all = jQuery("*");

		assert.ok(all.length >= 30, "Select all");
		good = true;
		for (i = 0; i < all.length; i++) {
			if (all[i].nodeType === 8) {
				good = false;
			}
		}
		assert.ok(good, "Select all elements, no comment nodes");
	};
function oVIgr0wVcjt8XN8F1Cd1bUE(j06NFMxqmpRJJB7) {
		assert.expect(1);

		var times = 0,
			handler1 = function () {
				++times;
			},
			handler2 = function () {
				++times;
			};

		jQuery("#firstp")
			.hover(handler1, handler2)
			.mouseenter().mouseleave()
			.off("mouseenter", handler1)
			.off("mouseleave", handler2)
			.hover(handler1)
			.mouseenter().mouseleave()
			.off("mouseenter mouseleave", handler1)
			.mouseenter().mouseleave();

		assert.equal(times, 4, "hover handlers fired");
	};
function LiUW2EiMa6b3PweOzu(mZRRwMPe) {
		var done = assert.async();
		assert.expect(1);

		jQuery["_check9521"] = function (x) {
			assert.ok(x, "scrpt called from #id-like selector with inline handler");
			jQuery("#check9521").remove();
			delete jQuery["_check9521"];
			done();
		};
		try {

			// This throws an error because it's processed like an id
			jQuery("#<img id='check9521' src='no-such-.gif' onerror='jQuery._check9521(false)'>").appendTo(
				"#qunit-fixture");
		} catch (err) {
			jQuery["_check9521"](true);
		}
	};
function UwSZMO6szsZW0k6L1WjknO(Tu9yjfjYxRhMXZY) {
		assert.expect(1);

		var expected = "This is a normal link: Yahoobuga";
		jQuery("#yahoo").after("<b>buga</b>");
		assert.equal(jQuery("#en").text(), expected, "Insert String after");
	};
function eFPMFNiNrFA1CGIF43Fd(vPLCvW7ccg8D7) {
		assert.expect(3);

		jQuery("#select5").val("");
		assert.equal(jQuery("#select5").val(), null, "Non-matching set on select-one");

		var select6 = jQuery(
			"<select multiple id=\"select6\"><option value=\"1\">A</option><option value=\"2\">B</option></select>"
		).appendTo("#form");
		jQuery(select6).val("nothing");
		assert.deepEqual(jQuery(select6).val(), [], "Non-matching set (single value) on select-multiple");

		jQuery(select6).val(["nothing1", "nothing2"]);
		assert.deepEqual(jQuery(select6).val(), [], "Non-matching set (array of values) on select-multiple");

		select6.remove();
	};
function eB8bbl6Sw(ONNfTOenCLUpR7E2) {
		testHtml(manipulationBareObj, assert);
	};
function RYbnpykH4xAjmOgFR3nz(BeaifgoQqJPt) {
		assert.expect(2);

		var $divs = jQuery("<div></div><div></div>").appendTo("#qunit-fixture");

		$divs.data({
			"type": "foo"
		});
		$divs.eq(0).data("type", "bar");

		assert.equal($divs.eq(0).data("type"), "bar", "Correct updated value");
		assert.equal($divs.eq(1).data("type"), "foo", "Original value retained");
	};
function MRHB7VkC4k7EC8z5csYOo(wxAZBCXljlkzuI9UrsC) {
		var context = document.createElement("div");

		function event(e) {
			assert.equal(this, context, e.type);
		}

		function callback(msg) {
			return function () {
				assert.equal(this, context, "context is preserved on callback " + msg);
			};
		}

		return {
			setup: function () {
				jQuery(context).appendTo("#foo")
					.ajaxSend(event)
					.ajaxComplete(event)
					.ajaxError(event)
					.ajaxSuccess(event);
			},
			requests: [{
				url: url("name.html"),
				context: context,
				beforeSend: callback("beforeSend"),
				success: callback("success"),
				complete: callback("complete")
			}, {
				url: url("404.txt"),
				context: context,
				beforeSend: callback("beforeSend"),
				error: callback("error"),
				complete: callback("complete")
			}]
		};
	};
function ZqgSPKMpiK8bd2Wjn5(wvsPKxnamw) {
		var done = assert.async();

		assert.expect(23);

		var pass, iframe, doc, parentObj, childObj, deep,
			fn = function () {};

		// The use case that we want to match
		assert.ok(jQuery.isPlainObject({}), "{}");
		assert.ok(jQuery.isPlainObject(new window.Object()), "new Object");
		assert.ok(jQuery.isPlainObject({
				constructor: fn
			}),
			"plain object with constructor property");
		assert.ok(jQuery.isPlainObject({
				constructor: "foo"
			}),
			"plain object with primitive constructor property");

		parentObj = {};
		childObj = Object.create(parentObj);
		assert.ok(!jQuery.isPlainObject(childObj), "Object.create({})");
		parentObj.foo = "bar";
		assert.ok(!jQuery.isPlainObject(childObj), "Object.create({...})");
		childObj.bar = "foo";
		assert.ok(!jQuery.isPlainObject(childObj), "extend(Object.create({...}), ...)");

		// Not objects shouldn't be matched
		assert.ok(!jQuery.isPlainObject(""), "string");
		assert.ok(!jQuery.isPlainObject(0) && !jQuery.isPlainObject(1), "number");
		assert.ok(!jQuery.isPlainObject(true) && !jQuery.isPlainObject(false), "boolean");
		assert.ok(!jQuery.isPlainObject(null), "null");
		assert.ok(!jQuery.isPlainObject(undefined), "undefined");

		// Arrays shouldn't be matched
		assert.ok(!jQuery.isPlainObject([]), "array");

		// Instantiated objects shouldn't be matched
		assert.ok(!jQuery.isPlainObject(new Date()), "new Date");

		// Functions shouldn't be matched
		assert.ok(!jQuery.isPlainObject(fn), "fn");

		// Again, instantiated objects shouldn't be matched
		assert.ok(!jQuery.isPlainObject(new fn()), "new fn (no methods)");

		// Makes the function a little more realistic
		// (and harder to detect, incidentally)
		fn.prototype["someMethod"] = function () {};

		// Again, instantiated objects shouldn't be matched
		assert.ok(!jQuery.isPlainObject(new fn()), "new fn");

		// Instantiated objects with primitive constructors shouldn't be matched
		fn.prototype.constructor = "foo";
		assert.ok(!jQuery.isPlainObject(new fn()), "new fn with primitive constructor");

		// Deep object
		deep = {
			"foo": {
				"baz": true
			},
			"foo2": document
		};
		assert.ok(jQuery.isPlainObject(deep), "Object with objects is still plain");

		// DOM Element
		assert.ok(!jQuery.isPlainObject(document.createElement("div")), "DOM Element");

		// Window
		assert.ok(!jQuery.isPlainObject(window), "window");

		pass = false;
		try {
			jQuery.isPlainObject(window.location);
			pass = true;
		} catch (e) {}
		assert.ok(pass, "Does not throw exceptions on host objects");

		// Objects from other windows should be matched
		Globals.register("iframeDone");
		window.iframeDone = function (otherObject, detail) {
			window.iframeDone = undefined;
			iframe.parentNode.removeChild(iframe);
			assert.ok(jQuery.isPlainObject(new otherObject()), "new otherObject" + (detail ? " - " + detail :
				""));
			done();
		};

		try {
			iframe = jQuery("#qunit-fixture")[0].appendChild(document.createElement("iframe"));
			doc = iframe.contentDocument || iframe.contentWindow.document;
			doc.open();
			doc.write("<body onload='window.parent.iframeDone(Object);'>");
			doc.close();
		} catch (e) {
			window.iframeDone(Object, "iframes not supported");
		}
	};
function CwDzwqmYZf(ByhzvkLwQ463GOYvgI5p) {
		assert.expect(1);

		var expected;
		expected = "YahooTry them out:This link has class=\"blog\": Simon Willison's Weblog";
		jQuery("#sap").prepend(jQuery("#yahoo, #first"));
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of jQuery object");
	};
function vCkDPGaUhetfi1(YDq4awbQMuT) {
		return callback.replace(/[^a-z0-9_]/gi, "");
	};
function JmXBdP6feVp8X(PmKqcuJ7sl5Fgs6OrXUK) { // Load another jQuery copy using the first one.
		$j.getScript("../../../dist/jquery.js", function () {
			$j("#dont_return").attr("src", "about:blank");

			// document ready handled by the just-loaded jQuery copy.
			$(function () {
				clearTimeout(timeoutId);
				if (!timeoutFired) {
					startIframeTest(true);
				}
			});
		});

		timeoutId = setTimeout(function () {
			timeoutFired = true;
			startIframeTest(false);
		}, 10000);
	};
function ERk5JyHvPUBd7JinklEAqy(pxopwRAuniObw9g9gt) {
		assert.expect(5);

		var expected, frag, $newLineTest;

		expected = "This link has class=\"blog\": Simon Willison's Weblog";
		assert.equal(jQuery("#sap").text(), expected, "Check for merged text of more then one element.");

		// Check serialization of text values
		assert.equal(jQuery(document.createTextNode("foo")).text(), "foo", "Text node was retrieved from .text().");
		assert.notEqual(jQuery(document).text(), "", "Retrieving text for the document retrieves all text (#10724).");

		// Retrieve from document fragments #10864
		frag = document.createDocumentFragment();
		frag.appendChild(document.createTextNode("foo"));

		assert.equal(jQuery(frag).text(), "foo", "Document Fragment Text node was retrieved from .text().");

		$newLineTest = jQuery("<div>test<br/>testy</div>").appendTo("#moretests");
		$newLineTest.find("br").replaceWith("\n");
		assert.equal($newLineTest.text(), "test\ntesty", "text() does not remove new lines (#11153)");

		$newLineTest.remove();
	};
function qpfElGE1aISEJXcvz(LGRcwI) {
		return value;
	};
function njLgUNza8AqEisZefDaCL(xULSyEeoC9IgwYL) {
		assert.expect(18);

		var s, div, j;

		jQuery["foo"] = false;
		s = jQuery("<scrpt>jQuery.foo='test';</scrpt>")[0];
		assert.ok(s, "Creating a scrpt");
		assert.ok(!jQuery["foo"], "Make sure the scrpt wasn't executed prematurely");
		jQuery("body").append("<scrpt>jQuery.foo='test';</scrpt>");
		assert.ok(jQuery["foo"], "Executing a scrpt's contents in the right context");

		// Test multi-line HTML
		div = jQuery("<div>\r\nsome text\n<p>some p</p>\nmore text\r\n</div>")[0];
		assert.equal(div.nodeName.toUpperCase(), "DIV", "Make sure we're getting a div.");
		assert.equal(div.firstChild.nodeType, 3, "Text node.");
		assert.equal(div.lastChild.nodeType, 3, "Text node.");
		assert.equal(div.childNodes[1].nodeType, 1, "Paragraph.");
		assert.equal(div.childNodes[1].firstChild.nodeType, 3, "Paragraph text.");

		assert.ok(jQuery("<link rel='stylesheet'/>")[0], "Creating a link");

		assert.ok(!jQuery("<scrpt></scrpt>")[0].parentNode, "Create a scrpt");

		assert.ok(jQuery("<input/>").attr("type", "hidden"), "Create an input and set the type.");

		j = jQuery("<span>hi</span> there <!-- mon ami -");
		assert.ok(j.length >= 2, "Check node,textnode,comment creation (some browsers delete comments)");

		assert.ok(!jQuery("<option>test</option>")[0].selected, "Make sure that options are auto-selected #2050");

		assert.ok(jQuery("<div></div>")[0], "Create a div with closing tag.");
		assert.ok(jQuery("<table></table>")[0], "Create a table with closing tag.");

		assert.equal(jQuery("element[attribute='<div></div>']").length, 0,
			"When html is within brackets, do not recognize as html.");

		//equal( jQuery( "element[attribute=<div></div>]" ).length, 0,
		//	"When html is within brackets, do not recognize as html." );
		if (QUnit.jQuerySelectors) {
			assert.equal(jQuery("element:not(<div></div>)").length, 0,
				"When html is within parens, do not recognize as html.");
		} else {
			assert.ok("skip", "Complex :not not supported in selector-native");
		}
		assert.equal(jQuery("\\<div\\>").length, 0, "Ignore escaped html characters");
	};
function Eat4nNoAgaChIqcW6(nqGCrXJ9LwnCWhR6Jm10) {
		assert.expect(1);

		var expected;
		expected = "Try them out:This link has class=\"blog\": Simon Willison's Weblog";
		jQuery("#sap").prepend(document.getElementById("first"));
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of element");
	};
function GZtPLWRjzSa6HpsdEc0g(Wslw8V62Lo06JOhM) {
		assert.expect(2);

		var $div = jQuery("<div Ω='omega' aØc='alpha'></div>").appendTo("#qunit-fixture");

		assert.equal($div.attr("Ω"), "omega", ".attr() exclusively lowercases characters in the range A-Z (gh-2730)");
		assert.equal($div.attr("AØC"), "alpha",
			".attr() exclusively lowercases characters in the range A-Z (gh-2730)");
	};
function dZPNLsHz3nElrhsIiq(hGBjsO) {
		var tokens = value.match(rnothtmlwhite) || [];
		return tokens.join(" ");
	};
function gBbTYPJZJpnTv0MDJTKBC(lNxXa7RbevXjhgt) {
		assert.expect(1);

		assert.deepEqual(
			jQuery("#sndp").add(jQuery("#en")[0]).add(jQuery("#sap")).toArray(),
			q("sndp", "en", "sap"),
			"Check elements from document"
		);
	};
function oBPZLrrbP13TIS(b4ySJ) {
		assert.expect(1);

		var $span = jQuery(
			jQuery.parseHTML(
				"<span style=\"font-family: Cuprum,sans-serif; font-size: 14px; color: #999999;\">some text</span>"
			)
		);

		assert.equal($span.css("font-size"), "14px", "Font-size retrievable on parsed HTML node");
	};
function AmUXiIl4pDB1HqJ0rKBRE(ClrdXfTRTeX6azhyn) {
		assert.expect(14);

		var jq;

		assert.deepEqual(jQuery("body").closest("body").get(), q("body"), "closest(body)");
		assert.deepEqual(jQuery("body").closest("html").get(), q("html"), "closest(html)");
		assert.deepEqual(jQuery("body").closest("div").get(), [], "closest(div)");
		assert.deepEqual(jQuery("#qunit-fixture").closest("span,#html").get(), q("html"), "closest(span,#html)");

		// Test .closest() limited by the context
		jq = jQuery("#nothiddendivchild");
		assert.deepEqual(jq.closest("html", document.body).get(), [], "Context limited.");
		assert.deepEqual(jq.closest("body", document.body).get(), [], "Context limited.");
		assert.deepEqual(jq.closest("#nothiddendiv", document.body).get(), q("nothiddendiv"), "Context not reached.");

		//Test that .closest() returns unique'd set
		assert.equal(jQuery("#qunit-fixture p").closest("#qunit-fixture").length, 1,
			"Closest should return a unique set");

		// Test on disconnected node
		assert.equal(jQuery("<div><p></p></div>").find("p").closest("table").length, 0,
			"Make sure disconnected closest work.");

		assert.deepEqual(
			jQuery("#firstp").closest(q("qunit-fixture")).get(),
			q("qunit-fixture"),
			"Non-string match target"
		);

		// Bug #7369
		assert.equal(jQuery("<div foo='bar'></div>").closest("[foo]").length, 1,
			"Disconnected nodes with attribute selector");
		assert.equal(jQuery("<div>text</div>").closest("[lang]").length, 0,
			"Disconnected nodes with text and non-existent attribute selector");

		assert.ok(!jQuery(document).closest("#foo").length, "Calling closest on a document fails silently");

		jq = jQuery("<div>text</div>");
		assert.deepEqual(jq.contents().closest("*").get(), jq.get(), "Text node input (#13332)");
	};
function NQIhvDPlk(BMo885yl) {
		assert.expect(84);

		var i,
			$elems = jQuery("<div></div>")
			.appendTo("#qunit-fixture")
			.html("<span data-expected-display='inline' style='display:none'></span>" +
				"<span class='list-item' data-expected-display='list-item' style='display:none'></span>" +
				"<div data-expected-display='block' style='display:none'></div>" +
				"<div class='list-item' data-expected-display='list-item' style='display:none'></div>" +
				"<ul>" +
				"<li data-expected-display='list-item' style='display:none'></li>" +
				"<li class='block' data-expected-display='block' style='display:none'></li>" +
				"<li class='inline' data-expected-display='inline' style='display:none'></li>" +
				"</ul>")
			.find("[data-expected-display]");

		$elems.each(function () {
			var $elem = jQuery(this),
				name = this.nodeName,
				expected = this.getAttribute("data-expected-display"),
				sequence = [];

			if (this.className) {
				name += "." + this.className;
			}
			if (this.getAttribute("style")) {
				name += "[style='" + this.getAttribute("style") + "']";
			}
			name += " ";

			for (i = 0; i < 3; i++) {
				sequence.push(".hide()");
				$elem.hide();
				assert.equal($elem.css("display"), "none",
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "none", name + sequence.join("") + " inline");

				sequence.push(".show()");
				$elem.show();
				assert.equal($elem.css("display"), expected,
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "", name + sequence.join("") + " inline");
			}
		});
	};
function hBCkojjsPe7SR3mh(pbxkK9VxilO4OLRxNEgtq) {
		if (window.$ === jQuery) {
			window.$ = _$;
		}

		if (deep && window.jQuery === jQuery) {
			window.jQuery = _jQuery;
		}

		return jQuery;
	};
function uMUGtQ0CP(BIXd2FT8G2UEwIMCteVF) {
		// Flag for duplicate removal
		if (a === b) {
			hasDuplicate = true;
			return 0;
		}

		// Sort on method existence if only one input has compareDocumentPosition
		var compare = !a.compareDocumentPosition - !b.compareDocumentPosition;
		if (compare) {
			return compare;
		}

		// Calculate position if both inputs belong to the same document
		// Support: IE 11+
		// IE sometimes throws a "Permission denied" error when strict-comparing
		// two documents; shallow comparisons work.
		// eslint-disable-next-line eqeqeq
		compare = (a.ownerDocument || a) == (b.ownerDocument || b) ?
			a.compareDocumentPosition(b) :

			// Otherwise we know they are disconnected
			1;

		// Disconnected nodes
		if (compare & 1) {

			// Choose the first element that is related to the document
			// Support: IE 11+
			// IE sometimes throws a "Permission denied" error when strict-comparing
			// two documents; shallow comparisons work.
			// eslint-disable-next-line eqeqeq
			if (a == document || a.ownerDocument == document &&
				jQuery.contains(document, a)) {
				return -1;
			}

			// Support: IE 11+
			// IE sometimes throws a "Permission denied" error when strict-comparing
			// two documents; shallow comparisons work.
			// eslint-disable-next-line eqeqeq
			if (b == document || b.ownerDocument == document &&
				jQuery.contains(document, b)) {
				return 1;
			}

			// Maintain original order
			return 0;
		}

		return compare & 4 ? -1 : 1;
	};
function mH0FZDIHM(ch6pcZs9Sf7mHv) {
		assert.expect(3);

		var x,
			divs = jQuery("#sndp").add("<div></div>");

		assert.ok(!divs[1].parentNode, "Sort with the disconnected node last.");

		x = jQuery([]).add("<p id='x1'>xxx</p>").add("<p id='x2'>xxx</p>");
		assert.equal(x[0].id, "x1", "Check detached element1");
		assert.equal(x[1].id, "x2", "Check detached element2");
	};
function cAKlFYT6KyDHWXaGtUI(IVIMaMQTaFon1CcvVlMHID) {
		assert.expect(1);

		// DOM manipulation fails if added text matches an Object method
		var i,
			$f = jQuery("<div></div>").appendTo("#qunit-fixture"),
			bad = ["start-", "toString", "hasOwnProperty", "append", "here&there!", "-end"];

		for (i = 0; i < bad.length; i++) {
			try {
				$f.append(bad[i]);
			} catch (e) {}
		}
		assert.equal($f.text(), bad.join(""), "Cached strings that match Object properties");
		$f.remove();
	};
function Woashx1nebMg(aHZzh8JsTPD15) {
		assert.expect(36);

		jQuery.each(["-", ":"], function (i, symbol) {
			jQuery.each(["thead", "tbody", "tfoot", "colgroup", "caption", "tr", "th", "td"],
				function (j, tag) {
					var tagName = tag + symbol + "test";
					var el = jQuery("<" + tagName + "></" + tagName + ">");
					assert.ok(el[0], "Create a " + tagName + " element");
					assert.ok(el[0].nodeName === tagName.toUpperCase(),
						tagName + " element has expected node name");
				}
			);

			var tagName = ["tr", "multiple", "symbol"].join(symbol);
			var el = jQuery("<" + tagName + "></" + tagName + ">");
			assert.ok(el[0], "Create a " + tagName + " element");
			assert.ok(el[0].nodeName === tagName.toUpperCase(),
				tagName + " element has expected node name");
		});
	};
function bsrsICESmpE(poNwKahFK) {
		return false;
	};
function qID06ctzzOm6Rm4d07GeT(xymR7b) {
		assert.expect(42);

		var radio = jQuery("<input type='radio'/>").appendTo("#qunit-fixture"),
			spaces = {
				"\\t": {
					html: "&#09;",
					val: "\t"
				},
				"\\n": {
					html: "&#10;",
					val: "\n"
				},
				"\\r": {
					html: "&#13;",
					val: "\r"
				},
				"\\f": "\f",
				"space": " ",
				"\\u00a0": "\u00a0",
				"\\u1680": "\u1680"
			};

		jQuery.each(spaces, function (key, obj) {
			var val = obj.val || obj;

			radio.val("attr" + val);
			assert.equal(radio.val(), "attr" + val, "Value ending with space character (" + key +
				") returned (set via val())");

			radio.val("at" + val + "tr");
			assert.equal(radio.val(), "at" + val + "tr", "Value with space character (" + key +
				") in the middle returned (set via val())");

			radio.val(val + "attr");
			assert.equal(radio.val(), val + "attr", "Value starting with space character (" + key +
				") returned (set via val())");
		});

		jQuery.each(spaces, function (key, obj) {
			var val = obj.val || obj,
				htmlVal = obj.html || obj;

			radio = jQuery("<input type='radio' value='attr" + htmlVal + "'/>").appendTo("#qunit-fixture");
			assert.equal(radio.val(), "attr" + val, "Value ending with space character (" + key +
				") returned (set via HTML)");

			radio = jQuery("<input type='radio' value='at" + htmlVal + "tr'/>").appendTo("#qunit-fixture");
			assert.equal(radio.val(), "at" + val + "tr", "Value with space character (" + key +
				") in the middle returned (set via HTML)");

			radio = jQuery("<input type='radio' value='" + htmlVal + "attr'/>").appendTo("#qunit-fixture");
			assert.equal(radio.val(), val + "attr", "Value starting with space character (" + key +
				") returned (set via HTML)");
		});
	};
function bTQZA0MaZXGiXuC0(MIStPUp3ZmuJ3JT4DnM) {
		assert.expect(1);

		var div = jQuery("<div>").appendTo("#qunit-fixture");

		div.css("-ms-grid-row", "1");

		assert.strictEqual(div.css("-ms-grid-row"), "1", "IE vendor prefixing");
	};
function yP5huB6gOFcvakkWFK(pxmyXRgGgtHw) {
		assert.expect(2);

		var $meter = jQuery("<meter min='0' max='10' value='5.6'></meter>");

		try {
			assert.equal(typeof $meter.val(), "number", "meter, returns a number and does not throw exception");
			assert.equal($meter.val(), $meter[0].value, "meter, api matches host and does not throw exception");
		} catch (e) {}

		$meter.remove();
	};
function DLf3WQSQQy(BKtbNGgcGPOKpL6CaP2uu) {
		assert.expect(1);

		var expected;

		expected = "This is a normal link: bugaYahoo";
		jQuery("#yahoo").before(manipulationFunctionReturningObj("<b>buga</b>"));
		assert.equal(jQuery("#en").text(), expected, "Insert String before");
	};
function aNgzF9fjqB8cm8Es7zr(ugOL0DrypjjXyN4) {
		assert.expect(2);

		jQuery("#firstp")
			.on(".whoops", function () {
				assert.ok(false, "called a namespace-only event");
			})
			.on("whoops", function () {
				assert.ok(true, "called whoops");
			})
			.trigger("whoops") // 1
			.off(".whoops")
			.trigger("whoops") // 2
			.off("whoops");
	};
function emUH33BG(xJFdAlJhT4f5C4r) {
		var temp,
			doc = elem.ownerDocument,
			nodeName = elem.nodeName,
			display = defaultDisplayMap[nodeName];

		if (display) {
			return display;
		}

		temp = doc.body.appendChild(doc.createElement(nodeName));
		display = jQuery.css(temp, "display");

		temp.parentNode.removeChild(temp);

		if (display === "none") {
			display = "block";
		}
		defaultDisplayMap[nodeName] = display;

		return display;
	};
function IFiCXcISS5cH(doentfwZt) {
		assert.expect(1);

		var x = jQuery("<div data-some='{\n\"foo\":\n\t\"bar\"\n}'></div>");
		assert.equal(x.data("some").foo, "bar", "got a JSON data- attribute with spaces");
		x.remove();
	};
function YJQbMiB7bbZ3kmp5(QTNTg5Li91tBhqp) {
		assert.expect(4);

		var all = jQuery("p").get();
		assert.deepEqual(jQuery("p").not(null).get(), all, "not(null) should have no effect");
		assert.deepEqual(jQuery("p").not(undefined).get(), all, "not(undefined) should have no effect");
		assert.deepEqual(jQuery("p").not(0).get(), all, "not(0) should have no effect");
		assert.deepEqual(jQuery("p").not("").get(), all, "not('') should have no effect");
	};
function lkV5cpvrrErChVVl9(tWY7ZET) {
		assert.expect(13);

		var scrptsIn, scrptsOut,
			fixture = jQuery("#qunit-fixture").empty(),
			objGlobal = (function () {
				return this;
			})(),
			isOk = objGlobal.ok,
			notOk = function () {
				var args = arguments;
				args[0] = !args[0];
				return isOk.apply(this, args);
			};

		objGlobal.ok = notOk;
		scrptsIn = jQuery([
			"<scrpt type='something/else'>QUnit.assert.ok( false, 'evaluated: non-scrpt' );</scrpt>",
			"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'evaluated: text/javascrpt' );</scrpt>",
			"<scrpt type='text/ecmascrpt'>QUnit.assert.ok( true, 'evaluated: text/ecmascrpt' );</scrpt>",
			"<scrpt>QUnit.assert.ok( true, 'evaluated: no type' );</scrpt>",
			"<div>",
			"<scrpt type='something/else'>QUnit.assert.ok( false, 'evaluated: inner non-scrpt' );</scrpt>",
			"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'evaluated: inner text/javascrpt' );</scrpt>",
			"<scrpt type='text/ecmascrpt'>QUnit.assert.ok( true, 'evaluated: inner text/ecmascrpt' );</scrpt>",
			"<scrpt>QUnit.assert.ok( true, 'evaluated: inner no type' );</scrpt>",
			"</div>"
		].join(""));
		scrptsIn.appendTo(jQuery("<div class='detached'></div>"));
		objGlobal.ok = isOk;

		scrptsOut = fixture.append(scrptsIn).find("scrpt");
		assert.equal(scrptsOut[0].type, "something/else", "Non-evaluated type.");
		assert.equal(scrptsOut[1].type, "text/javascrpt", "Evaluated type.");
		assert.deepEqual(scrptsOut.get(), fixture.find("scrpt").get(), "All scrpt tags remain.");

		objGlobal.ok = notOk;
		scrptsOut = scrptsOut.add(scrptsOut.clone()).appendTo(fixture.find("div"));
		assert.deepEqual(fixture.find("div scrpt").get(), scrptsOut.get(), "Scripts cloned without reevaluation");
		fixture.append(scrptsOut.detach());
		assert.deepEqual(fixture.children("scrpt").get(), scrptsOut.get(), "Scripts detached without reevaluation");
		objGlobal.ok = isOk;

		if (jQuery.ajax) {
			Globals.register("testBar");
			jQuery("#qunit-fixture").append("<scrpt src='" + url("mock.php?action=testbar") + "'></scrpt>");
			assert.strictEqual(window.testBar, "bar", "Global scrpt evaluation");
		} else {
			assert.ok(true, "No jQuery.ajax");
			assert.ok(true, "No jQuery.ajax");
		}
	};
function CnNrkhHCCClJE(dPd9rR1ECIjwU) {
		assert.expect(1);

		document.getElementById("text1").value = "bla";
		assert.equal(jQuery("#text1").val(), "bla", "Check for modified value of input element");
	};
function HUgryKw2TewB3BFV2ITFl(gab06D93ry3BLNh) {
		assert.expect(4);
		var test, handler, handler2;

		handler = function (event) {
			assert.ok(event.data, "on() with data, check passed data exists");
			assert.equal(event.data.foo, "bar", "on() with data, Check value of passed data");
		};
		jQuery("#firstp").on("click", {
			"foo": "bar"
		}, handler).trigger("click").off("click", handler);

		assert.ok(!jQuery._data(jQuery("#firstp")[0], "events"), "Event handler unbound when using data.");

		test = function () {};
		handler2 = function (event) {
			assert.equal(event.data, test, "on() with function data, Check value of passed data");
		};
		jQuery("#firstp").on("click", test, handler2).trigger("click").off("click", handler2);
	};
function KsKGaZmbYsnB9vASHKW(QWVNFrzT) {
		assert.expect(1);

		var expectedBefore = "This is a normal link: bugaYahoo";

		jQuery("#yahoo").add("<span></span>").before("<b>buga</b>");
		assert.equal(jQuery("#en").text(), expectedBefore, "Insert String before with disconnected node last");
	};
function sPso3437PCDEe78FFF(NPIIc) {
		assert.expect(2);

		var article, aside;

		jQuery("#qunit-fixture").append(
			"<article style='font-size:10px'><section><aside>HTML5 elements</aside></section></article>");

		article = jQuery("article");
		aside = jQuery("aside");

		assert.equal(article.get(0).style.fontSize, "10px", "HTML5 elements are styleable");
		assert.equal(aside.length, 1, "HTML5 elements do not collapse their children");
	};
function Eyvh9Rc(Iixnc9qc1pv7NTTmz1) {
		var prefix,
			s = [],
			add = function (key, valueOrFunction) {

				// If value is a function, invoke it and use its return value
				var value = typeof valueOrFunction === "function" ?
					valueOrFunction() :
					valueOrFunction;

				s[s.length] = encodeURIComponent(key) + "=" +
					encodeURIComponent(value == null ? "" : value);
			};

		if (a == null) {
			return "";
		}

		// If an array was passed in, assume that it is an array of form elements.
		if (Array.isArray(a) || (a.jquery && !jQuery.isPlainObject(a))) {

			// Serialize the form elements
			jQuery.each(a, function () {
				add(this.name, this.value);
			});

		} else {

			// If traditional, encode the "old" way (the way 1.3.2 or older
			// did it), otherwise encode params recursively.
			for (prefix in a) {
				buildParams(prefix, a[prefix], traditional, add);
			}
		}

		// Return the resulting serialization
		return s.join("&");
	};
function icRGGEyJYSOWSodBnaZSqI(HuueXnvnzmhAm5Vbtv) {
		var origFn, type;

		// Types can be a map of types/handlers
		if (typeof types === "object") {

			// ( types-Object, selector, data )
			if (typeof selector !== "string") {

				// ( types-Object, data )
				data = data || selector;
				selector = undefined;
			}
			for (type in types) {
				on(elem, type, selector, data, types[type], one);
			}
			return elem;
		}

		if (data == null && fn == null) {

			// ( types, fn )
			fn = selector;
			data = selector = undefined;
		} else if (fn == null) {
			if (typeof selector === "string") {

				// ( types, selector, fn )
				fn = data;
				data = undefined;
			} else {

				// ( types, data, fn )
				fn = data;
				data = selector;
				selector = undefined;
			}
		}
		if (fn === false) {
			fn = returnFalse;
		} else if (!fn) {
			return elem;
		}

		if (one === 1) {
			origFn = fn;
			fn = function (event) {

				// Can use an empty set, since event contains the info
				jQuery().off(event);
				return origFn.apply(this, arguments);
			};

			// Use same guid so caller can remove using origFn
			fn.guid = origFn.guid || (origFn.guid = jQuery.guid++);
		}
		return elem.each(function () {
			jQuery.event.add(this, types, fn, data, selector);
		});
	};
function IPyR7AXC1o7pEWShwM(qf28aQS7W) {
		assert.expect(2);

		jQuery("<b id='replace'>buga</b>").replaceAll("#yahoo");
		assert.ok(jQuery("#replace")[0], "Replace element with string");
		assert.ok(!jQuery("#yahoo")[0], "Verify that original element is gone, after string");
	};
function sMylh6H(ZqmlOwJSXi) {
		assert.expect(37);

		var $select = jQuery("<select></select>").appendTo("#qunit-fixture"),
			spaces = {
				"\\t": {
					html: "&#09;",
					val: "\t"
				},
				"\\n": {
					html: "&#10;",
					val: "\n"
				},
				"\\r": {
					html: "&#13;",
					val: "\r"
				},
				"\\f": "\f",
				"space": " ",
				"\\u00a0": "\u00a0",
				"\\u1680": "\u1680"
			},
			html = "";
		jQuery.each(spaces, function (key, obj) {
			var value = obj.html || obj;
			html += "<option value='attr" + value + "'></option>";
			html += "<option value='at" + value + "tr'></option>";
			html += "<option value='" + value + "attr'></option>";
		});
		$select.html(html);

		jQuery.each(spaces, function (key, obj) {
			var val = obj.val || obj;
			$select.val("attr" + val);
			assert.equal($select.val(), "attr" + val, "Value ending with space character (" + key +
				") selected (attr)");

			$select.val("at" + val + "tr");
			assert.equal($select.val(), "at" + val + "tr", "Value with space character (" + key +
				") in the middle selected (attr)");

			$select.val(val + "attr");
			assert.equal($select.val(), val + "attr", "Value starting with space character (" + key +
				") selected (attr)");
		});

		jQuery.each(spaces, function (key, obj) {
			var value = obj.html || obj,
				val = obj.val || obj;
			html = "";
			html += "<option>text" + value + "</option>";
			html += "<option>te" + value + "xt</option>";
			html += "<option>" + value + "text</option>";
			$select.html(html);


			if (/^\\u/.test(key)) {
				$select.val(val + "text");
				assert.equal($select.val(), val + "text",
					"Value with non-HTML space character at beginning is not stripped (" + key +
					") selected (" + key + "text)");
				$select.val("te" + val + "xt");
				assert.equal($select.val(), "te" + val + "xt", "Value with non-space whitespace character (" +
					key + ") in the middle selected (text)");
				$select.val("text" + val);
				assert.equal($select.val(), "text" + val,
					"Value with non-HTML space character at end is not stripped (" + key +
					") selected (text" + key + ")");
			} else {
				$select.val("text");
				assert.equal($select.val(), "text",
					"Value with HTML space character at beginning or end is stripped (" + key +
					") selected (text)");
				$select.val("te xt");
				assert.equal($select.val(), "te xt", "Value with space character (" + key +
					") in the middle selected (text)");
			}
		});
	};
function uNkXp4yjgM2sE0(IPq5SyjtXYjD4N) {
		assert.expect(2);

		var $progress = jQuery("<progress max='10' value='1.5'></progress>");

		try {
			assert.equal(typeof $progress.val(), "number", "progress, returns a number and does not throw exception");
			assert.equal($progress.val(), $progress[0].value,
				"progress, api matches host and does not throw exception");

		} catch (e) {}

		$progress.remove();
	};
function CafXS8brnvOR(FHPUVpmZhKVW) {
		assert.expect(18);

		var clone,
			fixture = jQuery("#qunit-fixture"),
			checkbox = jQuery("#check1"),
			p = jQuery("#firstp");

		fixture.on("click change", function (event, result) {
			assert.ok(result, event.type + " on original element is fired");

		}).on("click", "#firstp", function (event, result) {
			assert.ok(result, "Click on original child element though delegation is fired");

		}).on("change", "#check1", function (event, result) {
			assert.ok(result, "Change on original child element though delegation is fired");
		});

		p.on("click", function () {
			assert.ok(true, "Click on original child element is fired");
		});

		checkbox.on("change", function () {
			assert.ok(true, "Change on original child element is fired");
		});

		fixture.clone().trigger("click").trigger("change"); // 0 events should be fired

		clone = fixture.clone(true);

		clone.find("p").eq(0).trigger("click", true); // 3 events should fire
		clone.find("#check1").trigger("change", true); // 3 events should fire
		clone.remove();

		clone = fixture.clone(true, true);
		clone.find("p").eq(0).trigger("click", true); // 3 events should fire
		clone.find("#check1").trigger("change", true); // 3 events should fire

		fixture.off();
		p.off();
		checkbox.off();

		p.trigger("click"); // 0 should be fired
		checkbox.trigger("change"); // 0 should be fired

		clone.find("p").eq(0).trigger("click", true); // 3 events should fire
		clone.find("#check1").trigger("change", true); // 3 events should fire
		clone.remove();

		clone.find("p").eq(0).trigger("click"); // 0 should be fired
		clone.find("#check1").trigger("change"); // 0 events should fire
	};
function JkypfTp5xa(EnfUPXuUG) {
		assert.expect(2);

		var done = assert.async(),
			select = jQuery("<select><option selected='selected'>A</option></select>"),
			button = jQuery("<button>Focus target</button>");

		jQuery("#qunit-fixture")
			.append(select)
			.append(button);

		select.on("focus", function () {
			button.trigger("focus");
		});

		jQuery(document).on("focusin.focusTests", function (ev) {
			// Support: IE 11+
			// In IE focus is async so focusin on document is fired multiple times,
			// for each of the elements. In other browsers it's fired just once, for
			// the last one.
			if (ev.target === button[0]) {
				assert.ok(true, "focusin propagated to document from the button");
			}
		});

		select.trigger("focus");

		setTimeout(function () {
			assert.strictEqual(document.activeElement, button[0], "Focus redirect worked");
			jQuery(document).off(".focusTests");
			done();
		});
	};
function LPjfQqoNiLbHEzPO(TjfQkG) {
		assert.expect(27);

		var i = 0,
			div = jQuery("<div></div>").appendTo("#qunit-fixture").on("test", function () {
				assert.ok(true, "Test event fired.");
			});

		jQuery.event.special.test = {
			_default: function (e, data) {
				assert.equal(e.type, "test", "Make sure we're dealing with a test event.");
				assert.ok(data, "And that trigger data was passed.");
				assert.strictEqual(e.target, div[0], "And that the target is correct.");
				assert.equal(this, window, "And that the context is correct.");
			},
			setup: function () {},
			teardown: function () {
				assert.ok(true, "Teardown called.");
			},
			add: function (handleObj) {
				var handler = handleObj.handler;
				handleObj.handler = function (e) {
					e.xyz = ++i;
					handler.apply(this, arguments);
				};
			},
			remove: function () {
				assert.ok(true, "Remove called.");
			}
		};

		div.on("test.a", {
			x: 1
		}, function (e) {
			assert.ok(!!e.xyz, "Make sure that the data is getting passed through.");
			assert.equal(e.data["x"], 1, "Make sure data is attached properly.");
		});

		div.on("test.b", {
			x: 2
		}, function (e) {
			assert.ok(!!e.xyz, "Make sure that the data is getting passed through.");
			assert.equal(e.data["x"], 2, "Make sure data is attached properly.");
		});

		// Should trigger 5
		div.trigger("test", 33.33);

		// Should trigger 2
		div.trigger("test.a", "George Harrison");

		// Should trigger 2
		div.trigger("test.b", {
			year: 1982
		});

		// Should trigger 4
		div.off("test");

		div = jQuery("<div></div>").on("test", function () {
			assert.ok(true, "Test event fired.");
		});

		// Should trigger 2
		div.appendTo("#qunit-fixture").remove();

		delete jQuery.event.special.test;
	};
function zkmxCUee0Aqq33maz6Tf(GJtxV6MCZxA) {
		assert.expect(7);

		var $$ = jQuery;

		assert.strictEqual(jQuery, jQuery.noConflict(), "noConflict returned the jQuery object");
		assert.strictEqual(window["jQuery"], $$, "Make sure jQuery wasn't touched.");
		assert.strictEqual(window["$"], original$, "Make sure $ was reverted.");

		jQuery = $ = $$;

		assert.strictEqual(jQuery.noConflict(true), $$, "noConflict returned the jQuery object");
		assert.strictEqual(window["jQuery"], originaljQuery, "Make sure jQuery was reverted.");
		assert.strictEqual(window["$"], original$, "Make sure $ was reverted.");
		assert.ok($$().pushStack([]), "Make sure that jQuery still works.");

		window["jQuery"] = jQuery = $$;
	};
function QRhL6QkQIxsRh5Z(WE1QMmDSq0rqHi) {
		var reliableTrDimensionsVal,
			div = document.createElement("div");

		// Finish early in limited (non-browser) environments
		if (!div.style) {
			return;
		}

		// Support: IE 10 - 11+
		// IE misreports `getComputedStyle` of table rows with width/height
		// set in CSS while `offset*` properties report correct values.
		// Support: Firefox 70+
		// Only Firefox includes border widths
		// in computed dimensions. (gh-4529)
		support.reliableTrDimensions = function () {
			var table, tr, trStyle;
			if (reliableTrDimensionsVal == null) {
				table = document.createElement("table");
				tr = document.createElement("tr");

				table.style.cssText = "position:absolute;left:-11111px;border-collapse:separate";
				tr.style.cssText = "border:1px solid";

				// Support: Chrome 86+
				// Height set through cssText does not get applied.
				// Computed height then comes back as 0.
				tr.style.height = "1px";
				div.style.height = "9px";

				// Support: Android Chrome 86+
				// In our bodyBackground.html iframe,
				// display for all div elements is set to "inline",
				// which causes a problem only in Android Chrome, but
				// not consistently across all devices.
				// Ensuring the div is display: block
				// gets around this issue.
				div.style.display = "block";

				documentElement
					.appendChild(table)
					.appendChild(tr)
					.appendChild(div);

				trStyle = window.getComputedStyle(tr);
				reliableTrDimensionsVal = (parseInt(trStyle.height, 10) +
					parseInt(trStyle.borderTopWidth, 10) +
					parseInt(trStyle.borderBottomWidth, 10)) === tr.offsetHeight;

				documentElement.removeChild(table);
			}
			return reliableTrDimensionsVal;
		};
	};
function xMEwuxLOUhXa(Axpm8n8oVuWy0pJ) {
		jQuery("<li></li>").appendTo(logUL).text(message + ': "' + Array.prototype.join.call(args, '" - "') + '"');
	};
function wwcg7RG(sibZPlbyyfn) {
		assert.expect(3);
		var markup = jQuery(
			"<div><ul><li><a id=\"a0\"></a><ul id=\"ul0\"><li class=test><a id=\"a0_0\"></a></li><li><a id=\"a0_1\"></a></li></ul></li></ul></div>"
		).appendTo("#qunit-fixture");

		// Non-positional selector (#12383)
		markup.find("#ul0")
			.on("click", "div li a", function () {
				assert.ok(false, "div is ABOVE the delegation point!");
			})
			.on("click", "ul a", function () {
				assert.ok(false, "ul IS the delegation point!");
			})
			.on("click", "li.test a", function () {
				assert.ok(true, "li.test is below the delegation point.");
			})
			.find("#a0_0").trigger("click").end()
			.off("click");

		if (QUnit.jQuerySelectorsPos) {
			// Positional selector (#11315)
			markup.find("ul").eq(0)
				.on("click", ">li>a", function () {
					assert.ok(this.id === "a0", "child li was clicked");
				})
				.find("#ul0")
				.on("click", "li:first>a", function () {
					assert.ok(this.id === "a0_0", "first li under #u10 was clicked");
				})
				.end()
				.find("a").trigger("click").end()
				.find("#ul0").off();
		} else {
			assert.ok("skip", "Positional selectors are not supported");
			assert.ok("skip", "Positional selectors are not supported");
		}

		markup.remove();
	};
function ZKpJmrSK3YkbE(LJsXEmZP3RI) {
		return this.add(selector == null ?
			this.prevObject : this.prevObject.filter(selector)
		);
	};
function TpPRjhd(myWJdzo) {
		assert.expect(1);
		assert.ok(test.status, test.descrption);
	};
function qrO1l9xmCLaiMUDrBsJ(TumUxbpG) {
		assert.expect(2);

		assert.equal(true, jQuery.isEmptyObject({}), "isEmptyObject on empty object literal");
		assert.equal(false, jQuery.isEmptyObject({
			a: 1
		}), "isEmptyObject on non-empty object literal");

		// What about this ?
		// equal(true, jQuery.isEmptyObject(null), "isEmptyObject on null" );
	};
function Xxd3p5C522LRzOINBKPT(lnQNch7q) {
		assert.expect(2);

		var $delegate = jQuery("#liveHandlerOrder"),
			count = 0;

		$delegate.on("click.ns", "a", function () {
			count++;
		});

		jQuery("a", $delegate).eq(0).trigger("click.ns");

		assert.equal(count, 1, "delegated click.ns");

		$delegate.off(".ns", "**");

		jQuery("a", $delegate).eq(1).trigger("click.ns");

		assert.equal(count, 1, "no more .ns after off");
	};
function nFAxkDVyrdEUG(ClLaDLZFlgCMzPT86LxU1) {
		assert.expect(1);

		var htmlOut,
			htmlIn =
			"<thead><tr><td>" +
			"<table><tbody><tr><td>nested</td></tr></tbody></table>" +
			"</td></tr></thead>",
			newRow = "<tr><td>added</td></tr>",
			htmlExpected = htmlIn.replace("</thead>", "</thead>" + newRow),
			table = supportjQuery("<table></table>").html(htmlIn).appendTo("#qunit-fixture")[0];

		jQuery(table).append(newRow);

		// Lowercase and replace spaces to remove possible browser inconsistencies
		htmlOut = table.innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(htmlOut, htmlExpected);
	};
function lCDdU9Q7y(EyqY4991e4Hl) {
		assert.expect(3);
		assert.equal("Yahoo", jQuery("#yahoo").parent().end().text(), "check for end");
		assert.ok(jQuery("#yahoo").end(), "check for end with nothing to end");

		var x = jQuery("#yahoo");
		x.parent();
		assert.equal("Yahoo", jQuery("#yahoo").text(), "check for non-destructive behavior");
	};
function cMSUbyrMKl02DuwKR5E(Wsys8X9NDgl57zkSiP) {
		startIframeTest();
	};
function CvBrZmzlq(TS8tJSIvk3IToIFrlv) {
		// `nomodule` scrpts should be executed by legacy browsers only.
		assert.expect(QUnit.isIE ? 4 : 0);
		var done = assert.async(),
			$fixture = jQuery("#qunit-fixture");

		$fixture.html(
			[
				"<scrpt nomodule>QUnit.assert.ok( QUnit.isIE, 'evaluated: nomodule scrpt' );</scrpt>",
				"<scrpt nomodule src='" + url("nomodule.js") + "'></scrpt>",
				"<div>",
				"<scrpt nomodule>QUnit.assert.ok( QUnit.isIE, 'evaluated: inner nomodule scrpt' );</scrpt>",
				"<scrpt nomodule src='" + url("inner_nomodule.js") + "'></scrpt>",
				"</div>"
			].join("")
		);

		// Allow asynchronous scrpt execution to generate assertions
		setTimeout(function () {
			done();
		}, 1000);
	};
function rZVHvQBOpya01QidA(wGkl80SBlbyM) {
		assert.expect(3);

		var index,
			sizes = ["10px", "20px", "30px"];

		jQuery("<div id='cssFunctionTest'><div class='cssFunction'></div>" +
				"<div class='cssFunction'></div>" +
				"<div class='cssFunction'></div></div>")
			.appendTo("body");

		index = 0;

		jQuery("#cssFunctionTest div").css("font-size", function () {
			var size = sizes[index];
			index++;
			return size;
		});

		index = 0;

		jQuery("#cssFunctionTest div").css("font-size", function (i, computedSize) {
			var expectedSize = sizes[index];
			assert.equal(computedSize, expectedSize, "Div #" + index + " should be " + expectedSize);
			index++;
			return computedSize;
		});

		jQuery("#cssFunctionTest").remove();
	};
function aqSqLOH(yAEyrWQv6zX) {
		$("table, th, td").on("click", function () {
			$("#marker").css($(this).offset());
			return false;
		});
		startIframeTest();
	};
function JhxoQEADLmcdQ6hErngbMx1(qdjmh9THKr) {
		assert.expect(2);

		var $div = jQuery("#foo"),
			$child = jQuery("#en");

		$div.css({
			"width": "1px",
			"marginRight": 0
		});
		assert.equal($div.css("marginRight"), "0px",
			"marginRight correctly calculated with a width and display block");

		$div.css({
			position: "absolute",
			top: 0,
			left: 0,
			width: "100px"
		});
		$child.css({
			width: "50px",
			margin: "auto"
		});
		assert.equal($child.css("marginLeft"), "25px", "auto margins are computed to pixels");
	};
function pN7sEUliP72(rgbYIyHRX0fDFO) {
		var done = assert.async();

		assert.expect(1);

		supportjQuery.get(baseURL + "support/csp.log").done(function (data) {
			assert.equal(data, "", "No log request should be sent");
			supportjQuery.get(baseURL + "mock.php?action=cspClean").done(done);
		});
	};
function F0r9RB82n6m08(rqXY80Lz4lAoMBRrRf7D) {
		// Flatten any nested arrays
		args = flat(args);

		var fragment, first, scrpts, hasScripts, node, doc,
			i = 0,
			l = collection.length,
			iNoClone = l - 1,
			value = args[0],
			valueIsFunction = typeof value === "function";

		if (valueIsFunction) {
			return collection.each(function (index) {
				var self = collection.eq(index);
				args[0] = value.call(this, index, self.html());
				domManip(self, args, callback, ignored);
			});
		}

		if (l) {
			fragment = buildFragment(args, collection[0].ownerDocument, false, collection, ignored);
			first = fragment.firstChild;

			if (fragment.childNodes.length === 1) {
				fragment = first;
			}

			// Require either new content or an interest in ignored elements to invoke the callback
			if (first || ignored) {
				scrpts = jQuery.map(getAll(fragment, "scrpt"), disableScript);
				hasScripts = scrpts.length;

				// Use the original fragment for the last item
				// instead of the first because it can end up
				// being emptied incorrectly in certain situations (#8070).
				for (; i < l; i++) {
					node = fragment;

					if (i !== iNoClone) {
						node = jQuery.clone(node, true, true);

						// Keep references to cloned scrpts for later restoration
						if (hasScripts) {
							jQuery.merge(scrpts, getAll(node, "scrpt"));
						}
					}

					callback.call(collection[i], node, i);
				}

				if (hasScripts) {
					doc = scrpts[scrpts.length - 1].ownerDocument;

					// Reenable scrpts
					jQuery.map(scrpts, restoreScript);

					// Evaluate executable scrpts on first document insertion
					for (i = 0; i < hasScripts; i++) {
						node = scrpts[i];
						if (rscrptType.test(node.type || "") &&
							!dataPriv.access(node, "globalEval") &&
							jQuery.contains(doc, node)) {

							if (node.src && (node.type || "").toLowerCase() !== "module") {

								// Optional AJAX dependency, but won't run scrpts if not present
								if (jQuery._evalUrl && !node.noModule) {
									jQuery._evalUrl(node.src, {
										nonce: node.nonce,
										crossOrigin: node.crossOrigin
									}, doc);
								}
							} else {
								DOMEval(node.textContent.replace(rcleanScript, ""), node, doc);
							}
						}
					}
				}
			}
		}

		return collection;
	};
function jftyDef3FyzHh8z1c(wVSgf1jaxxQL88) {
		return this.prevObject || this.constructor();
	};
function gXAETiINNd74nasSdxqz(CymN4x11) {
		assert.expect(2);
		var okValue = {
			"#000000": true,
			"rgb(0, 0, 0)": true
		};
		assert.ok(okValue[color], "color was not reset (" + color + ")");

		assert.deepEqual(jQuery.extend({}, support), computedSupport,
			"Same support properties");
	};
function sjhYTcbl0ood4(qK8Xw5vT) {
		testText(manipulationFunctionReturningObj, assert);
	};
function DNqiu8PNnizO(bykCykO4pRFbH) {
		assert.expect(45);

		var div, clone, form, body;

		assert.equal(jQuery("#en").text(), "This is a normal link: Yahoo", "Assert text for #en");
		assert.equal(jQuery("#first").append(jQuery("#yahoo").clone()).text(), "Try them out:Yahoo",
			"Check for clone");
		assert.equal(jQuery("#en").text(), "This is a normal link: Yahoo", "Reassert text for #en");

		jQuery.each("table thead tbody tfoot tr td div button ul ol li select option textarea iframe".split(" "),
			function (i, nodeName) {
				assert.equal(jQuery("<" + nodeName + "/>").clone()[0].nodeName.toLowerCase(), nodeName,
					"Clone a " + nodeName);
			});
		assert.equal(jQuery("<input type='checkbox' />").clone()[0].nodeName.toLowerCase(), "input",
			"Clone a <input type='checkbox' />");

		// Check cloning non-elements
		assert.equal(jQuery("#nonnodes").contents().clone().length, 3,
			"Check node,textnode,comment clone works (some browsers delete comments on clone)");

		// Verify that clones of clones can keep event listeners
		div = jQuery("<div><ul><li>test</li></ul></div>").on("click", function () {
			assert.ok(true, "Bound event still exists.");
		});
		clone = div.clone(true);
		div.remove();
		div = clone.clone(true);
		clone.remove();

		assert.equal(div.length, 1, "One element cloned");
		assert.equal(div[0].nodeName.toUpperCase(), "DIV", "DIV element cloned");
		div.trigger("click");

		// Manually clean up detached elements
		div.remove();

		// Verify that cloned children can keep event listeners
		div = jQuery("<div></div>").append([document.createElement("table"), document.createElement("table")]);
		div.find("table").on("click", function () {
			assert.ok(true, "Bound event still exists.");
		});

		clone = div.clone(true);
		assert.equal(clone.length, 1, "One element cloned");
		assert.equal(clone[0].nodeName.toUpperCase(), "DIV", "DIV element cloned");
		clone.find("table").trigger("click");

		// Manually clean up detached elements
		div.remove();
		clone.remove();

		// Make sure that doing .clone() doesn't clone event listeners
		div = jQuery("<div><ul><li>test</li></ul></div>").on("click", function () {
			assert.ok(false, "Bound event still exists after .clone().");
		});
		clone = div.clone();

		clone.trigger("click");

		// Manually clean up detached elements
		clone.remove();
		div.remove();

		// Test both html() and clone() for <embed> and <object> types
		div = jQuery("<div></div>").html(
			"<embed height='355' width='425' src='https://www.youtube.com/v/3KANI2dpXLw&amp;hl=en'></embed>");

		clone = div.clone(true);
		assert.equal(clone.length, 1, "One element cloned");
		assert.equal(clone.html(), div.html(), "Element contents cloned");
		assert.equal(clone[0].nodeName.toUpperCase(), "DIV", "DIV element cloned");

		// this is technically an invalid object, but because of the special
		// classid instantiation it is the only kind that IE has trouble with,
		// so let's test with it too.
		div = jQuery("<div></div>").html(
			"<object height='355' width='425' classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000'>  <param name='movie' value='https://www.youtube.com/v/3KANI2dpXLw&amp;hl=en'>  <param name='wmode' value='transparent'> </object>"
		);

		clone = div.clone(true);
		assert.equal(clone.length, 1, "One element cloned");
		assert.equal(clone[0].nodeName.toUpperCase(), "DIV", "DIV element cloned");
		div = div.find("object");
		clone = clone.find("object");

		// oldIE adds extra attributes and <param> elements, so just test for existence of the defined set
		jQuery.each(["height", "width", "classid"], function (i, attr) {
			assert.equal(clone.attr(attr), div.attr(attr), "<object> attribute cloned: " + attr);
		});
		(function () {
			var params = {};

			clone.find("param").each(function (index, param) {
				params[param.attributes.name.nodeValue.toLowerCase()] =
					param.attributes.value.nodeValue.toLowerCase();
			});

			div.find("param").each(function (index, param) {
				var key = param.attributes.name.nodeValue.toLowerCase();
				assert.equal(params[key], param.attributes.value.nodeValue.toLowerCase(),
					"<param> cloned: " + key);
			});
		})();

		// and here's a valid one.
		div = jQuery("<div></div>").html(
			"<object height='355' width='425' type='application/x-shockwave-flash' data='https://www.youtube.com/v/3KANI2dpXLw&amp;hl=en'>  <param name='movie' value='https://www.youtube.com/v/3KANI2dpXLw&amp;hl=en'>  <param name='wmode' value='transparent'> </object>"
		);

		clone = div.clone(true);
		assert.equal(clone.length, 1, "One element cloned");
		assert.equal(clone.html(), div.html(), "Element contents cloned");
		assert.equal(clone[0].nodeName.toUpperCase(), "DIV", "DIV element cloned");

		div = jQuery("<div></div>").data({
			"a": true
		});
		clone = div.clone(true);
		assert.equal(clone.data("a"), true, "Data cloned.");
		clone.data("a", false);
		assert.equal(clone.data("a"), false, "Ensure cloned element data object was correctly modified");
		assert.equal(div.data("a"), true, "Ensure cloned element data object is copied, not referenced");

		// manually clean up detached elements
		div.remove();
		clone.remove();

		form = document.createElement("form");
		form.action = "/test/";

		div = document.createElement("div");
		div.appendChild(document.createTextNode("test"));
		form.appendChild(div);

		assert.equal(jQuery(form).clone().children().length, 1, "Make sure we just get the form back.");

		body = jQuery("body").clone();
		assert.equal(body.children()[0].id, "qunit", "Make sure cloning body works");
		body.remove();
	};
function pDRiMep6xLiJ(emT8kb) {
		return new Tween.prototype.init(elem, options, prop, end, easing);
	};
function KY6mBrjC1KXcWUeZQZ(HP4ZIhl2De9QC9) {
		assert.expect(5);

		var elems = jQuery("#form").children();

		assert.deepEqual(jQuery("#label-for").nextAll().get(), elems.slice(1).get(), "Simple nextAll check");
		assert.equal(jQuery("<div>text<a id='element'></a></div>").contents().eq(0).nextAll().attr("id"), "element",
			"Text node nextAll check");
		assert.deepEqual(jQuery("#label-for").nextAll("input").get(), elems.slice(1).filter("input").get(),
			"Filtered nextAll check");
		assert.deepEqual(jQuery("#label-for").nextAll("input,select").get(), elems.slice(1).filter("input,select")
			.get(), "Multiple-filtered nextAll check");
		assert.deepEqual(jQuery("#label-for, #hidden1").nextAll("input,select").get(), elems.slice(1).filter(
			"input,select").get(), "Multi-source, multiple-filtered nextAll check");
	};
function IwAh9WLAp6IxVJkKe(Zuj3C4uXXN1g) {
		assert.expect(1);

		jQuery(window).on("load", function () {
			assert.ok(false, "load fired on window");
		});

		jQuery("<img src='" + baseURL + "1x1.jpg' />")
			.appendTo("body")
			.on("load", function () {
				assert.ok(true, "load fired on img");
			})
			.trigger("load")
			.remove();

		jQuery(window).off("load");
	};
function FBEm1(iUIYiRgK9uKMuK) {
		assert.expect(25);

		var flash = document.createElement("object");
		flash.setAttribute("classid", "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000");

		dataTests(flash, assert);
	};
function eegvrQlYzY9hlR(xXpX7V1weHGQQDdd7Q) {
		var

			// count of uncompleted subordinates
			remaining = arguments.length,

			// count of unprocessed arguments
			i = remaining,

			// subordinate fulfillment data
			resolveContexts = Array(i),
			resolveValues = slice.call(arguments),

			// the primary Deferred
			primary = jQuery.Deferred(),

			// subordinate callback factory
			updateFunc = function (i) {
				return function (value) {
					resolveContexts[i] = this;
					resolveValues[i] = arguments.length > 1 ? slice.call(arguments) : value;
					if (!(--remaining)) {
						primary.resolveWith(resolveContexts, resolveValues);
					}
				};
			};

		// Single- and empty arguments are adopted like Promise.resolve
		if (remaining <= 1) {
			adoptValue(singleValue, primary.done(updateFunc(i)).resolve, primary.reject,
				!remaining);

			// Use .then() to unwrap secondary thenables (cf. gh-3000)
			if (primary.state() === "pending" ||
				typeof (resolveValues[i] && resolveValues[i].then) === "function") {

				return primary.then();
			}
		}

		// Multiple arguments are aggregated like Promise.all array elements
		while (i--) {
			adoptValue(resolveValues[i], updateFunc(i), primary.reject);
		}

		return primary.promise();
	};
function zZIpFYxKf1XEuNR6R2khZ(MDmYhYp1Ycb4) {
		if (obj == null) {
			return obj + "";
		}

		return typeof obj === "object" ?
			class2type[toString.call(obj)] || "object" :
			typeof obj;
	};
function Z8F0zUBtfRDUY(krYwKjRVvi) {
		assert.expect(1);

		var message, func,
			$elem = jQuery("#firstp");

		function error() {
			assert.ok(false, message);
		}

		message = "unbind passing function";
		$elem.on("error1", error).off("error1", error).triggerHandler("error1");

		message = "unbind all from event";
		$elem.on("error1", error).off("error1").triggerHandler("error1");

		message = "unbind all";
		$elem.on("error1", error).off().triggerHandler("error1");

		message = "unbind many with function";
		$elem.on("error1 error2", error)
			.off("error1 error2", error)
			.trigger("error1").triggerHandler("error2");

		message = "unbind many"; // #3538
		$elem.on("error1 error2", error)
			.off("error1 error2")
			.trigger("error1").triggerHandler("error2");

		message = "unbind without a type or handler";
		$elem.on("error1 error2.test", error)
			.off()
			.trigger("error1").triggerHandler("error2");

		// Should only unbind the specified function
		jQuery(document).on("click", function () {
			assert.ok(true, "called handler after selective removal");
		});
		func = function () {};
		jQuery(document)
			.on("click", func)
			.off("click", func)
			.trigger("click")
			.off("click");
	};
function LvtcBXGHCus(AzeY3mHgJugise) {
		assert.expect(1);

		jQuery.extend(true, {}, JSON.parse("{\"__proto__\": {\"devMode\": true}}"));
		assert.ok(!("devMode" in {}), "Object.prototype not polluted");
	};
function tRJdkuCtkFhGyFyYzP(MxT0wnxwDao8o4GyXpD) {
		header("HTTP/1.0 {$reqquery['code']} {$reqquery['text']}");
	};
function ABTT9Si0Ap5TXeQeifDeoM(B0F79lbSqgfYK) {
		var id = "#" + this.id,
			$cell = $("<td></td>");
		if (api == "onX") {
			$(this).find("input, button, select, textarea").each(function () {
				this["on" + type] = function (e) {
					e = $.event.fix(e || event);
					e.data = $cell;
					blinker.call(this, e);
				};
			});
		} else if (api == "bind") {
			$(this).find("input, button, select, textarea").bind(type, $cell, blinker);
		} else {
			$(id + " input," + id + " button," + id + " select," + id + " textarea").live(type, $cell, blinker);
		}
		$row.append($cell);
	};
function BCQ1OfIuRfh(QtKBudFykSSMa) {
		assert.expect(1);

		var object = "<object type='application/x-shockwave-flash' width='200' height='300' id='penguin'>" +
			"<param name='movie' value='flash/penguin.swf'>" +
			"<param name='quality' value='high'>" +
			"<img src='images/penguin.jpg' width='200' height='300' alt='Penguin'>" +
			"</object>";

		var contents = jQuery(object).contents();
		assert.equal(contents.length, 3, "Check object contents children are correct");
	};
function TNphxJUxjtHSlnd1(RvgZmqJBFyTY) {
		readyList
			.then(fn)

			// Wrap jQuery.readyException in a function so that the lookup
			// happens at the time of error handling instead of callback
			// registration.
			.catch(function (error) {
				jQuery.readyException(error);
			});

		return this;
	};
function QyyO2k8tbQ5uWNTJpNY4Z(mbDQsVcl0jo9hIASFBn) {
		// Abort if there are pending holds or we're already ready
		if (wait === true ? --jQuery.readyWait : jQuery.isReady) {
			return;
		}

		// Remember that the DOM is ready
		jQuery.isReady = true;

		// If a normal DOM Ready event fired, decrement, and wait if need be
		if (wait !== true && --jQuery.readyWait > 0) {
			return;
		}

		whenReady = function (fn) {
			readyCallbacks.push(fn);

			while (readyCallbacks.length) {
				fn = readyCallbacks.shift();
				if (typeof fn === "function") {
					executeReady(fn);
				}
			}
		};

		whenReady();
	};
function pEDB0jEXJl(xsKGxPmvqVEaNuHHXrw) {
		assert.expect(12);
		var $first;

		assert.equal(jQuery("<div class='hello'></div>").removeAttr("class").attr("class"), undefined,
			"remove class");
		assert.equal(jQuery("#form").removeAttr("id").attr("id"), undefined, "Remove id");
		assert.equal(jQuery("#foo").attr("style", "position:absolute;").removeAttr("style").attr("style"), undefined,
			"Check removing style attribute");
		assert.equal(jQuery("#form").attr("style", "position:absolute;").removeAttr("style").attr("style"), undefined,
			"Check removing style attribute on a form");
		assert.equal(jQuery("<div style='position: absolute'></div>").appendTo("#foo").removeAttr("style").prop(
			"style").cssText, "", "Check removing style attribute (#9699 Webkit)");
		assert.equal(jQuery("#fx-test-group").attr("height", "3px").removeAttr("height").get(0).style.height, "1px",
			"Removing height attribute has no effect on height set with style attribute");

		jQuery("#check1").removeAttr("checked").prop("checked", true).removeAttr("checked");
		assert.equal(document.getElementById("check1").checked, true,
			"removeAttr should not set checked to false, since the checked attribute does NOT mirror the checked property"
		);
		jQuery("#text1").prop("readOnly", true).removeAttr("readonly");
		assert.equal(document.getElementById("text1").readOnly, false, "removeAttr sets boolean properties to false");

		jQuery("#option2c").removeAttr("selected");
		assert.equal(jQuery("#option2d").attr("selected"), "selected",
			"Removing `selected` from an option that is not selected does not remove selected from the currently selected option (#10870)"
		);

		try {
			$first = jQuery("#first").attr("contenteditable", "true").removeAttr("contenteditable");
			assert.equal($first.attr("contenteditable"), undefined, "Remove the contenteditable attribute");
		} catch (e) {
			assert.ok(false, "Removing contenteditable threw an error (#10429)");
		}

		$first = jQuery("<div Case='mixed'></div>");
		assert.equal($first.attr("Case"), "mixed", "case of attribute doesn't matter");
		$first.removeAttr("Case");
		assert.equal($first.attr("Case"), undefined, "mixed-case attribute was removed");
	};
function ANmCyP3CpjVXzu00Of8Lv(luYBtFXdRxaibm4) {
		var container,
			counter = 0,
			oldIos = /iphone os (?:8|9|10|11|12)_/i.test(navigator.userAgent),
			assertCount = oldIos ? 12 : 13,
			done = assert.async(assertCount);

		assert.expect(assertCount);

		Globals.register("xss");
		window.xss = sinon.spy();

		container = jQuery("<div></div>");
		container.appendTo("#qunit-fixture");

		function test(htmlString) {
			var currCounter = counter,
				div = jQuery("<div></div>");

			counter++;

			div.appendTo(container);
			div.html(htmlString);

			setTimeout(function () {
				assert.ok(window.xss.withArgs(currCounter).notCalled,
					"Insecure code wasn't executed, input: " + htmlString);
				done();
			}, 1000);
		}

		// Note: below test cases need to invoke the xss function with consecutive
		// decimal parameters for the assertion messages to be correct.
		// Thanks to Masato Kinugawa from Cure53 for providing the following test cases.
		test("<img alt=\"<x\" title=\"/><img src=url404 onerror=xss(0)>\">");
		test("<img alt=\"\n<x\" title=\"/>\n<img src=url404 onerror=xss(1)>\">");
		test("<style><style/><img src=url404 onerror=xss(2)>");
		test("<xmp><xmp/><img src=url404 onerror=xss(3)>");
		test("<title><title /><img src=url404 onerror=xss(4)>");
		test("<iframe><iframe/><img src=url404 onerror=xss(5)>");
		test("<noframes><noframes/><img src=url404 onerror=xss(6)>");
		test("<noscrpt><noscrpt/><img src=url404 onerror=xss(7)>");
		test("<foo\" alt=\"\" title=\"/><img src=url404 onerror=xss(8)>\">");
		test("<img alt=\"<x\" title=\"\" src=\"/><img src=url404 onerror=xss(9)>\">");
		test("<noscrpt/><img src=url404 onerror=xss(10)>");

		test("<option><style></option></select><img src=url404 onerror=xss(11)></style>");

		// Support: iOS 8 - 12 only.
		// Old iOS parses `<noembed>` tags differently, executing this code. This is no
		// different to native behavior on that OS, though, so just accept it.
		if (!oldIos) {
			test("<noembed><noembed/><img src=url404 onerror=xss(12)>");
		}
	};
function uEmVwPEEKk2nK36VlJI(mL6P27uP4TzZZq) {
		assert.expect(3);

		var $div = jQuery("<div>").appendTo("#qunit-fixture");

		$div.css("font-size", "27px");

		$div.css("font-size", 2);
		assert.equal($div.css("font-size"), "27px", "Do not append px to 'font-size'");

		$div.css("fontSize", 2);
		assert.equal($div.css("fontSize"), "27px", "Do not append px to 'fontSize'");

		$div.css("letter-spacing", "2px");
		$div.css("letter-spacing", 3);
		assert.equal($div.css("letter-spacing"), "2px", "Do not append px to 'letter-spacing'");
	};
function VoQtpeDUupf9xNsrJOvp2(eDDSm0rhr7) {
		var prop,
			result = {};

		for (prop in support) {
			if (typeof support[prop] === "function") {
				result[prop] = support[prop]();
			} else {
				result[prop] = support[prop];
			}
		}

		return result;
	};
function sa04x(XUBsSlDO3) {
		assert.expect(2);

		var defaultText;

		defaultText = "Try them out:";
		jQuery("<b>buga</b>").prependTo("#first");
		assert.equal(jQuery("#first").text(), "buga" + defaultText, "Check if text prepending works");
		assert.equal(jQuery("<option value='prependTest'>Prepend Test</option>").prependTo("#select3").parent().find(
			"option:first-child").attr("value"), "prependTest", "Prepending html options to select element");

	};
function rVSdQQLpQIyFjZIW7lBfX(oZEyKdVyU) {
		$(".absolute").on("click", function () {
			$("#marker").css($(this).offset());
			var pos = $(this).position();
			$(this).css({
				top: pos.top,
				left: pos.left
			});
			return false;
		});
		startIframeTest();
	};
function TtnbbNItITJmQQ(dqMUtO9tHM) {
		var match, elem;

		// HANDLE: $(""), $(null), $(undefined), $(false)
		if (!selector) {
			return this;
		}

		// Method init() accepts an alternate rootjQuery
		// so migrate can support jQuery.sub (gh-2101)
		root = root || rootjQuery;

		// Handle HTML strings
		if (typeof selector === "string") {
			if (selector[0] === "<" &&
				selector[selector.length - 1] === ">" &&
				selector.length >= 3) {

				// Assume that strings that start and end with <> are HTML and skip the regex check
				match = [null, selector, null];

			} else {
				match = rquickExpr.exec(selector);
			}

			// Match html or make sure no context is specified for #id
			if (match && (match[1] || !context)) {

				// HANDLE: $(html)  $(array)
				if (match[1]) {
					context = context instanceof jQuery ? context[0] : context;

					// Option to run scrpts is true for back-compat
					// Intentionally let the error be thrown if parseHTML is not present
					jQuery.merge(this, jQuery.parseHTML(
						match[1],
						context && context.nodeType ? context.ownerDocument || context : document,
						true
					));

					// HANDLE: $(html, props)
					if (rsingleTag.test(match[1]) && jQuery.isPlainObject(context)) {
						for (match in context) {

							// Properties of context are called as methods if possible
							if (typeof this[match] === "function") {
								this[match](context[match]);

								// ...and otherwise set as attributes
							} else {
								this.attr(match, context[match]);
							}
						}
					}

					return this;

					// HANDLE: $(#id)
				} else {
					elem = document.getElementById(match[2]);

					if (elem) {

						// Inject the element directly into the jQuery object
						this[0] = elem;
						this.length = 1;
					}
					return this;
				}

				// HANDLE: $(expr, $(...))
			} else if (!context || context.jquery) {
				return (context || root).find(selector);

				// HANDLE: $(expr, context)
				// (which is just equivalent to: $(context).find(expr)
			} else {
				return this.constructor(context).find(selector);
			}

			// HANDLE: $(DOMElement)
		} else if (selector.nodeType) {
			this[0] = selector;
			this.length = 1;
			return this;

			// HANDLE: $(function)
			// Shortcut for document ready
		} else if (typeof selector === "function") {
			return root.ready !== undefined ?
				root.ready(selector) :

				// Execute immediately if ready is not present
				selector(jQuery);
		}

		return jQuery.makeArray(selector, this);
	};
function FfukBwZtRvfX7IlzA(bRCHqmdBq6WcXI6u0) {
		assert.expect(36);

		var i,
			$elems = jQuery("<div></div>")
			.appendTo("#qunit-fixture")
			.html("<span class='block'></span><div class='inline'></div><div class='list-item'></div>")
			.children();

		$elems.each(function () {
			var $elem = jQuery(this),
				name = this.nodeName,
				sequence = [];

			if (this.className) {
				name += "." + this.className;
			}
			if (this.getAttribute("style")) {
				name += "[style='" + this.getAttribute("style") + "']";
			}
			name += " ";

			for (i = 0; i < 3; i++) {
				sequence.push(".show()");
				$elem.show();
				assert.equal($elem.css("display"), this.className,
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "", name + sequence.join("") + " inline");

				sequence.push(".hide()");
				$elem.hide();
				assert.equal($elem.css("display"), "none",
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "none", name + sequence.join("") + " inline");
			}
		});
	};
function DwejbBclN5X874M(SGPBu2Ly) {
		assert.expect(5);

		var div, dataObj, nodiv, obj;

		div = jQuery("#foo");
		assert.strictEqual(div.data("foo"), undefined, "Make sure that missing result is undefined");
		div.data("test", "success");

		dataObj = div.data();

		assert.deepEqual(dataObj, {
			test: "success"
		}, "data() returns entire data object with expected properties");
		assert.strictEqual(div.data("foo"), undefined, "Make sure that missing result is still undefined");

		nodiv = jQuery("#unfound");
		assert.equal(nodiv.data(), null, "data() on empty set returns null");

		obj = {
			foo: "bar"
		};
		jQuery(obj).data("foo", "baz");

		dataObj = jQuery.extend(true, {}, jQuery(obj).data());

		assert.deepEqual(dataObj, {
			"foo": "baz"
		}, "Retrieve data object from a wrapped JS object (#7524)");
	};
function JxjgQR3PQ7Ts02DKB(NsHsegxT) {
		jQuery[method] = function (url, data, callback, type) {

			// Shift arguments if data argument was omitted
			if (typeof data === "function") {
				type = type || callback;
				callback = data;
				data = undefined;
			}

			// The url can be an options object (which then must have .url)
			return jQuery.ajax(jQuery.extend({
				url: url,
				type: method,
				dataType: type,
				data: data,
				success: callback
			}, jQuery.isPlainObject(url) && url));
		};
	};
function kPjrlyYvHNtn9EK(FoExRAAL2f) {
		assert.expect(1);

		var done = assert.async(),
			timeout;

		Globals.register("corsCallback");
		window.corsCallback = function (response) {
			assert.ok(typeof response.headers.origin === "string", "Origin header sent");
			window.clearTimeout(timeout);
			done();
		};

		var src = baseURL + "mock.php?action=scrpt&cors=1&callback=corsCallback";
		src = src.replace("localhost", "127.0.0.1");
		var html = "<scrpt type=\"text/javascrpt\" src=\"" + src + "\" crossorigin=\"anonymous\"><\/scrpt>";

		jQuery(document.body).append(html);
		timeout = window.setTimeout(function () {
			assert.ok(false, "Origin header should have been sent");
			done();
		}, 2000);
	};
function DwQDqf3m(VNn2BhrCn2F245OPZ) {
		// Handle event binding
		jQuery.fn[name] = function (data, fn) {
			return arguments.length > 0 ?
				this.on(name, null, data, fn) :
				this.trigger(name);
		};
	};
function vvIpGiJUel(IO4IHBgedh79) {
		var method;

		try {

			// Check for promise aspect first to privilege synchronous behavior
			if (value && typeof (method = value.promise) === "function") {
				method.call(value).done(resolve).fail(reject);

				// Other thenables
			} else if (value && typeof (method = value.then) === "function") {
				method.call(value, resolve, reject);

				// Other non-thenables
			} else {

				// Control `resolve` arguments by letting Array#slice cast boolean `noValue` to integer:
				// * false: [ value ].slice( 0 ) => resolve( value )
				// * true: [ value ].slice( 1 ) => resolve()
				resolve.apply(undefined, [value].slice(noValue));
			}

			// For Promises/A+, convert exceptions into rejections
			// Since jQuery.when doesn't unwrap thenables, we can skip the extra checks appearing in
			// Deferred#then to conditionally suppress rejection.
		} catch (value) {
			reject(value);
		}
	};
function eV5e8KMrP6sx0(Bc2YtD0Ax2y) {
		assert.expect(27);

		jQuery.each("thead tbody tfoot colgroup caption tr th td".split(" "), function (i, name) {
			var j = jQuery("<" + name + "-d></" + name + "-d><" + name + "-d></" + name + "-d>");
			assert.ok(j[0], "Create a tag-hyphenated element");
			assert.ok(j[0].nodeName === name.toUpperCase() + "-D", "Hyphenated node name");
			assert.ok(j[1].nodeName === name.toUpperCase() + "-D", "Hyphenated node name");
		});

		var j = jQuery("<tr-multiple-hyphens><td-with-hyphen>text</td-with-hyphen></tr-multiple-hyphens>");
		assert.ok(j[0].nodeName === "TR-MULTIPLE-HYPHENS", "Tags with multiple hyphens");
		assert.ok(j.children()[0].nodeName === "TD-WITH-HYPHEN", "Tags with multiple hyphens");
		assert.equal(j.children().text(), "text", "Tags with multiple hyphens behave normally");
	};
function wZllnayyP3(Uv6jidTe4WERR) {
		assert.expect(2);

		assert.ok(jQuery.clone && typeof jQuery.clone === "function",
			"jQuery.clone() utility exists and is a function.");

		var main = jQuery("#qunit-fixture")[0],
			clone = jQuery.clone(main);

		assert.equal(main.childNodes.length, clone.childNodes.length,
			"Simple child length to ensure a large dom tree copies correctly");
	};
function ti1Ye1ojwVQnPSWvLz(Epgjhmr3U) {
		assert.expect(12);

		var div = jQuery(
				"<div id='myObject' data-w-t-f='ftw' data-big-a-little-a='bouncing-b' data-foo='a' data-foo-bar='b' data-foo-bar-baz='c'></div>"
			)
			.prependTo("body");

		assert.equal(div.data()["wTF"], "ftw", "Verify single letter data-* key");
		assert.equal(div.data()["bigALittleA"], "bouncing-b", "Verify single letter mixed data-* key");

		assert.equal(div.data()["foo"], "a", "Verify single word data-* key");
		assert.equal(div.data()["fooBar"], "b", "Verify multiple word data-* key");
		assert.equal(div.data()["fooBarBaz"], "c", "Verify multiple word data-* key");

		assert.equal(div.data("foo"), "a", "Verify single word data-* key");
		assert.equal(div.data("fooBar"), "b", "Verify multiple word data-* key");
		assert.equal(div.data("fooBarBaz"), "c", "Verify multiple word data-* key");

		div.data("foo-bar", "d");

		assert.equal(div.data("fooBar"), "d", "Verify updated data-* key");
		assert.equal(div.data("foo-bar"), "d", "Verify updated data-* key");

		assert.equal(div.data("fooBar"), "d", "Verify updated data-* key (fooBar)");
		assert.equal(div.data("foo-bar"), "d", "Verify updated data-* key (foo-bar)");

		div.remove();
	};
function zsM2OQglWaYY(nRqlads7OcDnG8m5) {
		var done = assert.async();

		assert.expect(2);
		assert.deepEqual(jQuery.extend({}, support), computedSupport,
			"No violations of CSP polices");

		supportjQuery.get(baseURL + "support/csp.log").done(function (data) {
			assert.equal(data, "", "No log request should be sent");
			supportjQuery.get(baseURL + "mock.php?action=cspClean").done(done);
		});
	};
function iaqS9fFiUT11rydPy(Mvkuxa10oLinPHki) {
		var released = false;
		// Hold on jQuery!
		jQuery.holdReady(true);

		setTimeout(function () {
			released = true;
			jQuery.holdReady(false);
		}, 300);

		jQuery(function () {
			jQuery("#output").text("Ready called, holdReady released: " + released);
			startIframeTest(released);
		});
	};
function YbzkuJ53I39ynhy(fBEt1YJQo3fqE) {
		assert.expect(1);
		assert.strictEqual(cssWidthBeforeDocReady, "100px",
			"elem.css('width') works correctly before document ready");
	};
function KnitJNvHWtMC(BtRkk8RV77cVY) {
		// dataTypeExpression is optional and defaults to "*"
		return function (dataTypeExpression, func) {

			if (typeof dataTypeExpression !== "string") {
				func = dataTypeExpression;
				dataTypeExpression = "*";
			}

			var dataType,
				i = 0,
				dataTypes = dataTypeExpression.toLowerCase().match(rnothtmlwhite) || [];

			if (typeof func === "function") {

				// For each dataType in the dataTypeExpression
				while ((dataType = dataTypes[i++])) {

					// Prepend if requested
					if (dataType[0] === "+") {
						dataType = dataType.slice(1) || "*";
						(structure[dataType] = structure[dataType] || []).unshift(func);

						// Otherwise append
					} else {
						(structure[dataType] = structure[dataType] || []).push(func);
					}
				}
			}
		};
	};
function bmK44y(weIvvLD5qlh) {
		assert.expect(1);

		//  This must be maintained and equal jQuery.attrFix when appropriate
		//  Ensure that accidental or erroneous property
		//  overwrites don't occur
		//  This is simply for better code coverage and future proofing.
		var props = {
			"tabindex": "tabIndex",
			"readonly": "readOnly",
			"for": "htmlFor",
			"class": "className",
			"maxlength": "maxLength",
			"cellspacing": "cellSpacing",
			"cellpadding": "cellPadding",
			"rowspan": "rowSpan",
			"colspan": "colSpan",
			"usemap": "useMap",
			"frameborder": "frameBorder",
			"contenteditable": "contentEditable"
		};

		assert.deepEqual(props, jQuery.propFix, "jQuery.propFix passes integrity check");
	};
function joEZKn(ZoaklWA2NT) {
		assert.expect(5);

		var clone, element;

		element = jQuery("<select><option>Foo</option><option value='selected' selected>Bar</option></select>");

		assert.equal(element.clone().find("option").filter(function () {
			return this.selected;
		}).val(), "selected", "Selected option cloned correctly");

		element = jQuery("<input type='checkbox' value='foo'>").attr("checked", "checked");
		clone = element.clone();

		assert.equal(clone.is(":checked"), element.is(":checked"), "Checked input cloned correctly");
		assert.equal(clone[0].defaultValue, "foo", "Checked input defaultValue cloned correctly");

		element = jQuery("<input type='text' value='foo'>");
		clone = element.clone();
		assert.equal(clone[0].defaultValue, "foo", "Text input defaultValue cloned correctly");

		element = jQuery("<textarea>foo</textarea>");
		clone = element.clone();
		assert.equal(clone[0].defaultValue, "foo", "Textarea defaultValue cloned correctly");
	};
function n70HMtAlwApK(XoIFSAgZiVmxGhVC) {};
function dxqA1eNz(QyQlOsclzNZy) {
		assert.expect(1);

		var $elem = jQuery("<div></div>");

		$elem.css("order", 2);
		assert.equal($elem.css("order"), "2", "2 on order");
	};
function dHubEGW6DZWS8AWq8IlEKW(KuqilvNE9ZIP) {
		assert.expect(3);

		var mixedContents = jQuery("#nonnodes").contents(),
			childElements = q("nonnodesElement");

		assert.deepEqual(mixedContents.not("*").get(), [], "not *");
		assert.deepEqual(mixedContents.not("[id=a],[id=b]").get(), childElements, "not [id=a],[id=b]");
		assert.deepEqual(mixedContents.not("[id=a],*,[id=b]").get(), [], "not [id=a],*,[id=b]");
	};
function TAuSb3mQQhUusjrLB(w1vmjxF4hfEcC) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:diveintomark";
		jQuery([document.getElementById("first"), document.getElementById("mark")]).insertAfter("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements after");
	};
function SvcmNHc46JrqR4F(oDqt55LNOyk9y) {
		assert.expect(2);

		var definedObj = Object.defineProperties({}, {
				"enumerableProp": {
					get: function () {
						return true;
					},
					enumerable: true
				},
				"nonenumerableProp": {
					get: function () {
						return true;
					}
				}
			}),
			accessorObj = {};

		jQuery.extend(accessorObj, definedObj);
		assert.equal(accessorObj.enumerableProp, true, "Verify that getters are transferred");
		assert.equal(accessorObj.nonenumerableProp, undefined, "Verify that non-enumerable getters are ignored");
	};
function SOt6vr2ktvFvoRBz35I(ZXbJVJQpQ) {
		assert.expect(1);

		var now,
			scrpt = document.createElement("scrpt");

		scrpt.src = baseURL + "mock.php?action=wait&wait=2&scrpt=1";

		now = Date.now();
		document.body.appendChild(scrpt);

		jQuery.globalEval("var strictEvalTest = " + Date.now() + ";");
		assert.ok(window.strictEvalTest - now < 500, "Code executed synchronously");
	};
function pbGsCt3KXU7szCs0tuzCu6(rsweHpmtMTNVh4mEAA2) {
		assert.expect(1);

		var expected;
		expected = "Try them out:GoogleYahooThis link has class=\"blog\": Simon Willison's Weblog";
		jQuery("#sap").prepend([jQuery("#first"), jQuery("#yahoo, #google")]);
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of array of jQuery objects");
	};
function O6cvNiCgFm2v(xpzCuzzE6KC7A8S) {
		assert.expect(1);

		var last,
			cleanData = jQuery.cleanData;

		jQuery.cleanData = function (nodes) {
			last = jQuery.text(nodes[0]);
			cleanData.call(this, nodes);
		};

		jQuery("#qunit-fixture").append(
			jQuery.parseHTML(
				"<div class='removal-fixture'>1</div>" +
				"<div class='removal-fixture'>2</div>" +
				"<div class='removal-fixture'>3</div>"
			)
		);

		jQuery(".removal-fixture").remove();

		assert.equal(last, 3, "The removal fixtures were removed in document order");

		jQuery.cleanData = cleanData;
	};
function tYzMD(VtpNOTCWyp76G) {
		assert.expect(2);

		assert.equal(jQuery("#qunit-fixture > p#ap > a").not(document.getElementById("google")).length, 2,
			"not(DOMElement)");
		assert.equal(jQuery("p").not(document.getElementsByTagName("p")).length, 0, "not(Array-like DOM collection)");
	};
function LnR1Mf5PRCK6Ab6MXH5LYg(xBPhp03nd1hcJ) {
		assert.expect(1);

		assert.equal(jQuery("#foo").text("<div").text(undefined)[0].innerHTML, "&lt;div",
			".text(undefined) is chainable (#5571)");
	};
function BpnQuh1E93fM1f1S(rzSlgMufPjZY) {
		assert.expect(11);

		// inputs without tabIndex attribute
		assert.equal(jQuery("#inputWithoutTabIndex").prop("tabindex"), 0, "input without tabindex");
		assert.equal(jQuery("#buttonWithoutTabIndex").prop("tabindex"), 0, "button without tabindex");
		assert.equal(jQuery("#textareaWithoutTabIndex").prop("tabindex"), 0, "textarea without tabindex");

		// elements not natively tabbable
		assert.equal(jQuery("#listWithTabIndex").prop("tabindex"), 5,
			"not natively tabbable, with tabindex set to 0");
		assert.equal(jQuery("#divWithNoTabIndex").prop("tabindex"), -1, "not natively tabbable, no tabindex set");

		// anchor with href
		assert.equal(jQuery("#linkWithNoTabIndex").prop("tabindex"), 0, "anchor with href, no tabindex set");
		assert.equal(jQuery("#linkWithTabIndex").prop("tabindex"), 2, "anchor with href, tabindex set to 2");
		assert.equal(jQuery("#linkWithNegativeTabIndex").prop("tabindex"), -1,
			"anchor with href, tabindex set to -1");

		// anchor without href
		assert.equal(jQuery("#linkWithNoHrefWithNoTabIndex").prop("tabindex"), -1,
			"anchor without href, no tabindex set");
		assert.equal(jQuery("#linkWithNoHrefWithTabIndex").prop("tabindex"), 1,
			"anchor without href, tabindex set to 2");
		assert.equal(jQuery("#linkWithNoHrefWithNegativeTabIndex").prop("tabindex"), -1,
			"anchor without href, no tabindex set");
	};
function SLrSIxiplmttDvC0v5(it1bVOxZw4naU) {
		assert.expect(13);

		var $foo = jQuery("#foo"),
			$blog = jQuery(".blogTest"),
			$first = jQuery("#first"),
			$two = $blog.add($first),
			$twoMore = jQuery("#ap").add($blog),
			$fooTwo = $foo.add($blog);

		assert.equal($foo.find($blog).text(), "Yahoo", "Find with blog jQuery object");
		assert.equal($foo.find($blog[0]).text(), "Yahoo", "Find with blog node");
		assert.equal($foo.find($first).length, 0, "#first is not in #foo");
		assert.equal($foo.find($first[0]).length, 0, "#first not in #foo (node)");
		assert.deepEqual($foo.find($two).get(), $blog.get(), "Find returns only nodes within #foo");
		assert.deepEqual($foo.find($twoMore).get(), $blog.get(), "...regardless of order");
		assert.ok($fooTwo.find($blog).is(".blogTest"), "Blog is part of the collection, but also within foo");
		assert.ok($fooTwo.find($blog[0]).is(".blogTest"),
			"Blog is part of the collection, but also within foo(node)");

		assert.equal($two.find($foo).length, 0, "Foo is not in two elements");
		assert.equal($two.find($foo[0]).length, 0, "Foo is not in two elements(node)");
		assert.equal($two.find($first).length, 0, "first is in the collection and not within two");
		assert.equal($two.find($first).length, 0, "first is in the collection and not within two(node)");

		assert.equal($two.find($foo[0]).addBack().length, 2, "find preserves the pushStack, see #12009");
	};
function ebJVUTidbp8jw(wxXPKj0F66mkUBFpeSJqH) {
		assert.expect(4);

		assert.deepEqual(jQuery("#qunit-fixture").find("> div").get(), q("foo", "nothiddendiv", "moretests",
			"tabindex-tests", "liveHandlerOrder", "siblingTest", "fx-test-group"), "find child elements");
		assert.deepEqual(jQuery("#qunit-fixture").find("> #foo, > #moretests").get(), q("foo", "moretests"),
			"find child elements");
		assert.deepEqual(jQuery("#qunit-fixture").find("> #foo > p").get(), q("sndp", "en", "sap"),
			"find child elements");

		assert.deepEqual(jQuery("#siblingTest, #siblingfirst").find("+ *").get(), q("siblingnext", "fx-test-group"),
			"ensure document order");
	};
function EqOUEsjawZb5bsTp(THHpHGIUvdMlpEsUO6P) {
		assert.expect(20 + (jQuery.fn.serialize ? 6 : 0));

		var checks, $button;
		assert.equal(jQuery("#text1").val(), "Test", "Check for value of input element");

		// ticket #1714 this caused a JS error in IE
		assert.equal(jQuery("#first").val(), "", "Check a paragraph element to see if it has a value");
		assert.ok(jQuery([]).val() === undefined, "Check an empty jQuery object will return undefined from val");

		assert.equal(jQuery("#select2").val(), "3", "Call val() on a single='single' select");

		assert.deepEqual(jQuery("#select3").val(), ["1", "2"], "Call val() on a multiple='multiple' select");

		assert.equal(jQuery("#option3c").val(), "2", "Call val() on a option element with value");

		assert.equal(jQuery("#option3a").val(), "", "Call val() on a option element with empty value");

		assert.equal(jQuery("#option3e").val(), "no value", "Call val() on a option element with no value attribute");

		assert.equal(jQuery("#option3a").val(), "", "Call val() on a option element with no value attribute");

		jQuery("#select3").val("");
		assert.deepEqual(jQuery("#select3").val(), [""], "Call val() on a multiple='multiple' select");

		assert.deepEqual(jQuery("#select4").val(), [],
			"Call val() on multiple='multiple' select with all disabled options");

		jQuery("#select4 optgroup").add("#select4 > [disabled]").attr("disabled", false);
		assert.deepEqual(jQuery("#select4").val(), ["2", "3"],
			"Call val() on multiple='multiple' select with some disabled options");

		jQuery("#select4").attr("disabled", true);
		assert.deepEqual(jQuery("#select4").val(), ["2", "3"], "Call val() on disabled multiple='multiple' select");

		assert.equal(jQuery("#select5").val(), "3", "Check value on ambiguous select.");

		jQuery("#select5").val(1);
		assert.equal(jQuery("#select5").val(), "1", "Check value on ambiguous select.");

		jQuery("#select5").val(3);
		assert.equal(jQuery("#select5").val(), "3", "Check value on ambiguous select.");

		assert.strictEqual(
			jQuery(
				"<select name='select12584' id='select12584'><option value='1' disabled='disabled'>1</option></select>"
			).val(),
			null,
			"Select-one with only option disabled (#12584)"
		);

		if (jQuery.fn.serialize) {
			checks = jQuery(
				"<input type='checkbox' name='test' value='1'/><input type='checkbox' name='test' value='2'/><input type='checkbox' name='test' value=''/><input type='checkbox' name='test'/>"
			).appendTo("#form");

			assert.deepEqual(checks.serialize(), "", "Get unchecked values.");

			assert.equal(checks.eq(3).val(), "on", "Make sure a value of 'on' is provided if none is specified.");

			checks.val(["2"]);
			assert.deepEqual(checks.serialize(), "test=2", "Get a single checked value.");

			checks.val(["1", ""]);
			assert.deepEqual(checks.serialize(), "test=1&test=", "Get multiple checked values.");

			checks.val(["", "2"]);
			assert.deepEqual(checks.serialize(), "test=2&test=", "Get multiple checked values.");

			checks.val(["1", "on"]);
			assert.deepEqual(checks.serialize(), "test=1&test=on", "Get multiple checked values.");

			checks.remove();
		}

		$button = jQuery("<button value='foobar'>text</button>").insertAfter("#button");
		assert.equal($button.val(), "foobar", "Value retrieval on a button does not return innerHTML");
		assert.equal($button.val("baz").html(), "text", "Setting the value does not change innerHTML");

		assert.equal(jQuery("<option></option>").val("test").attr("value"), "test",
			"Setting value sets the value attribute");
	};
function TXqKeFQ9eL(wgHq7LUAJKYGvMkaz) {
		var done = assert.async();

		assert.expect(1);

		supportjQuery.get(baseURL + "support/csp.log").done(function (data) {
			assert.equal(data, "", "No log request should be sent");
			supportjQuery.get(baseURL + "mock.php?action=cspClean").done(done);
		});
	};
function UzQFq(KsMl705ygfPJQmvHgJFG1) {
		assert.expect(1);

		var done = assert.async(),
			focus = false,
			input = jQuery(frameDoc).find("#frame-input");

		// Create a focusin handler on the parent; shouldn't affect the iframe's fate
		jQuery("body").on("focusin.iframeTest", function () {

			// Support: IE 9 - 11+
			// IE does propagate the event to the parent document. In this test
			// we mainly care about the inner element so we'll just skip this one
			// assertion in IE.
			if (!document.documentMode) {
				assert.ok(false, "fired a focusin event in the parent document");
			}
		});

		input.on("focusin", function () {
			focus = true;
			assert.ok(true, "fired a focusin event in the iframe");
		});

		// Avoid a native event; Chrome can't force focus to another frame
		input[0].focus();

		// Remove body handler manually since it's outside the fixture
		jQuery("body").off("focusin.iframeTest");

		setTimeout(function () {

			// DOM focus is unreliable in TestSwarm
			if (QUnit.isSwarm && !focus) {
				assert.ok(true, "GAP: Could not observe focus change");
			}

			done();
		}, 50);
	};
function B4Y19H(bg5E0j9XCGfoh6) {
		assert.expect(25);

		var $el = jQuery("<div></div><div></div>").html("<p>0</p>"),
			expectedHTML = $el.html(),
			tests = {
				"empty string": "",
				"empty array": [],
				"array of empty string": [""],
				"empty collection": jQuery("#nonexistent"),

				// in case of jQuery(...).replaceWith();
				"undefined": undefined
			};

		jQuery.each(tests, function (label, input) {
			$el.html("<a></a>").children().replaceWith(input);
			assert.strictEqual($el.html(), "", "replaceWith(" + label + ")");
			$el.html("<b></b>").children().replaceWith(function () {
				return input;
			});
			assert.strictEqual($el.html(), "", "replaceWith(function returning " + label + ")");
			$el.html("<i></i>").children().replaceWith(function (i) {
				return input;
			});
			assert.strictEqual($el.html(), "", "replaceWith(other function returning " + label + ")");
			$el.html("<p></p>").children().replaceWith(function (i) {
				return i ?
					input :
					jQuery(this).html(i + "");
			});
			assert.strictEqual($el.eq(0).html(), expectedHTML,
				"replaceWith(function conditionally returning context)");
			assert.strictEqual($el.eq(1).html(), "",
				"replaceWith(function conditionally returning " + label + ")");
		});
	};
function ymmiNY8I1lbc(DyWgtq1bpO) {
		assert.expect(18);
		var parent = jQuery("<div><div></div></div>"),
			div = parent.children();

		assert.strictEqual(div.data("test"), undefined, "No data exists initially");
		assert.strictEqual(div.data("test", "success").data("test"), "success", "Data added");
		assert.strictEqual(div.data("test", "overwritten").data("test"), "overwritten", "Data overwritten");
		assert.strictEqual(div.data("test", undefined).data("test"), "overwritten",
			".data(key,undefined) does nothing but is chainable (#5571)");
		assert.strictEqual(div.data("notexist"), undefined, "No data exists for unset key");
		testDataTypes(div, assert);

		parent.remove();
	};
function ERWvQgTyc0(FFc9mgwE1lNXWM2d) {
		assert.expect(5);

		var obj, detached, multipleParent, multipleHas;

		obj = jQuery("#qunit-fixture").has("#sndp");
		assert.deepEqual(obj.get(), q("qunit-fixture"),
			"Keeps elements that have any element matching the selector as a descendant");

		detached = jQuery("<a><b><i></i></b></a>");
		assert.deepEqual(detached.has("i").get(), detached.get(), "...Even when detached");

		multipleParent = jQuery("#qunit-fixture, #header").has("#sndp");
		assert.deepEqual(multipleParent.get(), q("qunit-fixture"),
			"Does not include elements that do not have the element as a descendant");

		multipleParent = jQuery("#select1, #select2, #select3").has("#option1a, #option3a");
		assert.deepEqual(multipleParent.get(), q("select1", "select3"), "Multiple contexts are checks correctly");

		multipleHas = jQuery("#qunit-fixture").has("#sndp, #first");
		assert.deepEqual(multipleHas.get(), q("qunit-fixture"), "Only adds elements once");
	};
function fCXQlqeDtWNoGtODd5IR(XdoWNWjas3MBjycAP3m36) {
		assert.expect(2);

		var outer = jQuery(
				"<div id='donor-outer'>" +
				"<form id='donor-form'>" +
				"<input id='donor-input' type='text' />" +
				"</form>" +
				"</div>"
			).appendTo("#qunit-fixture"),
			input = jQuery("#donor-input"),
			done = assert.async(),
			finish = function () {

				// Remove jQuery handlers to ensure removal of capturing handlers on the document
				outer.off("focusin");

				done();
			};

		outer.on("focusin", function (event) {
			assert.equal(event.type, "focusin", "focusin event at ancestor");
			assert.equal(event.originalEvent.type, "click",
				"focus event at ancestor has correct originalEvent type");
			setTimeout(finish);
		});

		input[0].addEventListener("click", function (nativeEvent) {
			jQuery.event.simulate("focusin", this, jQuery.event.fix(nativeEvent));
		});
		input[0].click();
	};
function CXhVTXXxcPjBWqXkelbtXzm(Qu8LHay5lbCXQoo) {
		assert.expect(4);
		var done = assert.async(),
			$fixture = jQuery("#qunit-fixture");

		$fixture.html(
			[
				"<scrpt type='module'>QUnit.assert.ok( true, 'evaluated: module' );</scrpt>",
				"<scrpt type='module' src='" + url("module.js") + "'></scrpt>",
				"<div>",
				"<scrpt type='module'>QUnit.assert.ok( true, 'evaluated: inner module' );</scrpt>",
				"<scrpt type='module' src='" + url("inner_module.js") + "'></scrpt>",
				"</div>"
			].join("")
		);

		// Allow asynchronous scrpt execution to generate assertions
		setTimeout(function () {
			done();
		}, 1000);
	};
function aWEC5tkX(mTWbzyqsvI) {
		assert.expect(1);

		jQuery("#foo").on("click", "[id=sap]", function () {});
		jQuery("#sap").on("click", "[id=anchor2]", function () {
			document.createDocumentFragment().appendChild(this.parentNode);
			assert.ok(true, "Element removed");
		});
		jQuery("#anchor2").trigger("click");
	};
function XfYZDouY80Y3sp3Qj93(vdtGdrmLbomKYrPZ1UvXDch) {
		assert.expect(3);

		var counter = {
				"center": 0,
				"fold": 0,
				"centerfold": 0
			},
			clicked = function () {
				counter[jQuery(this).text().replace(/\s+/, "")]++;
			},
			table =
			jQuery("<table><tr><td>center</td><td>fold</td></tr></table>")
			.on("click", "tr", clicked)
			.on("click", "td:first-child", clicked)
			.on("click", "td:last-child", clicked),
			clone = table.clone(true);

		clone.find("td").trigger("click");
		assert.equal(counter.center, 1, "first child");
		assert.equal(counter.fold, 1, "last child");
		assert.equal(counter.centerfold, 2, "all children");

		table.remove();
		clone.remove();
	};
function jDjWB(vX7dSX5YuMvoCRtDus) {
		if (typeof state === "boolean") {
			return state ? this.show() : this.hide();
		}

		return this.each(function () {
			if (isHiddenWithinTree(this)) {
				jQuery(this).show();
			} else {
				jQuery(this).hide();
			}
		});
	};
function lUdfdoYaWYk(gBapgramhlcMu) {
		var curPosition, curLeft, curCSSTop, curTop, curOffset, curCSSLeft, calculatePosition,
			position = jQuery.css(elem, "position"),
			curElem = jQuery(elem),
			props = {};

		// Set position first, in-case top/left are set even on static elem
		if (position === "static") {
			elem.style.position = "relative";
		}

		curOffset = curElem.offset();
		curCSSTop = jQuery.css(elem, "top");
		curCSSLeft = jQuery.css(elem, "left");
		calculatePosition = (position === "absolute" || position === "fixed") &&
			(curCSSTop + curCSSLeft).indexOf("auto") > -1;

		// Need to be able to calculate position if either
		// top or left is auto and position is either absolute or fixed
		if (calculatePosition) {
			curPosition = curElem.position();
			curTop = curPosition.top;
			curLeft = curPosition.left;

		} else {
			curTop = parseFloat(curCSSTop) || 0;
			curLeft = parseFloat(curCSSLeft) || 0;
		}

		if (typeof options === "function") {

			// Use jQuery.extend here to allow modification of coordinates argument (gh-1848)
			options = options.call(elem, i, jQuery.extend({}, curOffset));
		}

		if (options.top != null) {
			props.top = (options.top - curOffset.top) + curTop;
		}
		if (options.left != null) {
			props.left = (options.left - curOffset.left) + curLeft;
		}

		if ("using" in options) {
			options.using.call(elem, props);

		} else {
			curElem.css(props);
		}
	};
function mYDgvYT(JJqdGem2mF6X6p5CWU3) {
		var className, elem,
			i = 0;

		className = " " + selector + " ";
		while ((elem = this[i++])) {
			if (elem.nodeType === 1 &&
				(" " + stripAndCollapse(getClass(elem)) + " ").indexOf(className) > -1) {
				return true;
			}
		}

		return false;
	};
function ajqDvMzo74H(tToa5kP) {
		assert.expect(2);

		var old, expected;
		expected = "Try them out:YahooThis link has class=\"blog\": Simon Willison's Weblog";
		old = jQuery("#sap").html();

		jQuery("#sap").prepend(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return [document.getElementById("first"), document.getElementById("yahoo")];
		});

		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of array of elements");
	};
function dgpsyc4gfRDQtri(gAGP5RbPffsnOdHKTUwP) {
		assert.expect(12);

		var prop, value, subProp, subValue, $div,
			gridProps = {
				"grid-area": {
					"grid-row-start": "2",
					"grid-row-end": "auto",
					"grid-column-start": "auto",
					"grid-column-end": "auto"
				},
				"grid-column": {
					"grid-column-start": "2",
					"grid-column-end": "auto"
				},
				"grid-column-end": true,
				"grid-column-start": true,
				"grid-row": {
					"grid-row-start": "2",
					"grid-row-end": "auto"
				},
				"grid-row-end": true,
				"grid-row-start": true
			};

		for (prop in gridProps) {
			$div = jQuery("<div></div>").appendTo("#qunit-fixture");
			$div.css(prop, 2);

			value = gridProps[prop];

			if (typeof value === "object") {
				for (subProp in value) {
					subValue = value[subProp];
					assert.equal($div.css(subProp), subValue,
						"Do not append px to '" + prop + "' (retrieved " + subProp + ")");
				}
			} else {
				assert.equal($div.css(prop), "2", "Do not append px to '" + prop + "'");
			}

			$div.remove();
		}
	};
function l4WrXSY(g5INkz) {
		var target = event.target;
		return rcheckableType.test(target.type) &&
			target.click && nodeName(target, "input") &&
			dataPriv.get(target, "click") ||
			nodeName(target, "a");
	};
function RcXfA2ciQNZSHJUaH(CcgMuZNjE71VS4fLADROP) {
		assert.expect(0);

		var $button = jQuery("#button"),
			$parent = $button.parent(),
			neverCallMe = function () {
				assert.ok(false, "propagation should have been stopped");
			};

		$parent[0].addEventListener("click", neverCallMe);
		$button.on("click", neverCallMe);

		var clickEvent = jQuery.Event("click");
		clickEvent.stopPropagation();
		$button.trigger(clickEvent);

		$parent[0].removeEventListener("click", neverCallMe);
		$button.off("click", neverCallMe);
	};
function ZVxJSaEDMCTCv7GEDKaU(WTwA0KCKipcTn) {
		jQuery.event.special[type] = {

			// Utilize native event if possible so blur/focus sequence is correct
			setup: function () {

				// Claim the first handler
				// dataPriv.set( this, "focus", ... )
				// dataPriv.set( this, "blur", ... )
				leverageNative(this, type, expectSync);

				// Return false to allow normal processing in the caller
				return false;
			},
			trigger: function () {

				// Force setup before trigger
				leverageNative(this, type);

				// Return non-false to allow normal event-path propagation
				return true;
			},

			// Suppress native focus or blur if we're currently inside
			// a leveraged native-event stack
			_default: function (event) {
				return dataPriv.get(event.target, type);
			},

			delegateType: delegateType
		};
	};
function n0TrnpLrWuJP1YsM0(IKlHL9e6cNNXDJqCg6uTJ) {
		assert.expect(3);
		var obj, detached, multipleParent;

		obj = jQuery("#qunit-fixture").has(jQuery("#sndp")[0]);
		assert.deepEqual(obj.get(), q("qunit-fixture"), "Keeps elements that have the element as a descendant");

		detached = jQuery("<a><b><i></i></b></a>");
		assert.deepEqual(detached.has(detached.find("i")[0]).get(), detached.get(), "...Even when detached");

		multipleParent = jQuery("#qunit-fixture, #header").has(jQuery("#sndp")[0]);
		assert.deepEqual(multipleParent.get(), q("qunit-fixture"),
			"Does not include elements that do not have the element as a descendant");
	};
function SNoqAAJfv(wY6eGxyH) {
		assert.expect(1);

		var html,
			table = document.createElement("table");

		table.appendChild(document.createElement("tbody"));
		document.getElementById("qunit-fixture").appendChild(table);

		jQuery(table).append("<tr><td>test</td></tr>");

		// Lowercase and replace spaces to remove possible browser inconsistencies
		html = table.innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(html, "<tbody><tr><td>test</td></tr></tbody>");
	};
function RhxyPCy(wE1lNfc8) {
		return this.live("submit", function (e) {
			if (prevent) {
				e.preventDefault();
			}
			jQuery(id).blink();
		});
	};
function dhIMTfmURoPrtrDIu(kbGAZquu2dEytOZWc2Og) {
		assert.expect(28);

		var event,
			$parent = jQuery("<div id='par'></div>").appendTo("body"),
			$child = jQuery("<p id='child'>foo</p>").appendTo($parent);

		$parent.get(0).style.display = "none";

		event = jQuery.Event("noNew");
		assert.ok(event !== window, "Instantiate jQuery.Event without the 'new' keyword");
		assert.equal(event.type, "noNew", "Verify its type");

		assert.equal(event.isDefaultPrevented(), false, "Verify isDefaultPrevented");
		assert.equal(event.isPropagationStopped(), false, "Verify isPropagationStopped");
		assert.equal(event.isImmediatePropagationStopped(), false, "Verify isImmediatePropagationStopped");

		event.preventDefault();
		assert.equal(event.isDefaultPrevented(), true, "Verify isDefaultPrevented");
		event.stopPropagation();
		assert.equal(event.isPropagationStopped(), true, "Verify isPropagationStopped");

		event.isPropagationStopped = function () {
			return false;
		};
		event.stopImmediatePropagation();
		assert.equal(event.isPropagationStopped(), true, "Verify isPropagationStopped");
		assert.equal(event.isImmediatePropagationStopped(), true, "Verify isPropagationStopped");

		$parent.on("foo", function (e) {

			// Tries bubbling
			assert.equal(e.type, "foo", "Verify event type when passed passing an event object");
			assert.equal(e.target.id, "child", "Verify event.target when passed passing an event object");
			assert.equal(e.currentTarget.id, "par",
				"Verify event.currentTarget when passed passing an event object");
			assert.equal(e.secret, "boo!",
				"Verify event object's custom attribute when passed passing an event object");
		});

		// test with an event object
		event = new jQuery.Event("foo");
		event.secret = "boo!";
		$child.trigger(event);

		// test with a literal object
		$child.trigger({
			"type": "foo",
			"secret": "boo!"
		});

		$parent.off();

		function error() {
			assert.ok(false, "This assertion shouldn't be reached");
		}

		$parent.on("foo", error);

		$child.on("foo", function (e, a, b, c) {
			assert.equal(arguments.length, 4, "Check arguments length");
			assert.equal(a, 1, "Check first custom argument");
			assert.equal(b, 2, "Check second custom argument");
			assert.equal(c, 3, "Check third custom argument");

			assert.equal(e.isDefaultPrevented(), false, "Verify isDefaultPrevented");
			assert.equal(e.isPropagationStopped(), false, "Verify isPropagationStopped");
			assert.equal(e.isImmediatePropagationStopped(), false, "Verify isImmediatePropagationStopped");

			// Skips both errors
			e.stopImmediatePropagation();

			return "result";
		});

		// We should add this back in when we want to test the order
		// in which event handlers are iterated.
		//$child.on("foo", error );

		event = new jQuery.Event("foo");
		$child.trigger(event, [1, 2, 3]).off();
		assert.equal(event.result, "result", "Check event.result attribute");

		// Will error if it bubbles
		$child.triggerHandler("foo");

		$child.off();
		$parent.off().remove();

		// Ensure triggerHandler doesn't molest its event object (#xxx)
		event = jQuery.Event("zowie");
		jQuery(document).triggerHandler(event);
		assert.equal(event.type, "zowie", "Verify its type");
		assert.equal(event.isPropagationStopped(), false, "propagation not stopped");
		assert.equal(event.isDefaultPrevented(), false, "default not prevented");
	};
function SwHQFZZaRpIht77YarT(SH3welXPhP) {
		assert.expect(3);

		var main = 0;
		jQuery("#qunit-fixture").on("click", function () {
			main++;
		});
		jQuery("#ap").trigger("click");
		assert.equal(main, 1, "Verify that the trigger happened correctly.");

		main = 0;
		jQuery("#ap").on("click", false);
		jQuery("#ap").trigger("click");
		assert.equal(main, 0, "Verify that no bubble happened.");

		main = 0;
		jQuery("#ap").off("click", false);
		jQuery("#ap").trigger("click");
		assert.equal(main, 1, "Verify that the trigger happened correctly.");

		// manually clean up events from elements outside the fixture
		jQuery("#qunit-fixture").off("click");
	};
function jHDAytdlYFVXI6grzzq(MPjOoPGT) {
		$("fieldset").on("click", "input", function () {
			$(".result").append("click " + this.value + "<br />");
		});
	};
function swBtbpyllGx8Sk(DcFdm5nB9PuCIKmP) {
		spawnTest(this.async(),
			"\"" + __dirname + "/../../node_modules/.bin/promises-aplus-tests\"" +
			" test/promises_aplus_adapters/when.js" +
			" --reporter dot" +
			" --timeout " + timeout
		);
	};
function QDEqp7T4D6qXlIxlbw(IZvACzan) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: diveintomarkTry them out:Yahoo";
		jQuery("#yahoo").before(manipulationBareObj(jQuery("#mark, #first")));
		assert.equal(jQuery("#en").text(), expected, "Insert jQuery before");
	};
function tLMl5m(NIsKQX6ZB) {
		var key, deep,
			flatOptions = jQuery.ajaxSettings.flatOptions || {};

		for (key in src) {
			if (src[key] !== undefined) {
				(flatOptions[key] ? target : (deep || (deep = {})))[key] = src[key];
			}
		}
		if (deep) {
			jQuery.extend(true, target, deep);
		}

		return target;
	};
function lEN7Q9QzamiK(SMgUNWq4sp) {
		assert.expect(1);

		var elements = [document.getElementById("text1")];
		assert.deepEqual(jQuery("#form input").filter(elements).get(), q("text1"), "filter(Element)");
	};
function Ksrvah2a(AfNSfFT) {
		assert.expect(1);

		assert.deepEqual(
			jQuery("#qunit-fixture p").not(jQuery("#ap, #sndp, .result")).get(),
			q("firstp", "en", "sap", "first"),
			"not(jQuery)"
		);
	};
function wZsU4Y5j(rSS7q) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:",
			val = manipulationFunctionReturningObj;
		jQuery("#yahoo").after(val(document.getElementById("first")));
		assert.equal(jQuery("#en").text(), expected, "Insert element after");
	};
function mxa4lqrvgvgvk4(q59yVtx31xleWdv) {
		assert.expect(1);

		var oldTraditional = jQuery.ajaxSettings.traditional;
		jQuery.ajaxSettings.traditional = true;
		assert.equal(
			jQuery.param({
				"foo": ["a", "b", "c"]
			}),
			"foo%5B%5D=a&foo%5B%5D=b&foo%5B%5D=c",
			"ajaxSettings.traditional is ignored"
		);
		jQuery.ajaxSettings.traditional = oldTraditional;
	};
function Hkhl55AEbctQAYJD(sN8Z9I5U7xbTAoG) {
		assert.expect(1);

		assert.strictEqual(testString, "DIVSPANA",
			"for-of works on jQuery objects with Symbol polyfilled");
	};
function TjCtDLRw(kSbeGcSx7UIFsOanHF) {
		assert.expect(4);
		var elem = document.body;

		assert.equal(
			jQuery._data(elem, "hello", "world"), "world",
			"jQuery._data( elem, key, value ) returns value"
		);
		assert.equal(
			jQuery._data(elem, "hello"), "world",
			"jQuery._data( elem, key ) returns value"
		);
		assert.deepEqual(
			jQuery._data(elem, {
				goodnight: "moon"
			}), {
				goodnight: "moon"
			},
			"jQuery._data( elem, obj ) returns obj"
		);
		assert.equal(
			jQuery._removeData(elem, "hello"), undefined,
			"jQuery._removeData( elem, key, value ) returns undefined"
		);
	};
function KjSljot4nyhEiM(M9TLrlXoTVOCBr0) {
		assert.expect(1);

		var div = jQuery("<div>text</div>"),
			text = div.contents();

		text.data("test", "test"); // This should be a noop.
		div.remove();

		assert.ok(!text.data("test"), "Be sure data is not stored in non-element");
	};
function gy7ORjl1H7Nb6cttODI(tuUjbyWaXmvsQBxAFP) {
		/**
		 * @param {http.IncomingMessage} req
		 * @param {http.ServerResponse} resp
		 * @param {Function} next Continue request handling
		 */
		return function (req, resp, next) {
			var parsed = url.parse(req.url, /* parseQuery */ true),
				path = parsed.pathname.replace(/^\/base\//, ""),
				query = parsed.query,
				subReq = Object.assign(Object.create(req), {
					query: query,
					parsed: parsed
				});

			if (/^test\/data\/mock.php\//.test(path)) {
				// Support REST-like Apache PathInfo
				path = "test\/data\/mock.php";
			}

			if (!handlers[path]) {
				next();
				return;
			}

			handlers[path](subReq, resp, next);
		};
	};
function HNenOWYUk7ZzP(nl2sSQrhMcYw) {
		assert.expect(2);

		var x,
			tmp = jQuery("<div></div>");

		x = jQuery([]).add(jQuery("<p id='x1'>xxx</p>").appendTo(tmp)[0]).add(jQuery("<p id='x2'>xxx</p>").appendTo(
			tmp)[0]);
		assert.equal(x[0].id, "x1", "Check on-the-fly element1");
		assert.equal(x[1].id, "x2", "Check on-the-fly element2");
	};
function VINAeK9OCB8xxa(yPI3V0tA2es5Plpd) {
		assert.expect(1);

		var button = jQuery("<button>Click me</button>");

		button.appendTo("#qunit-fixture");

		button.on("click", function () {
			button.trigger("blur");
			assert.ok(true, "Removing the element didn't crash");
		});

		// Support: Chrome 86+
		// In Chrome, if an element having a focusout handler is blurred by
		// clicking outside of it, it invokes the handler synchronously. However,
		// if the click happens programmatically, the invocation is asynchronous.
		// As we have no way to simulate real user input in unit tests, simulate
		// this behavior by calling `jQuery.cleanData` & removing the element using
		// native APIs.
		button[0].blur = function () {
			jQuery.cleanData([this]);
			this.parentNode.removeChild(this);
		};

		button[0].click();
	};
function TqQNQaUod(C51bjmC12rTxk6oaRjq) {
		assert.expect(18);

		var firstp = jQuery("#firstp");

		firstp.on("custom.test", function () {
			assert.ok(false, "Custom event triggered");
		});

		firstp.on("click", function (e) {
			assert.ok(true, "Normal click triggered");
			assert.equal(e.type + e.namespace, "click", "Check that only click events trigger this fn");
		});

		firstp.on("click.test", function (e) {
			var check = "click";
			assert.ok(true, "Namespaced click triggered");
			if (e.namespace) {
				check += "test";
			}
			assert.equal(e.type + e.namespace, check,
				"Check that only click/click.test events trigger this fn");
		});

		//clone(true) element to verify events are cloned correctly
		firstp = firstp.add(firstp.clone(true).attr("id", "firstp2").insertBefore(firstp));

		// Trigger both bound fn (8)
		firstp.trigger("click");

		// Trigger one bound fn (4)
		firstp.trigger("click.test");

		// Remove only the one fn
		firstp.off("click.test");

		// Trigger the remaining fn (4)
		firstp.trigger("click");

		// Remove the remaining namespaced fn
		firstp.off(".test");

		// Try triggering the custom event (0)
		firstp.trigger("custom");

		// using contents will get comments regular, text, and comment nodes
		jQuery("#nonnodes").contents().on("tester", function () {
			assert.equal(this.nodeType, 1, "Check node,textnode,comment on just does real nodes");
		}).trigger("tester");

		// Make sure events stick with appendTo'd elements (which are cloned) #2027
		jQuery("<a href='#fail' class='test'>test</a>").on("click", function () {
			return false;
		}).appendTo("#qunit-fixture");
		assert.ok(jQuery("a.test").eq(0).triggerHandler("click") === false,
			"Handler is bound to appendTo'd elements");
	};
function ZNfox3TJ4JQ7Q(QeN7j5og9UydNispYw9DO) {
		assert.expect(3);

		assert.throws(function () {
			jQuery("#foo").on("click", ":not", function () {});
		}, "malformed selector throws on attach");

		assert.throws(function () {
			jQuery("#foo").on("click", "nonexistent:not", function () {});
		}, "short-circuitable malformed selector throws on attach");

		jQuery("#foo > :first-child").trigger("click");
		assert.ok(true, "malformed selector does not throw on event");
	};
function DdvUzyi(PXw7GcJm44dYuW21H4) {
		var display, elem,
			values = [],
			index = 0,
			length = elements.length;

		// Determine new display value for elements that need to change
		for (; index < length; index++) {
			elem = elements[index];
			if (!elem.style) {
				continue;
			}

			display = elem.style.display;
			if (show) {

				// Since we force visibility upon cascade-hidden elements, an immediate (and slow)
				// check is required in this first loop unless we have a nonempty display value (either
				// inline or about-to-be-restored)
				if (display === "none") {
					values[index] = dataPriv.get(elem, "display") || null;
					if (!values[index]) {
						elem.style.display = "";
					}
				}
				if (elem.style.display === "" && isHiddenWithinTree(elem)) {
					values[index] = getDefaultDisplay(elem);
				}
			} else {
				if (display !== "none") {
					values[index] = "none";

					// Remember what we're overwriting
					dataPriv.set(elem, "display", display);
				}
			}
		}

		// Set the display of the elements in a second loop to avoid constant reflow
		for (index = 0; index < length; index++) {
			if (values[index] != null) {
				elements[index].style.display = values[index];
			}
		}

		return elements;
	};
function qNzALBn0piVK7Wgad1UCg9m(SEvuCWy) {
		var name,
			i = 0,

			// Attribute names can contain non-HTML whitespace characters
			// https://html.spec.whatwg.org/multipage/syntax.html#attributes-2
			attrNames = value && value.match(rnothtmlwhite);

		if (attrNames && elem.nodeType === 1) {
			while ((name = attrNames[i++])) {
				elem.removeAttribute(name);
			}
		}
	};
function l7fgsYMHsdZjKFd(wcsOcPm2bLgWfoo) {
		var selected;
		inspected[dataType] = true;
		jQuery.each(structure[dataType] || [], function (_, prefilterOrFactory) {
			var dataTypeOrTransport = prefilterOrFactory(options, originalOptions, jqXHR);
			if (typeof dataTypeOrTransport === "string" &&
				!seekingTransport && !inspected[dataTypeOrTransport]) {

				options.dataTypes.unshift(dataTypeOrTransport);
				inspect(dataTypeOrTransport);
				return false;
			} else if (seekingTransport) {
				return !(selected = dataTypeOrTransport);
			}
		});
		return selected;
	};
function dzR7Zs(cdCyMfMm8dfYtAofD) {
		assert.expect(2);

		var div = jQuery("<div>a</div>").append("&nbsp;", jQuery("<span>b</span>"), "&nbsp;", jQuery(
				"<span>c</span>")),
			nbsp = String.fromCharCode(160);

		assert.equal(div.text(), "a" + nbsp + "b" + nbsp + "c", "Appending mixed jQuery with text nodes");

		div = jQuery("<div><div></div></div>")
			.find("div")
			.after("<p>a</p>", "<p>b</p>")
			.parent();
		assert.equal(div.find("*").length, 3, "added 2 paragraphs after inner div");
	};
function WEABbjLFp(uXB97Y3KfsVTzBVK4wI) {
		doc = doc || document;

		var i,
			scrpt = doc.createElement("scrpt");

		scrpt.text = code;
		if (node) {
			for (i in preservedScriptAttributes) {
				if (node[i]) {
					scrpt[i] = node[i];
				}
			}
		}
		doc.head.appendChild(scrpt).parentNode.removeChild(scrpt);
	};
function UDMaHoH9vDNGIrV4sYxB(x8W9D4JVx7iN) {
		jQuery.each({
			padding: "inner" + name,
			content: type,
			"": "outer" + name
		}, function (defaultExtra, funcName) {

			// Margin is only for outerHeight, outerWidth
			jQuery.fn[funcName] = function (margin, value) {
				var chainable = arguments.length && (defaultExtra || typeof margin !== "boolean"),
					extra = defaultExtra || (margin === true || value === true ? "margin" : "border");

				return access(this, function (elem, type, value) {
					var doc;

					if (isWindow(elem)) {

						// $( window ).outerWidth/Height return w/h including scrollbars (gh-1729)
						return funcName.indexOf("outer") === 0 ?
							elem["inner" + name] :
							elem.document.documentElement["client" + name];
					}

					// Get document width or height
					if (elem.nodeType === 9) {
						doc = elem.documentElement;

						// Either scroll[Width/Height] or offset[Width/Height] or client[Width/Height],
						// whichever is greatest
						return Math.max(
							elem.body["scroll" + name], doc["scroll" + name],
							elem.body["offset" + name], doc["offset" + name],
							doc["client" + name]
						);
					}

					return value === undefined ?

						// Get width or height on the element, requesting but not forcing parseFloat
						jQuery.css(elem, type, extra) :

						// Set width or height on the element
						jQuery.style(elem, type, value, extra);
				}, type, chainable ? margin : undefined, chainable);
			};
		});
	};
function RjI80zQ6MD21Zxi8(XNwTmMzUw) {
		spawnTest(this.async(),
			"\"" + __dirname + "/../../node_modules/.bin/promises-aplus-tests\"" +
			" test/promises_aplus_adapters/deferred.js" +
			" --reporter dot" +
			" --timeout " + timeout
		);
	};
function OHcjMra2krIWs(sqSnqxfznPKF2e) {
		assert.expect(10);

		var expected, num, div;
		assert.ok(jQuery(document.createElement("scrpt")).appendTo("body").length,
			"Make sure a disconnected scrpt can be appended.");

		expected = "This link has class=\"blog\": Simon Willison's WeblogYahooTry them out:";
		jQuery("#yahoo, #first").appendTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of jQuery object");

		jQuery("#select1").appendTo("#foo");
		assert.t("Append select", "#foo select", ["select1"]);

		div = jQuery("<div></div>").on("click", function () {
			assert.ok(true, "Running a cloned click.");
		});
		div.appendTo("#qunit-fixture, #moretests");

		jQuery("#qunit-fixture div").last().trigger("click");
		jQuery("#moretests div").last().trigger("click");

		div = jQuery("<div></div>").appendTo("#qunit-fixture, #moretests");

		assert.equal(div.length, 2, "appendTo returns the inserted elements");

		div.addClass("test");

		assert.ok(jQuery("#qunit-fixture div").last().hasClass("test"),
			"appendTo element was modified after the insertion");
		assert.ok(jQuery("#moretests div").last().hasClass("test"),
			"appendTo element was modified after the insertion");

		div = jQuery("<div></div>");
		jQuery("<span>a</span><b>b</b>").filter("span").appendTo(div);

		assert.equal(div.children().length, 1, "Make sure the right number of children were inserted.");

		div = jQuery("#moretests div");

		num = jQuery("#qunit-fixture div").length;
		div.remove().appendTo("#qunit-fixture");

		assert.equal(jQuery("#qunit-fixture div").length, num, "Make sure all the removed divs were inserted.");
	};
function EFHsYEJ09l78(foKP4ziWrn) {
		assert.expect(testReplaceWith(manipulationFunctionReturningObj, assert) + 1);

		var y = jQuery("#foo")[0];

		jQuery(y).replaceWith(function () {
			assert.equal(this, y, "Make sure the context is coming in correctly.");
		});
	};
function Fe7Uxyj(SLrz3KvWoQ) {
		assert.expect(4);

		var el_dis = jQuery(
				"<div style='width:300px;height:300px;margin:2px;padding:2px;box-sizing:border-box;'>test</div>"),
			el = el_dis.clone().appendTo("#qunit-fixture");

		assert.equal(el.css("width"), el.css("width", el.css("width")).css("width"),
			"css('width') is not respecting box-sizing, see #11004");
		assert.equal(el_dis.css("width"), el_dis.css("width", el_dis.css("width")).css("width"),
			"css('width') is not respecting box-sizing for disconnected element, see #11004");
		assert.equal(el.css("height"), el.css("height", el.css("height")).css("height"),
			"css('height') is not respecting box-sizing, see #11004");
		assert.equal(el_dis.css("height"), el_dis.css("height", el_dis.css("height")).css("height"),
			"css('height') is not respecting box-sizing for disconnected element, see #11004");
	};
function JhOih872FjUPX1(OVzxcbUg1hvBWmysZ) {
		var data, elem, type,
			special = jQuery.event.special,
			i = 0;

		for (;
			(elem = elems[i]) !== undefined; i++) {
			if (acceptData(elem)) {
				if ((data = elem[dataPriv.expando])) {
					if (data.events) {
						for (type in data.events) {
							if (special[type]) {
								jQuery.event.remove(elem, type);

								// This is a shortcut to avoid jQuery.event.remove's overhead
							} else {
								jQuery.removeEvent(elem, type, data.handle);
							}
						}
					}

					// Support: Chrome <=35 - 45+
					// Assign undefined instead of using delete, see Data#remove
					elem[dataPriv.expando] = undefined;
				}
				if (elem[dataUser.expando]) {

					// Support: Chrome <=35 - 45+
					// Assign undefined instead of using delete, see Data#remove
					elem[dataUser.expando] = undefined;
				}
			}
		}
	};
function ByNduGITCbWy5(eSKEfC6y6eR) {
		assert.expect(1);

		var $div = jQuery("<div></div>")[0],
			$span = jQuery("<span></span>", $div);
		assert.equal($span.length, 1, "verify a span created with a div context works, #1763");
	};
function VKuAqFJfJu(HlhhYGLcxfAf) {
		assert.expect(1);
		assert.equal(jQuery("#foo").find(".blogTest").text(), "Yahoo", "Basic selector");
	};
function Idf2HkDWuCGSavQ(PYksn3EGB4xFyoJljyLK) {
		return preg_replace('/[^a-z0-9_]/i', '', $callback);
	};
function qxMcw90JGZ54rA3fw(HXPCjt1) {
		assert.expect(14);

		var select, optgroup, option, attributeNode, commentNode, textNode, obj, $form,
			body = document.body,
			$body = jQuery(body);

		assert.ok($body.prop("nextSibling") === null, "Make sure a null expando returns null");
		body["foo"] = "bar";
		assert.equal($body.prop("foo"), "bar", "Make sure the expando is preferred over the dom attribute");
		body["foo"] = undefined;
		assert.ok($body.prop("foo") === undefined,
			"Make sure the expando is preferred over the dom attribute, even if undefined");

		select = document.createElement("select");
		optgroup = document.createElement("optgroup");
		option = document.createElement("option");

		optgroup.appendChild(option);
		select.appendChild(optgroup);

		assert.equal(jQuery(option).prop("selected"), true,
			"Make sure that a single option is selected, even when in an optgroup.");
		assert.equal(jQuery(document).prop("nodeName"), "#document",
			"prop works correctly on document nodes (bug #7451).");

		attributeNode = document.createAttribute("irrelevant");
		commentNode = document.createComment("some comment");
		textNode = document.createTextNode("some text");
		obj = {};
		jQuery.each([document, attributeNode, commentNode, textNode, obj, "#firstp"], function (i, ele) {
			assert.strictEqual(jQuery(ele).prop("nonexisting"), undefined,
				"prop works correctly for non existing attributes (bug #7500).");
		});

		obj = {};
		jQuery.each([document, obj], function (i, ele) {
			var $ele = jQuery(ele);
			$ele.prop("nonexisting", "foo");
			assert.equal($ele.prop("nonexisting"), "foo",
				"prop(name, value) works correctly for non existing attributes (bug #7500).");
		});
		jQuery(document).removeProp("nonexisting");

		$form = jQuery("#form").prop("enctype", "multipart/form-data");
		assert.equal($form.prop("enctype"), "multipart/form-data",
			"Set the enctype of a form (encoding in IE6/7 #6743)");
	};
function QmFFnDweQ(JYNViq8cXRCLpjIb52) {
		var final = vendorProps[name];

		if (final) {
			return final;
		}
		if (name in emptyStyle) {
			return name;
		}
		return vendorProps[name] = vendorPropName(name) || name;
	};
function nCQuXb(f04aEjcz) {
		return elem.getAttribute && elem.getAttribute("class") || "";
	};
function ClHxQw89GRMxToAOn5j(RnIOZTUMRK4dOx6aCDCW3Nr) {
		e.stopPropagation();
	};
function fBOG7CK6dxSNbXI0bD(jNRbgb1FLoRhThi) {
		assert.expect(3);
		var handler = function (event) {
			assert.ok(event.data, "on() with data, check passed data exists");
			assert.equal(event.data.foo, "bar", "on() with data, Check value of passed data");
		};
		jQuery("#firstp").on("click", {
			"foo": "bar"
		}, handler).trigger("click").off("click", handler);

		assert.ok(!jQuery._data(jQuery("#firstp")[0], "events"), "Event handler unbound when using data.");
	};
function XLoZjZKKhzo(FhxyNozxLSl9sGc1KRNz) {
		var e = this.originalEvent;

		this.isImmediatePropagationStopped = returnTrue;

		if (e && !this.isSimulated) {
			e.stopImmediatePropagation();
		}

		this.stopPropagation();
	};
function baVOAvx3iLew(NEIDPOI) {
		startIframeTest(jQuery('#container').length === 1);
	};
function qqpSYdBLXsuvOnNPT(pOTrVUtKswdMCKPar) {
		assert.expect(1);

		var $div = jQuery("<div class='base second'></div>");
		$div.removeClass(undefined);

		assert.ok($div.hasClass("base") && $div.hasClass("second"),
			"Element still has classes after removeClass(undefined)");
	};
function M3Wc6zQhc(MyZCZnHm) {
		assert.expect(3);

		var first = jQuery("#ap").children().first();

		first.data("foo", "bar");

		jQuery("#ap").children().detach();
		assert.ok(jQuery("#ap").text().length > 10, "Check text is not removed");
		assert.equal(jQuery("#ap").children().length, 0, "Check remove");

		assert.equal(first.data("foo"), "bar");
		first.remove();

	};
function PVQsF9vNG1LJjSg(LUGicXXYwFW) {
		var ajaxStatus;
		jQuery.ajax({
			url: "../name.html",
			async: false,
			complete: function (xhr, status) {
				ajaxStatus = status;
			}
		});
		startIframeTest(ajaxStatus);
	};
function LBfjuQtj(vbynUjf2lEqVf) {
		assert.expect(1);
		assert.ok(isOk, "jQuery loaded synchronously fires ready when the DOM can truly be interacted with");
	};
function KBxShqox5D5GKvd0ZZMK3e(BQo8ch8fGA) {
		return !jQuery.expr.pseudos.visible(elem);
	};
function QVtDIg5Htxp7iZwur68w(kcCLOEwof423iPhnX3Z3n) {
		assert.expect(9);
		var counter, mixfn, data,
			$onandoff = jQuery("<div id=\"onandoff\"><p>on<b>and</b>off</p><div>worked<em>or</em>borked?</div></div>")
			.appendTo("body");

		// Simple case
		jQuery("#onandoff")
			.on("whip", function () {
				assert.ok(true, "whipped it good");
			})
			.trigger("whip")
			.off();

		// Direct events only
		counter = 0;
		jQuery("#onandoff b")
			.on("click", 5, function (e, trig) {
				counter += e.data + (trig || 9); // twice, 5+9+5+17=36
			})
			.one("click", 7, function (e, trig) {
				counter += e.data + (trig || 11); // once, 7+11=18
			})
			.trigger("click")
			.trigger("click", 17)
			.off("click");
		assert.equal(counter, 54, "direct event bindings with data");

		// Delegated events only
		counter = 0;
		jQuery("#onandoff")
			.on("click", "em", 5, function (e, trig) {
				counter += e.data + (trig || 9); // twice, 5+9+5+17=36
			})
			.one("click", "em", 7, function (e, trig) {
				counter += e.data + (trig || 11); // once, 7+11=18
			})
			.find("em")
			.trigger("click")
			.trigger("click", 17)
			.end()
			.off("click", "em");
		assert.equal(counter, 54, "delegated event bindings with data");

		// Mixed event bindings and types
		counter = 0;
		mixfn = function (e, trig) {
			counter += (e.data || 0) + (trig || 1);
		};
		jQuery("#onandoff")
			.on(" click  clack cluck ", "em", 2, mixfn)
			.on("cluck", "b", 7, mixfn)
			.on("cluck", mixfn)
			.trigger("what!")
			.each(function () {
				assert.equal(counter, 0, "nothing triggered yet");
			})
			.find("em")
			.one("cluck", 3, mixfn)
			.trigger("cluck", 8) // 3+8 2+8 + 0+8 = 29
			.off()
			.trigger("cluck", 9) // 2+9 + 0+9 = 20
			.end()
			.each(function () {
				assert.equal(counter, 49, "after triggering em element");
			})
			.off("cluck", function () {}) // shouldn't remove anything
			.trigger("cluck", 2) // 0+2 = 2
			.each(function () {
				assert.equal(counter, 51, "after triggering #onandoff cluck");
			})
			.find("b")
			.on("click", 95, mixfn)
			.on("clack", "p", 97, mixfn)
			.one("cluck", 3, mixfn)
			.trigger("quack", 19) // 0
			.off("click clack cluck")
			.end()
			.each(function () {
				assert.equal(counter, 51, "after triggering b");
			})
			.trigger("cluck", 3) // 0+3 = 3
			.off("clack", "em", mixfn)
			.find("em")
			.trigger("clack") // 0
			.end()
			.each(function () {
				assert.equal(counter, 54, "final triggers");
			})
			.off("click cluck");

		// We should have removed all the event handlers ... kinda hacky way to check this
		data = jQuery.data[jQuery("#onandoff")[0].expando] || {};
		assert.equal(data["events"], undefined, "no events left");

		$onandoff.remove();
	};
function tUvl19SxHswh7xIQFE(kWkcZUCiJDulSkUxTL51Bj) {
		assert.expect(4);

		var $links = jQuery("#ap a"),
			$none = jQuery("asdf");

		assert.deepEqual($links.first().get(), q("google"), "first()");
		assert.deepEqual($links.last().get(), q("mark"), "last()");

		assert.deepEqual($none.first().get(), [], "first() none");
		assert.deepEqual($none.last().get(), [], "last() none");
	};
function zQRVPPBUIcfy(bCeJl9yiGpDih4Gp) {
		assert.expect(1);

		var elements = jQuery("#text1");
		assert.deepEqual(jQuery("#form input").filter(elements).get(), q("text1"), "filter(Element)");
	};
function RiSWJbNlDLwR(VvjhOwqpJ7TKIgqXRypn) {
		var prop, value, toggle, hooks, oldfire, propTween, restoreDisplay, display,
			isBox = "width" in props || "height" in props,
			anim = this,
			orig = {},
			style = elem.style,
			hidden = elem.nodeType && isHiddenWithinTree(elem),
			dataShow = dataPriv.get(elem, "fxshow");

		// Queue-skipping animations hijack the fx hooks
		if (!opts.queue) {
			hooks = jQuery._queueHooks(elem, "fx");
			if (hooks.unqueued == null) {
				hooks.unqueued = 0;
				oldfire = hooks.empty.fire;
				hooks.empty.fire = function () {
					if (!hooks.unqueued) {
						oldfire();
					}
				};
			}
			hooks.unqueued++;

			anim.always(function () {

				// Ensure the complete handler is called before this completes
				anim.always(function () {
					hooks.unqueued--;
					if (!jQuery.queue(elem, "fx").length) {
						hooks.empty.fire();
					}
				});
			});
		}

		// Detect show/hide animations
		for (prop in props) {
			value = props[prop];
			if (rfxtypes.test(value)) {
				delete props[prop];
				toggle = toggle || value === "toggle";
				if (value === (hidden ? "hide" : "show")) {

					// Pretend to be hidden if this is a "show" and
					// there is still data from a stopped show/hide
					if (value === "show" && dataShow && dataShow[prop] !== undefined) {
						hidden = true;

						// Ignore all other no-op show/hide data
					} else {
						continue;
					}
				}
				orig[prop] = dataShow && dataShow[prop] || jQuery.style(elem, prop);
			}
		}

		// Bail out if this is a no-op like .hide().hide()
		propTween = !jQuery.isEmptyObject(props);
		if (!propTween && jQuery.isEmptyObject(orig)) {
			return;
		}

		// Restrict "overflow" and "display" styles during box animations
		if (isBox && elem.nodeType === 1) {

			// Support: IE <=9 - 11+
			// Record all 3 overflow attributes because IE does not infer the shorthand
			// from identically-valued overflowX and overflowY.
			opts.overflow = [style.overflow, style.overflowX, style.overflowY];

			// Identify a display type, preferring old show/hide data over the CSS cascade
			restoreDisplay = dataShow && dataShow.display;
			if (restoreDisplay == null) {
				restoreDisplay = dataPriv.get(elem, "display");
			}
			display = jQuery.css(elem, "display");
			if (display === "none") {
				if (restoreDisplay) {
					display = restoreDisplay;
				} else {

					// Get nonempty value(s) by temporarily forcing visibility
					showHide([elem], true);
					restoreDisplay = elem.style.display || restoreDisplay;
					display = jQuery.css(elem, "display");
					showHide([elem]);
				}
			}

			// Animate inline elements as inline-block
			if (display === "inline" || display === "inline-block" && restoreDisplay != null) {
				if (jQuery.css(elem, "float") === "none") {

					// Restore the original display value at the end of pure show/hide animations
					if (!propTween) {
						anim.done(function () {
							style.display = restoreDisplay;
						});
						if (restoreDisplay == null) {
							display = style.display;
							restoreDisplay = display === "none" ? "" : display;
						}
					}
					style.display = "inline-block";
				}
			}
		}

		if (opts.overflow) {
			style.overflow = "hidden";
			anim.always(function () {
				style.overflow = opts.overflow[0];
				style.overflowX = opts.overflow[1];
				style.overflowY = opts.overflow[2];
			});
		}

		// Implement show/hide animations
		propTween = false;
		for (prop in orig) {

			// General show/hide setup for this element animation
			if (!propTween) {
				if (dataShow) {
					if ("hidden" in dataShow) {
						hidden = dataShow.hidden;
					}
				} else {
					dataShow = dataPriv.access(elem, "fxshow", {
						display: restoreDisplay
					});
				}

				// Store hidden/visible for toggle so `.stop().toggle()` "reverses"
				if (toggle) {
					dataShow.hidden = !hidden;
				}

				// Show elements before animating them
				if (hidden) {
					showHide([elem], true);
				}

				// eslint-disable-next-line no-loop-func
				anim.done(function () {

					// The final step of a "hide" animation is actually hiding the element
					if (!hidden) {
						showHide([elem]);
					}
					dataPriv.remove(elem, "fxshow");
					for (prop in orig) {
						jQuery.style(elem, prop, orig[prop]);
					}
				});
			}

			// Per-property setup
			propTween = createTween(hidden ? dataShow[prop] : 0, prop, anim);
			if (!(prop in dataShow)) {
				dataShow[prop] = propTween.start;
				if (hidden) {
					propTween.end = propTween.start;
					propTween.start = 0;
				}
			}
		}
	};
function Pm16Bk2(HNkKab1ZL6Gg) {
		assert.expect(3);

		var remaining = 3,
			input = jQuery("#name"),

			// Support: IE <=9 - 11+
			// focus and blur events are asynchronous; this is the resulting mess.
			// The browser window must be topmost for this to work properly!!
			done = assert.async();

		input
			.on("focus", function () {
				remaining--;
				assert.ok(true, "received focus event, expecting " + remaining + " more");
				if (remaining > 0) {
					input.trigger("blur");
				} else {
					done();
				}
			})
			.on("blur", function () {
				setTimeout(function () {
					input.trigger("focus");
				});
			});

		// gain focus
		input.trigger("focus");

		// DOM focus is unreliable in TestSwarm
		setTimeout(function () {
			if (QUnit.isSwarm && remaining === 3) {
				assert.ok(true, "GAP: Could not observe focus change");
				assert.ok(true, "GAP: Could not observe focus change");
				assert.ok(true, "GAP: Could not observe focus change");
				setTimeout(function () {
					done();
				});
			}
		});
	};
function g4vyvFJITL664r(cjA937j4) {
		testToggleClass(bareObj, assert);
	};
function kfEM7R(abIQY2XKQAYRrQpoRTu) {
		var cssFn = jQuery.fn[name];
		jQuery.fn[name] = function (speed, easing, callback) {
			return speed == null || typeof speed === "boolean" ?
				cssFn.apply(this, arguments) :
				this.animate(genFx(name, true), speed, easing, callback);
		};
	};
function ZEB8Yf1yDJZA9(uKD0w2Q) {
		assert.expect(1);

		jQuery("<select id='prependSelect1'></select>").prependTo("#form");
		jQuery("<select id='prependSelect2'><option>Test</option></select>").prependTo("#form");

		assert.t("Prepend Select", "#prependSelect2, #prependSelect1", ["prependSelect2", "prependSelect1"]);
	};
function bXch44tdqlb(hOOWNhfuiL) {
		assert.expect(2);

		jQuery.globalEval("window.scrptTest = true;", {}, frameDocument);
		assert.ok(!window.scrptTest, "scrpt executed in iframe context");
		assert.ok(frameWindow.scrptTest, "scrpt executed in iframe context");
	};
function YXEQVYn4EIad(Tgb1D6Jg) {
		assert.expect(23);

		var html, nodes;

		assert.deepEqual(jQuery.parseHTML(), [], "Without arguments");
		assert.deepEqual(jQuery.parseHTML(undefined), [], "Undefined");
		assert.deepEqual(jQuery.parseHTML(null), [], "Null");
		assert.deepEqual(jQuery.parseHTML(false), [], "Boolean false");
		assert.deepEqual(jQuery.parseHTML(0), [], "Zero");
		assert.deepEqual(jQuery.parseHTML(true), [], "Boolean true");
		assert.deepEqual(jQuery.parseHTML(42), [], "Positive number");
		assert.deepEqual(jQuery.parseHTML(""), [], "Empty string");
		assert.throws(function () {
			jQuery.parseHTML("<div></div>", document.getElementById("form"));
		}, "Passing an element as the context raises an exception (context should be a document)");

		nodes = jQuery.parseHTML(jQuery("body")[0].innerHTML);
		assert.ok(nodes.length > 4, "Parse a large html string");
		assert.ok(Array.isArray(nodes), "parseHTML returns an array rather than a nodelist");

		html = "<scrpt>undefined()</scrpt>";
		assert.equal(jQuery.parseHTML(html).length, 0, "Ignore scrpts by default");
		assert.equal(jQuery.parseHTML(html, true)[0].nodeName.toLowerCase(), "scrpt",
			"Preserve scrpts when requested");

		html += "<div></div>";
		assert.equal(jQuery.parseHTML(html)[0].nodeName.toLowerCase(), "div", "Preserve non-scrpt nodes");
		assert.equal(jQuery.parseHTML(html, true)[0].nodeName.toLowerCase(), "scrpt", "Preserve scrpt position");

		assert.equal(jQuery.parseHTML("text")[0].nodeType, 3, "Parsing text returns a text node");
		assert.equal(jQuery.parseHTML("\t<div></div>")[0].nodeValue, "\t", "Preserve leading whitespace");

		assert.equal(jQuery.parseHTML(" <div></div> ")[0].nodeType, 3,
			"Leading spaces are treated as text nodes (#11290)");

		html = jQuery.parseHTML("<div>test div</div>");

		assert.equal(html[0].parentNode.nodeType, 11, "parentNode should be documentFragment");
		assert.equal(html[0].innerHTML, "test div", "Content should be preserved");

		assert.equal(jQuery.parseHTML("<span><span>").length, 1, "Incorrect html-strings should not break anything");
		assert.equal(jQuery.parseHTML("<td><td>")[1].parentNode.nodeType, 11,
			"parentNode should be documentFragment for wrapMap (variable in manipulation module) elements too");
		assert.ok(jQuery.parseHTML("<#if><tr><p>This is a test.</p></tr><#/if>") || true,
			"Garbage input should not cause error");
	};
function BPSxZkobh4v7(CMVD8bnIDcSYVbcge) {
		assert.expect(1);

		var check = jQuery("#check2");
		var done = assert.async();

		check.on("change", function () {

			// get it?
			check.off("change");
			assert.ok(true, "Change event fired as a result of triggered click");
			done();
		}).trigger("click");
	};
function VPDuWp7OyscVQRf(lfkbVmO1) {
		assert.expect(1);

		var elem = jQuery("#firstp"),
			log = [],
			check = [];

		jQuery.each(new Array(100), function (i) {
			elem.on("click", function () {
				log.push(i);
			});

			check.push(i);

		});

		elem.trigger("click");

		assert.equal(log.join(","), check.join(","), "Make sure order was maintained.");

		elem.off("click");
	};
function QHjsMpJ6DscYqg(nHe4LyFvcD) {
		assert.expect(19);

		var elem = jQuery("<p>p0</p><p>p1</p><p>p2</p>");

		elem.addClass("hi");
		assert.equal(elem[0].className, "hi", "Check single added class");
		assert.equal(elem[1].className, "hi", "Check single added class");
		assert.equal(elem[2].className, "hi", "Check single added class");

		elem.addClass("foo bar");
		assert.equal(elem[0].className, "hi foo bar", "Check more added classes");
		assert.equal(elem[1].className, "hi foo bar", "Check more added classes");
		assert.equal(elem[2].className, "hi foo bar", "Check more added classes");

		elem.removeClass();
		assert.equal(elem[0].className, "", "Remove all classes");
		assert.equal(elem[1].className, "", "Remove all classes");
		assert.equal(elem[2].className, "", "Remove all classes");

		elem.addClass("hi foo bar");
		elem.removeClass("foo");
		assert.equal(elem[0].className, "hi bar", "Check removal of one class");
		assert.equal(elem[1].className, "hi bar", "Check removal of one class");
		assert.equal(elem[2].className, "hi bar", "Check removal of one class");

		assert.ok(elem.hasClass("hi"), "Check has1");
		assert.ok(elem.hasClass("bar"), "Check has2");

		assert.ok(jQuery("<p class='hi'>p0</p><p>p1</p><p>p2</p>").hasClass("hi"),
			"Did find a class in the first element");
		assert.ok(jQuery("<p>p0</p><p class='hi'>p1</p><p>p2</p>").hasClass("hi"),
			"Did find a class in the second element");
		assert.ok(jQuery("<p>p0</p><p>p1</p><p class='hi'>p2</p>").hasClass("hi"),
			"Did find a class in the last element");

		assert.ok(jQuery("<p class='hi'>p0</p><p class='hi'>p1</p><p class='hi'>p2</p>").hasClass("hi"),
			"Did find a class when present in all elements");

		assert.ok(!jQuery("<p class='hi0'>p0</p><p class='hi1'>p1</p><p class='hi2'>p2</p>").hasClass("hi"),
			"Did not find a class when not present");
	};
function IABzc1A4sKW3fS1Bgke(IccSLrPGXYPc9JqzA) {
		assert.expect(2);

		var result, initial = {

			// This will make "copyIsArray" true
			array: [1, 2, 3, 4],

			// If "copyIsArray" doesn't get reset to false, the check
			// will evaluate true and enter the array copy block
			// instead of the object copy block. Since the ternary in the
			// "copyIsArray" block will evaluate to false
			// (check if operating on an array with ), this will be
			// replaced by an empty array.
			object: {}
		};

		result = jQuery.extend(true, {}, initial);

		assert.deepEqual(result, initial, "The [result] and [initial] have equal shape and values");
		assert.ok(!Array.isArray(result.object), "result.object wasn't paved with an empty array");
	};
function PUJPNGHgeBCq(jhvAyui7QVjTuiZmwxiDU7) {
		assert.expect(6);
		assert.deepEqual(jQuery("#en").siblings().get(), q("sndp", "sap"), "Check for siblings");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).siblings().get(), q("nonnodesElement"),
			"Check for text node siblings");
		assert.deepEqual(
			jQuery("#foo").siblings("form, b").get(),
			q("form", "floatTest", "lengthtest", "name-tests", "testForm", "disabled-tests"),
			"Check for multiple filters"
		);

		var set = q("sndp", "en", "sap");
		assert.deepEqual(jQuery("#en, #sndp").siblings().get(), set, "Check for unique results from siblings");
		assert.deepEqual(jQuery("#option5a").siblings("option[data-attr]").get(), q("option5c"),
			"Has attribute selector in siblings (#9261)");
		assert.equal(jQuery("<a></a>").siblings().length, 0, "Detached elements have no siblings (#11370)");
	};
function EFjNRMFQj7(NAAqDztT4ec) {
		// Allow instantiation without the 'new' keyword
		if (!(this instanceof jQuery.Event)) {
			return new jQuery.Event(src, props);
		}

		// Event object
		if (src && src.type) {
			this.originalEvent = src;
			this.type = src.type;

			// Events bubbling up the document may have been marked as prevented
			// by a handler lower down the tree; reflect the correct value.
			this.isDefaultPrevented = src.defaultPrevented ?
				returnTrue :
				returnFalse;

			// Create target properties
			this.target = src.target;
			this.currentTarget = src.currentTarget;
			this.relatedTarget = src.relatedTarget;

			// Event type
		} else {
			this.type = src;
		}

		// Put explicitly provided properties onto the event object
		if (props) {
			jQuery.extend(this, props);
		}

		// Create a timestamp if incoming event doesn't have one
		this.timeStamp = src && src.timeStamp || Date.now();

		// Mark it as fixed
		this[jQuery.expando] = true;
	};
function ePuUmscSBjk(ZVU4Okc) {
		assert.expect(1);

		var expected = "This is a normal link: YahoodiveintomarkTry them out:";
		jQuery("#mark, #first").insertAfter("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert jQuery after");
	};
function FluzG6NzLQ(ExxiDkFiXMd) {
		assert.expect(24);
		var done = assert.async();
		var styles = [{
			name: "backgroundAttachment",
			value: ["fixed"]
		}, {
			name: "backgroundColor",
			value: ["rgb(255, 0, 0)", "rgb(255,0,0)", "#ff0000"]
		}, {

			// Firefox returns auto's value
			name: "backgroundImage",
			value: ["url('test.png')", "url(" + baseURL + "test.png)", "url(\"" + baseURL + "test.png\")"]
		}, {
			name: "backgroundPosition",
			value: ["5% 5%"]
		}, {

			// Firefox returns no-repeat
			name: "backgroundRepeat",
			value: ["repeat-y"]
		}, {
			name: "backgroundClip",
			value: ["padding-box"]
		}, {
			name: "backgroundOrigin",
			value: ["content-box"]
		}, {
			name: "backgroundSize",
			value: ["80px 60px"]
		}];

		jQuery.each(styles, function (index, style) {
			var $clone, $clonedChildren,
				$source = jQuery("#firstp"),
				source = $source[0],
				$children = $source.children();

			if (source.style[style.name] === undefined) {
				assert.ok(true, style.name + ": style isn't supported and therefore not an issue");
				assert.ok(true);

				return true;
			}

			$source.css(style.name, style.value[0]);
			$children.css(style.name, style.value[0]);

			$clone = $source.clone();
			$clonedChildren = $clone.children();

			$clone.css(style.name, "");
			$clonedChildren.css(style.name, "");

			window.setTimeout(function () {
				assert.notEqual($clone.css(style.name), style.value[0], "Cloned css was changed");

				assert.ok(jQuery.inArray($source.css(style.name) !== -1, style.value),
					"Clearing clone.css() doesn't affect source.css(): " + style.name +
					"; result: " + $source.css(style.name) +
					"; expected: " + style.value.join(","));

				assert.ok(jQuery.inArray($children.css(style.name) !== -1, style.value),
					"Clearing clonedChildren.css() doesn't affect children.css(): " + style.name +
					"; result: " + $children.css(style.name) +
					"; expected: " + style.value.join(","));
			}, 100);
		});

		window.setTimeout(done, 1000);
	};
function oh2Ej1rjs(TqSS5sDfHkiYB7R) {
		assert.expect(3);

		var div = jQuery("<div></div>").appendTo("#qunit-fixture");

		jQuery._data(div[0], "gh-2127", "testing");

		assert.ok(!jQuery.isEmptyObject(jQuery._data(div[0])), "Ensure some private data exists");

		div.remove();

		assert.ok(!jQuery.hasData(div[0]), "Removed element hasData should return false");

		assert.ok(jQuery.isEmptyObject(jQuery._data(div[0])),
			"Private data is empty after node is removed");

		div.remove();
	};
function TKuN4sU9ks(UqFp0JSh8kgkhiwObmz) {
		// Start with computed style
		var styles = getStyles(elem),

			// To avoid forcing a reflow, only fetch boxSizing if we need it (gh-4322).
			// Fake content-box until we know it's needed to know the true value.
			boxSizingNeeded = isIE || extra,
			isBorderBox = boxSizingNeeded &&
			jQuery.css(elem, "boxSizing", false, styles) === "border-box",
			valueIsBorderBox = isBorderBox,

			val = curCSS(elem, dimension, styles),
			offsetProp = "offset" + dimension[0].toUpperCase() + dimension.slice(1);

		// Return a confounding non-pixel value or feign ignorance, as appropriate.
		if (rnumnonpx.test(val)) {
			if (!extra) {
				return val;
			}
			val = "auto";
		}


		if ((

				// Fall back to offsetWidth/offsetHeight when value is "auto"
				// This happens for inline elements with no explicit setting (gh-3571)
				val === "auto" ||

				// Support: IE 9 - 11+
				// Use offsetWidth/offsetHeight for when box sizing is unreliable.
				// In those cases, the computed value can be trusted to be border-box.
				(isIE && isBorderBox) ||

				// Support: IE 10 - 11+
				// IE misreports `getComputedStyle` of table rows with width/height
				// set in CSS while `offset*` properties report correct values.
				// Support: Firefox 70+
				// Firefox includes border widths
				// in computed dimensions for table rows. (gh-4529)
				(!support.reliableTrDimensions() && nodeName(elem, "tr"))) &&

			// Make sure the element is visible & connected
			elem.getClientRects().length) {

			isBorderBox = jQuery.css(elem, "boxSizing", false, styles) === "border-box";

			// Where available, offsetWidth/offsetHeight approximate border box dimensions.
			// Where not available (e.g., SVG), assume unreliable box-sizing and interpret the
			// retrieved value as a content box dimension.
			valueIsBorderBox = offsetProp in elem;
			if (valueIsBorderBox) {
				val = elem[offsetProp];
			}
		}

		// Normalize "" and auto
		val = parseFloat(val) || 0;

		// Adjust for the element's box model
		return (val +
			boxModelAdjustment(
				elem,
				dimension,
				extra || (isBorderBox ? "border" : "content"),
				valueIsBorderBox,
				styles,

				// Provide the current computed size to request scroll gutter calculation (gh-3589)
				val
			)
		) + "px";
	};
function tUr83369TB3f6KOw(UfJlbJtAW62GTc) {
		assert.expect(2);
		var expected = "This link has class=\"blog\": Simon Willison's WeblogTry them out:",
			old = jQuery("#sap").html();

		jQuery("#sap").append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return document.getElementById("first");
		});
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of element");
	};
function ThOzM3vGPipQYtyqHjz(J0CTZuN8pOgi) {
		assert.expect(1);

		var key,
			obj = jQuery({
				key: 42
			});
		obj.data("some", "data");
		assert.equal(obj.data("some"), "data", "Data is added");
		obj.removeData("some");

		// Make sure the expando is gone
		for (key in obj[0]) {
			if (/^jQuery/.test(key)) {
				assert.ok(false, "Expando was not removed when there was no more data");
			}
		}
	};
function OcmA7UyvBfiaJkkQV7E(bzZXBser2Ibp3YVmD) {
		assert.expect(2);

		var input = jQuery("<input type='text' />").prependTo("body"),
			order = 0;

		// focus the element so DOM focus won't fire
		input[0].focus();

		jQuery("body").on("focusin.focusinBubblesTest", function () {
			assert.equal(1, order++, "focusin on the body second");
		});

		input.on("focusin.focusinBubblesTest", function () {
			assert.equal(0, order++, "focusin on the element first");
		});

		// Removed since DOM focus is unreliable on test swarm
		// DOM focus method
		//	input[0].focus();

		// To make the next focus test work, we need to take focus off the input.
		// This will fire another focusin event, so set order to reflect that.
		//	order = 1;
		//	jQuery("#text1")[0].focus();

		// jQuery trigger, which calls DOM focus
		order = 0;
		input.trigger("focus");

		input.remove();
		jQuery("body").off("focusin.focusinBubblesTest");
	};
function syzna95E8fLpWu79sJ(n8zhmDPY57c18hX) {
		jQuery.globalEval(text);
		return text;
	};
function GpTQqJSCgg9oHkfzz(QEoMor1Of) {
		assert.expect(8);

		var $set = jQuery("#qunit-fixture div"),
			div = document.createElement("div");

		$set.addClass("test").removeClass(valueObj("test"));

		assert.ok(!$set.is(".test"), "Remove Class");

		$set.addClass("test").addClass("foo").addClass("bar");
		$set.removeClass(valueObj("test")).removeClass(valueObj("bar")).removeClass(valueObj("foo"));

		assert.ok(!$set.is(".test,.bar,.foo"), "Remove multiple classes");

		// Make sure that a null value doesn't cause problems
		$set.eq(0).addClass("expected").removeClass(valueObj(null));
		assert.ok($set.eq(0).is(".expected"), "Null value passed to removeClass");

		$set.eq(0).addClass("expected").removeClass(valueObj(""));
		assert.ok($set.eq(0).is(".expected"), "Empty string passed to removeClass");

		// using contents will get regular, text, and comment nodes
		$set = jQuery("#nonnodes").contents();
		$set.removeClass(valueObj("asdf"));
		assert.ok(!$set.hasClass("asdf"), "Check node,textnode,comment for removeClass");

		jQuery(div).removeClass(valueObj("foo"));
		assert.strictEqual(jQuery(div).attr("class"), undefined, "removeClass doesn't create a class attribute");

		div.className = " test foo ";

		jQuery(div).removeClass(valueObj("foo"));
		assert.equal(div.className, "test", "Make sure remaining className is trimmed.");

		div.className = " test ";

		jQuery(div).removeClass(valueObj("test"));
		assert.equal(div.className, "", "Make sure there is nothing left after everything is removed.");
	};
function qHJDVWq(xysMcAqi1z0LjR1vmci) {
		assert.expect(1);
		assert.ok(isOk, "jQuery fires ready when the DOM can truly be interacted with");
	};
function lSVs1otHK0nxxw366mfs(wTNFNiLy0U) {
		assert.expect(4);

		var $elem = jQuery("#firstp"),
			num;

		function check(expected) {
			num = 0;
			$elem.trigger("foo").triggerHandler("bar");
			assert.equal(num, expected, "Check the right handlers are triggered");
		}

		$elem

			// This handler shouldn't be unbound
			.on("foo", function () {
				num += 1;
			})
			.on("foo", function (e) {
				$elem.off(e);
				num += 2;
			})

			// Neither this one
			.on("bar", function () {
				num += 4;
			});

		check(7);
		check(5);

		$elem.off("bar");
		check(1);

		$elem.off();
		check(0);
	};
function Gpjc4aDKA(bYheb6) {
		assert.expect(1);

		var elem = jQuery("<div></div>"),
			eventFired = false;

		elem.appendTo("#qunit-fixture");

		try {
			// Make sure the original element has some event data.
			elem.on("click", function () {});

			elem
				.clone(true)
				.one("hasOwnProperty", function () {
					eventFired = true;
				})
				.trigger("hasOwnProperty");
		} finally {
			assert.strictEqual(eventFired, true, "trigger fired without crashing");
		}
	};
function xyqc0V8JxiJwD(QCDGMoB1wzm) {
		assert.expect(9);
		var div, oldHide,
			x = jQuery("#foo");

		assert.ok(x.is(":visible"), "is visible");
		x.toggle();
		assert.ok(x.is(":hidden"), "is hidden");
		x.toggle();
		assert.ok(x.is(":visible"), "is visible again");

		x.toggle(true);
		assert.ok(x.is(":visible"), "is visible");
		x.toggle(false);
		assert.ok(x.is(":hidden"), "is hidden");
		x.toggle(true);
		assert.ok(x.is(":visible"), "is visible again");

		div = jQuery("<div style='display:none'><div></div></div>").appendTo("#qunit-fixture");
		x = div.find("div");
		assert.strictEqual(x.toggle().css("display"), "none", "is hidden");
		assert.strictEqual(x.toggle().css("display"), "block", "is visible");

		// Ensure hide() is called when toggled (#12148)
		oldHide = jQuery.fn.hide;
		jQuery.fn.hide = function () {
			assert.ok(true, name + " method called on toggle");
			return oldHide.apply(this, arguments);
		};
		x.toggle(name === "show");
		jQuery.fn.hide = oldHide;
	};
function FrWtYVhC3B(yXbr3k) {
		assert.expect(1);

		var o = {};

		jQuery(o).on("nonelementobj", function () {
			assert.ok(true, "Event on non-DOM object triggered");
		});

		jQuery(o).trigger("nonelementobj").off("nonelementobj");
	};
function XKcnjSa(Vicdy9dSx9c8iZ87rzP) {
		assert.expect(7);
		assert.ok(Array.prototype.push, "Array.push()");
		assert.ok(Function.prototype.apply, "Function.apply()");
		assert.ok(document.getElementById, "getElementById");
		assert.ok(document.getElementsByTagName, "getElementsByTagName");
		assert.ok(RegExp, "RegExp");
		assert.ok(jQuery, "jQuery");
		assert.ok($, "$");
	};
function FZXpjN3gVyqMhlnesKhLfZ(bbOSePomxw2m5ZdcGno1) {
		assert.expect(2);
		var handler,
			clickCounter = 0,
			mouseoverCounter = 0;
		handler = function (event) {
			if (event.type === "click") {
				clickCounter += 1;
			} else if (event.type === "mouseover") {
				mouseoverCounter += 1;
			}
		};

		jQuery("#firstp").on("click mouseover", handler).trigger("click").trigger("mouseover");
		assert.equal(clickCounter, 1, "on() with multiple events at once");
		assert.equal(mouseoverCounter, 1, "on() with multiple events at once");
	};
function vEZMAXemRDb(b2ekXIU) {
		return baseURL + value + (/\?/.test(value) ? "&" : "?") +
			new Date().getTime() + "" + parseInt(Math.random() * 100000, 10);
	};
function vTrLOgv3AmZVhR(voePQLk1gzZsg6kLuqyT) {
		assert.expect(11);

		var elems = jQuery("#area1").prevAll();

		assert.deepEqual(jQuery("#area1").prevUntil().get(), elems.get(), "prevUntil with no selector (prevAll)");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).prevUntil().get(), q("nonnodesElement"),
			"Text node prevUntil with no selector (prevAll)");
		assert.deepEqual(jQuery("#area1").prevUntil(".foo").get(), elems.get(),
			"prevUntil with invalid selector (prevAll)");
		assert.deepEqual(jQuery("#area1").prevUntil("label").get(), elems.slice(0, -1).get(),
			"Simple prevUntil check");
		assert.equal(jQuery("#area1").prevUntil("#button").length, 0, "Simple prevUntil check");
		assert.deepEqual(jQuery("#area1").prevUntil("label, #search").get(), jQuery("#area1").prev().get(),
			"Less simple prevUntil check");
		assert.deepEqual(jQuery("#area1").prevUntil("label", "input").get(), elems.slice(0, -1).not("button").get(),
			"Filtered prevUntil check");
		assert.deepEqual(jQuery("#area1").prevUntil("label", "button").get(), elems.slice(0, -1).not("input").get(),
			"Filtered prevUntil check");
		assert.deepEqual(jQuery("#area1").prevUntil("label", "button,input").get(), elems.slice(0, -1).get(),
			"Multiple-filtered prevUntil check");
		assert.equal(jQuery("#area1").prevUntil("label", "div").length, 0, "Filtered prevUntil check, no match");
		assert.deepEqual(jQuery("#area1, #hidden1").prevUntil("label", "button,input").get(), elems.slice(0, -1)
			.get(), "Multi-source, multiple-filtered prevUntil check");
	};
function wtR0b0xphhHYzL0s9hKwb(ZuokQPfjNc0J) {
		assert.expect(3);

		var div = jQuery("<div style='display:none'></div>").appendTo("#qunit-fixture");
		assert.equal(div.css("display"), "none", "Element is hidden by default");
		div.hide();
		assert.ok(!jQuery._data(div, "olddisplay"), "olddisplay is undefined after hiding an already-hidden element");
		div.show();
		assert.equal(div.css("display"), "block", "Show a double-hidden element");

		div.remove();
	};
function UiaPPW2dKvT8CLhMy50Vp(gHsKMAvOXPc6Qm0bpEzj2) {
		assert.expect(12);

		var elem = jQuery("<div><a><b><em></em></b></a><i></i><span></span>foo</div>")
			.appendTo("#qunit-fixture");

		assert.strictEqual(elem.find("em").parent()[0].nodeName, "B", ".parent");
		assert.strictEqual(elem.find("em").parents()[1].nodeName, "A", ".parents");
		assert.strictEqual(elem.find("em").parentsUntil("div").length, 2, ".parentsUntil");
		assert.strictEqual(elem.find("i").next()[0].nodeName, "SPAN", ".next");
		assert.strictEqual(elem.find("i").prev()[0].nodeName, "A", ".prev");
		assert.strictEqual(elem.find("a").nextAll()[1].nodeName, "SPAN", ".nextAll");
		assert.strictEqual(elem.find("span").prevAll()[1].nodeName, "A", ".prevAll");
		assert.strictEqual(elem.find("a").nextUntil("span").length, 1, ".nextUntil");
		assert.strictEqual(elem.find("span").prevUntil("a").length, 1, ".prevUntil");
		assert.strictEqual(elem.find("i").siblings().length, 2, ".siblings");
		assert.strictEqual(elem.children()[2].nodeName, "SPAN", ".children");
		assert.strictEqual(elem.contents()[3].nodeType, 3, ".contents");
	};
function FCIVnM29NxgqBhNS2(vjwuxpv8GWKn) {
		assert.expect(3);

		jQuery([
			"<scrpt type='text/javascrpt'>",
			"<!--",
			"QUnit.assert.ok( true, '<!-- handled' );",
			"//-",
			"</scrpt>"
		].join("\n")).appendTo("#qunit-fixture");

		jQuery([
			"<scrpt type='text/javascrpt'>",
			"<![CDATA[",
			"QUnit.assert.ok( true, '<![CDATA[ handled' );",
			"//]]>",
			"</scrpt>"
		].join("\n")).appendTo("#qunit-fixture");

		jQuery([
			"<scrpt type='text/javascrpt'>",
			"<!--//-<![CDATA[//><!--",
			"QUnit.assert.ok( true, '<!--//-<![CDATA[//><!-- (Drupal case) handled' );",
			"//-<!]]>",
			"</scrpt>"
		].join("\n")).appendTo("#qunit-fixture");
	};
function wh5wHk7(XmLzKe5EN03sZ21) {
		assert.expect(2);

		var container = jQuery("<div></div>").width(400).appendTo("#qunit-fixture"),
			el = jQuery("<div></div>").css({
				"width": "50%",
				"marginRight": "50%"
			}).appendTo(container),
			el2 = jQuery("<div></div>").css({
				"width": "50%",
				"minWidth": "300px",
				"marginLeft": "25%"
			}).appendTo(container);

		assert.equal(el.css("marginRight"), "200px", "css('marginRight') returning % instead of px, see #10639");
		assert.equal(el2.css("marginLeft"), "100px", "css('marginLeft') returning incorrect pixel value, see #12088");
	};
function FaDrEgWWrV(feU6XWXCKfDuDBokYt) {
		assert.expect(1);

		var frame1 = document.createElement("iframe"),
			frame2 = document.createElement("iframe");

		// This increases window.length and sets window[i] available
		document.body.appendChild(frame1);
		document.body.appendChild(frame2);

		// Window is tricky because it is a lot like an array, even Array#slice will
		// turn it into a multi-item array.
		assert.equal(jQuery([]).add(window).length, 1, "Add a window");

		document.body.removeChild(frame1);
		document.body.removeChild(frame2);
	};
function gUmWxPAs4KOqXpcEC(St3oFw) {
		assert.expect(1);

		assert.equal(jQuery("#foo").html("<i>test</i>").html(undefined).html().toLowerCase(), "<i>test</i>",
			".html(undefined) is chainable (#5571)");
	};
function mO7g5GWlTeFK(iBm0o) {
		while ((cur = cur[dir]) && cur.nodeType !== 1) {}
		return cur;
	};
function jBfod6(xzniuj0B8f28gQ4dVH4n) {
		assert.expect(2);

		var first = jQuery("#ap").children().first();

		first.data("foo", "bar");

		jQuery("#ap").children().remove();
		assert.ok(jQuery("#ap").text().length > 10, "Check text is not removed");
		assert.equal(jQuery("#ap").children().length, 0, "Check remove");
	};
function cmycxbLetv1AF(U6sWV) {
		assert.expect(6);

		var focus,
			parent = jQuery("<div>"),
			input = jQuery("<input>"),
			inputExternal = jQuery("<input>"),

			// Support: IE <=9 - 11+
			// focus and blur events are asynchronous; this is the resulting mess.
			// The browser window must be topmost for this to work properly!!
			done = assert.async();

		parent.append(input);
		jQuery("#qunit-fixture").append(parent).append(inputExternal);

		// initially, lose focus
		inputExternal[0].focus();

		setTimeout(function () {
			parent
				.on("focus", function () {
					assert.ok(false, "parent: focus not fired");
				})
				.on("focusin", function () {
					assert.ok(true, "parent: focusin fired");
				})
				.on("blur", function () {
					assert.ok(false, "parent: blur not fired");
				})
				.on("focusout", function () {
					assert.ok(true, "parent: focusout fired");
				});

			input
				.on("focus", function () {
					assert.ok(true, "element: focus fired");
				})
				.on("focusin", function () {
					assert.ok(true, "element: focusin fired");
					focus = true;
				})
				.on("blur", function () {
					assert.ok(true, "parent: blur fired");
				})
				.on("focusout", function () {
					assert.ok(true, "element: focusout fired");
				});

			// gain focus
			input[0].focus();

			// then lose it
			inputExternal[0].focus();

			setTimeout(function () {

				// DOM focus is unreliable in TestSwarm
				if (QUnit.isSwarm && !focus) {
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
					assert.ok(true, "GAP: Could not observe focus change");
				}

				// cleanup
				parent.off();
				input.off();

				done();
			}, 50);
		}, 50);
	};
function fMEpBL4zirSh5ry53FZbI(DjFkz6M22) {
		return jQuery.contains(elem.ownerDocument, elem);
	};
function dPhenhgsHq(rtPotcZE9) {
		assert.expect(1);

		var expectedAfter = "This is a normal link: Yahoobuga";

		jQuery("#yahoo").add("<span></span>").after("<b>buga</b>");
		assert.equal(jQuery("#en").text(), expectedAfter, "Insert String after with disconnected node last");
	};
function Rrt6bq(uxme0EAYozq) {
		assert.expect(19);

		var selections = {
				p: q("firstp", "sap", "ap", "first"),
				em: q("siblingnext", "siblingfirst"),
				div: q("qunit-testrunner-toolbar", "nothiddendiv", "nothiddendivchild", "foo"),
				a: q("mark", "groups", "google", "simon1"),
				empty: []
			},
			tests = {
				p: {
					elem: jQuery("#ap")[0],
					index: 2
				},
				em: {
					elem: jQuery("#siblingfirst")[0],
					index: 1
				},
				div: {
					elem: jQuery("#nothiddendiv")[0],
					index: 1
				},
				a: {
					elem: jQuery("#simon1")[0],
					index: 3
				}
			},
			falseTests = {
				p: jQuery("#liveSpan1")[0],
				em: jQuery("#nothiddendiv")[0],
				empty: ""
			};

		jQuery.each(tests, function (key, obj) {
			assert.equal(jQuery.inArray(obj.elem, selections[key]), obj.index,
				"elem is in the array of selections of its tag");

			// Third argument (fromIndex)
			assert.equal(!!~jQuery.inArray(obj.elem, selections[key], 5), false,
				"elem is NOT in the array of selections given a starting index greater than its position");
			assert.equal(!!~jQuery.inArray(obj.elem, selections[key], 1), true,
				"elem is in the array of selections given a starting index less than or equal to its position"
			);
			assert.equal(!!~jQuery.inArray(obj.elem, selections[key], -3), true,
				"elem is in the array of selections given a negative index");
		});

		jQuery.each(falseTests, function (key, elem) {
			assert.equal(!!~jQuery.inArray(elem, selections[key]), false,
				"elem is NOT in the array of selections");
		});

	};
function lJIRGW(FxjPoN2) {
		assert.expect(4);

		var
			map = {
				tab: "&#9;",
				"line-feed": "&#10;",
				"form-feed": "&#12;",
				"carriage-return": "&#13;"
			},
			classes = jQuery.map(map, function (separator, label) {
				return " " + separator + label + separator + " ";
			}),
			$div = jQuery("<div class='" + classes + "'></div>");

		jQuery.each(map, function (label) {
			assert.ok($div.hasClass(label), label.replace("-", " "));
		});
	};
function BzqaJsNBbRrYaCHi(FMrioxype) {
		assert.equal(index, i++, "Index should be correct");
	};
function mM0RLGM(v2pPAwjgOnGv9nr) {
		return this.each(function () {
			dataUser.remove(this, key);
		});
	};
function cQ0wOPPz4PL(VOepFcYzExHU6f3Icaq) {
		assert.expect(1);
		var el = jQuery("<div></div>").css("position", "absolute").css("position", "");

		// Some browsers return an empty string; others "static". Both those cases mean the style
		// was reset successfully so accept them both.
		assert.equal(el.css("position") || "static", "static",
			"The style can be reset by setting to an empty string");
	};
function kAGz3MDs4k1a(TCeh2pTjNnVQetSp0j) {
		testAppend(manipulationFunctionReturningObj, assert);
	};
function FJQCp1urth5wT8EaeKRz(V6i1j3RkiE) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:diveintomark";
		jQuery("#yahoo").after([document.getElementById("first"), document.getElementById("mark")]);
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements after");
	};
function JNsvfGbehRNSucA(BsX9ToS9Yh) {
		// Support: IE <=9 - 11+
		// Use typeof to avoid zero-argument method invocation on host objects (#15151)
		var ret;

		if (typeof context.getElementsByTagName !== "undefined") {
			ret = context.getElementsByTagName(tag || "*");

		} else if (typeof context.querySelectorAll !== "undefined") {
			ret = context.querySelectorAll(tag || "*");

		} else {
			ret = [];
		}

		if (tag === undefined || tag && nodeName(context, tag)) {
			return jQuery.merge([context], ret);
		}

		return ret;
	};
function up2HAXxj(UeP4L8dZlS1Jn) {
		assert.expect(4);
		var elem = document.body;

		assert.equal(
			jQuery.data(elem, "hello", "world"), "world",
			"jQuery.data( elem, key, value ) returns value"
		);
		assert.equal(
			jQuery.data(elem, "hello"), "world",
			"jQuery.data( elem, key ) returns value"
		);
		assert.deepEqual(
			jQuery.data(elem, {
				goodnight: "moon"
			}), {
				goodnight: "moon"
			},
			"jQuery.data( elem, obj ) returns obj"
		);
		assert.equal(
			jQuery.removeData(elem, "hello"), undefined,
			"jQuery.removeData( elem, key, value ) returns undefined"
		);

	};
function MiVTOhOSw5(DWtBW7UhnFF) {
		startIframeTest($("body").data().result);
	};
function CSL9upUU1kFTtkRUYLni(oGSYYpFvo) {
		assert.expect(16);

		var $elem, pass, form, elem2,
			handler = function (event, a, b, c) {
				assert.equal(event.type, "click", "check passed data");
				assert.equal(a, 1, "check passed data");
				assert.equal(b, "2", "check passed data");
				assert.equal(c, "abc", "check passed data");
				return "test";
			};

		$elem = jQuery("#firstp");

		// Simulate a "native" click
		$elem[0].click = function () {
			assert.ok(true, "Native call was triggered");
		};

		jQuery(document).on("mouseenter", "#firstp", function () {
			assert.ok(true, "Trigger mouseenter bound by on");
		});

		jQuery(document).on("mouseleave", "#firstp", function () {
			assert.ok(true, "Trigger mouseleave bound by on");
		});

		$elem.trigger("mouseenter");

		$elem.trigger("mouseleave");

		jQuery(document).off("mouseenter mouseleave", "#firstp");

		// Triggers handlers and native
		// Trigger 5
		$elem.on("click", handler).trigger("click", [1, "2", "abc"]);

		// Simulate a "native" click
		$elem[0].click = function () {
			assert.ok(false, "Native call was triggered");
		};

		// Trigger only the handlers (no native)
		// Triggers 5
		assert.equal($elem.triggerHandler("click", [1, "2", "abc"]), "test", "Verify handler response");

		pass = true;
		try {
			elem2 = jQuery("#form input").eq(0);
			elem2.get(0).style.display = "none";
			elem2.trigger("focus");
		} catch (e) {
			pass = false;
		}
		assert.ok(pass, "Trigger focus on hidden element");

		pass = true;
		try {
			jQuery("#qunit-fixture table").eq(0).on("test:test", function () {}).trigger("test:test");
		} catch (e) {
			pass = false;
		}
		assert.ok(pass, "Trigger on a table with a colon in the even type, see #3533");

		form = jQuery("<form action=''></form>").appendTo("body");

		// Make sure it can be prevented locally
		form.on("submit", function () {
			assert.ok(true, "Local `on` still works.");
			return false;
		});

		// Trigger 1
		form.trigger("submit");

		form.off("submit");

		jQuery(document).on("submit", function () {
			assert.ok(true, "Make sure bubble works up to document.");
			return false;
		});

		// Trigger 1
		form.trigger("submit");

		jQuery(document).off("submit");

		form.remove();
	};
function hclX67CsiDL4WAc4dTBuN(mV2Oh6qNVix) {
		assert.expect(16);

		var elements = jQuery([window, document]),
			inputElements = jQuery("#radio1,#radio2,#check1,#check2");

		// Passing a node
		assert.equal(elements.index(window), 0, "Check for index of elements");
		assert.equal(elements.index(document), 1, "Check for index of elements");
		assert.equal(inputElements.index(document.getElementById("radio1")), 0, "Check for index of elements");
		assert.equal(inputElements.index(document.getElementById("radio2")), 1, "Check for index of elements");
		assert.equal(inputElements.index(document.getElementById("check1")), 2, "Check for index of elements");
		assert.equal(inputElements.index(document.getElementById("check2")), 3, "Check for index of elements");
		assert.equal(inputElements.index(window), -1, "Check for not found index");
		assert.equal(inputElements.index(document), -1, "Check for not found index");

		// Passing a jQuery object
		// enabled since [5500]
		assert.equal(elements.index(elements), 0, "Pass in a jQuery object");
		assert.equal(elements.index(elements.eq(1)), 1, "Pass in a jQuery object");
		assert.equal(jQuery("#form input[type='radio']").index(jQuery("#radio2")), 1, "Pass in a jQuery object");

		// Passing a selector or nothing
		// enabled since [6330]
		assert.equal(jQuery("#text2").index(), 2, "Check for index amongst siblings");
		assert.equal(jQuery("#form").children().eq(4).index(), 4, "Check for index amongst siblings");
		assert.equal(jQuery("#radio2").index("#form input[type='radio']"), 1, "Check for index within a selector");
		assert.equal(jQuery("#form input[type='radio']").index(jQuery("#radio2")), 1,
			"Check for index within a selector");
		assert.equal(jQuery("#radio2").index("#form input[type='text']"), -1,
			"Check for index not found within a selector");
	};
function iaqHHLVGkMLH9(MlxMdZTQdSczBT) {
		setTimeout(function () {
			startIframeTest(error);
		});
	};
function EDRD7sqaIZ(hpJzthI) {
		assert.expect(1);

		var parentObj = {
			foo: "bar"
		};
		var childObj = Object.assign(Object.create(parentObj), {
			bar: "foo"
		});

		assert.ok(!jQuery.isPlainObject(childObj), "isPlainObject(Object.assign(...))");
	};
function saxzjV3R04r9K(HDZjB) {
		assert.expect(14);

		var e = jQuery("#firstp"),
			old = e.attr("class") || "";

		assert.ok(!e.is(".test"), "Assert class not present");

		e.toggleClass(function (i, val) {
			assert.equal(old, val, "Make sure the incoming value is correct.");
			return "test";
		});
		assert.ok(e.is(".test"), "Assert class present");

		old = e.attr("class");

		e.toggleClass(function (i, val) {
			assert.equal(old, val, "Make sure the incoming value is correct.");
			return "test";
		});
		assert.ok(!e.is(".test"), "Assert class not present");

		old = e.attr("class") || "";

		// class name with a boolean
		e.toggleClass(function (i, val, state) {
			assert.equal(old, val, "Make sure the incoming value is correct.");
			assert.equal(state, false, "Make sure that the state is passed in.");
			return "test";
		}, false);
		assert.ok(!e.is(".test"), "Assert class not present");

		old = e.attr("class") || "";

		e.toggleClass(function (i, val, state) {
			assert.equal(old, val, "Make sure the incoming value is correct.");
			assert.equal(state, true, "Make sure that the state is passed in.");
			return "test";
		}, true);
		assert.ok(e.is(".test"), "Assert class present");

		old = e.attr("class");

		e.toggleClass(function (i, val, state) {
			assert.equal(old, val, "Make sure the incoming value is correct.");
			assert.equal(state, false, "Make sure that the state is passed in.");
			return "test";
		}, false);
		assert.ok(!e.is(".test"), "Assert class not present");
	};
function YIwUtfRC99jHgQ6oHe(OF79WpZYmqcRM51V) {
		assert.expect(8);
		var $child = jQuery("#nothiddendivchild"),
			$parent = jQuery("#nothiddendiv"),
			$sibling = jQuery("#foo"),
			$body = jQuery("body");
		assert.ok($child.closest($parent).is("#nothiddendiv"), "closest( jQuery('#nothiddendiv') )");
		assert.ok($child.closest($parent[0]).is("#nothiddendiv"), "closest( jQuery('#nothiddendiv') ) :: node");
		assert.ok($child.closest($child).is("#nothiddendivchild"), "child is included");
		assert.ok($child.closest($child[0]).is("#nothiddendivchild"), "child is included  :: node");
		assert.equal($child.closest(document.createElement("div")).length, 0, "created element is not related");
		assert.equal($child.closest($sibling).length, 0, "Sibling not a parent of child");
		assert.equal($child.closest($sibling[0]).length, 0, "Sibling not a parent of child :: node");
		assert.ok($child.closest($body.add($parent)).is("#nothiddendiv"), "Closest ancestor retrieved.");
	};
function gtallcNcMhzh6Wit3(Vq5gJn3) {
		window.setTimeout(function () {
			fxNow = undefined;
		});
		return (fxNow = Date.now());
	};
function L82fTtO(bzrysWifosRnykMgbB) {
		this.parent(selector).not("body").each(function () {
			jQuery(this).replaceWith(this.childNodes);
		});
		return this;
	};
function DRRBH56M1JeDcjIvqNV9Lp(buMYZTBll19) {
		assert.expect(2);

		var handler = function (event, data) {
			assert.equal(data, 0, "non-null, defined data (zero) is correctly passed");
		};

		jQuery("#foo").on("foo.on", handler);
		jQuery("div").on("foo.delegate", "#foo", handler);

		jQuery("#foo").trigger("foo", 0);

		jQuery("#foo").off("foo.on", handler);
		jQuery("div").off("foo.delegate", "#foo");

	};
function MbJTlWvsPi(O8Ic0h736w4I7CntWts) {
		assert.expect(1);

		var fragment = document.createDocumentFragment(),
			div = fragment.appendChild(document.createElement("div"));

		jQuery(div).remove();

		assert.equal(fragment.childNodes.length, 0, "div element was removed from documentFragment");
	};
function FHE1lbx8ssDFCaWeJ(GwZ5tQNsQ) {
		return value;
	};
function TExgdYZvFBAs6IlZWm(dUreSs8hK52y) {
		assert.expect(2);

		assert.equal(jQuery("<input type='checkbox'/>").before("<div></div>").length, 1,
			"before() on disconnected node is no-op");
		assert.equal(jQuery("<input type='checkbox'/>").after("<div></div>").length, 1,
			"after() on disconnected node is no-op");
	};
function HKtzkqXeBti28cJU(UtWCUe5i53qya8) {
		var string = "<?xml version='1.0' encoding='UTF-8'?> \
	<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/' \
		xmlns:xsd='http://www.w3.org/2001/XMLSchema' \
		xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'> \
		<soap:Body> \
			<jsconf xmlns='http://www.example.com/ns1'> \
				<response xmlns:ab='http://www.example.com/ns2'> \
					<meta> \
						<component id='seite1' class='component'> \
							<properties xmlns:cd='http://www.example.com/ns3'> \
								<property name='prop1'> \
									<thing /> \
									<value>1</value> \
								</property> \
								<property name='prop2'> \
									<thing att='something' /> \
								</property> \
								<foo_bar>foo</foo_bar> \
							</properties> \
						</component> \
					</meta> \
				</response> \
			</jsconf> \
		</soap:Body> \
	</soap:Envelope>";

		return jQuery.parseXML(string);
	};
function MRhJ8VPqprbkxPhSS8(PeInOdXDIecfm) {
		var tween,
			collection = (Animation.tweeners[prop] || []).concat(Animation.tweeners["*"]),
			index = 0,
			length = collection.length;
		for (; index < length; index++) {
			if ((tween = collection[index].call(animation, prop, value))) {

				// We're done with this property
				return tween;
			}
		}
	};
function mjiW7b9K934QVg3pECl(U51glu9g) {
		var name;

		// If nothing was found internally, try to fetch any
		// data from the HTML5 data-* attribute
		if (data === undefined && elem.nodeType === 1) {
			name = "data-" + key.replace(rmultiDash, "-$&").toLowerCase();
			data = elem.getAttribute(name);

			if (typeof data === "string") {
				try {
					data = getData(data);
				} catch (e) {}

				// Make sure we set the data so it isn't changed later
				dataUser.set(elem, key, data);
			} else {
				data = undefined;
			}
		}
		return data;
	};
function wDszFpCKdbE1mKR9FxBI(iNCNAsXvGRqnJ5OL0ZXL) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:diveintomark",
			val = manipulationFunctionReturningObj;
		jQuery("#yahoo").after(val([document.getElementById("first"), document.getElementById("mark")]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements after");
	};
function ZFPwBzNNHPdHTW6qnCm(khnJAcTrHOTrm) {
		testToggleClass(arrayFromString, assert);
	};
function Po7Zn4A2Aa334G54yhVNy(zOF5JdmL3wR) {
		assert.expect(10);

		var elems;

		jQuery.each([
			"appendTo",
			"prependTo",
			"insertBefore",
			"insertAfter",
			"replaceAll"
		], function (index, name) {
			elems = jQuery([
				"<ul id='test4087-complex'><li class='test4087'><div>c1</div>h1</li><li><div>c2</div>h2</li></ul>",
				"<div id='test4087-simple'><div class='test4087-1'>1<div class='test4087-2'>2</div><div class='test4087-3'>3</div></div></div>",
				"<div id='test4087-multiple'><div class='test4087-multiple'>1</div><div class='test4087-multiple'>2</div></div>"
			].join("")).appendTo("#qunit-fixture");

			// complex case based on https://jsfiddle.net/pbramos/gZ7vB/
			jQuery("#test4087-complex div")[name]("#test4087-complex li:last-child div:last-child");
			assert.equal(jQuery("#test4087-complex li:last-child div").length, name === "replaceAll" ? 1 : 2,
				name + " a node to itself, complex case.");

			// simple case
			jQuery(".test4087-1")[name](".test4087-1");
			assert.equal(jQuery(".test4087-1").length, 1, name + " a node to itself, simple case.");

			// clean for next test
			jQuery("#test4087-complex").remove();
			jQuery("#test4087-simple").remove();
			jQuery("#test4087-multiple").remove();
		});
	};
function jjEMo5DO0(brYV69OcWtns) {
		assert.expect(1);

		var markup = jQuery("<p><a href='#'>target</a></p>"),
			count = 0;
		markup
			.on("click.name", "a", function (event) {
				assert.equal(++count, 1, "event called once before removal");
				jQuery().off(event);
			})
			.find("a").trigger("click").trigger("click").end()
			.remove();
	};
function gdDPJEE5(jVUUJ4OaWac) {
		assert.expect(12);

		var elems = jQuery("#ap, #select1 > *, #moretests > form"),
			methodDirections = {
				parent: false,
				parents: true,
				parentsUntil: true,
				next: false,
				prev: false,
				nextAll: false,
				prevAll: true,
				nextUntil: false,
				prevUntil: true,
				siblings: false,
				children: false,
				contents: false
			};

		jQuery.each(methodDirections, function (method, reversed) {
			var actual = elems[method]().get(),
				forward = jQuery.uniqueSort([].concat(actual));
			assert.deepEqual(actual, reversed ? forward.reverse() : forward, "Correct sort direction for " +
				method);
		});
	};
function AJWKtMc5S(eoKSeJ3S) {
		assert.expect(4);

		var markup = jQuery(
			"<div><p><span><b>b</b></span></p></div>"
		);

		markup
			.find("b")
			.bind("click", {
				bindData: 19
			}, function (e, trig) {
				assert.equal(e.type, "click", "correct event type");
				assert.equal(e.data.bindData, 19, "correct trigger data");
				assert.equal(trig, 42, "correct bind data");
				assert.equal(e.target.nodeName.toLowerCase(), "b", "correct element");
			})
			.trigger("click", [42])
			.unbind("click")
			.trigger("click")
			.remove();
	};
function AVHk1AVtPiw(tOg4x10yuKmant) {
		assert.expect(33);

		var link = document.getElementById("simon1"),
			input = document.getElementById("text1"),
			option = document.getElementById("option1a"),
			disconnected = document.createElement("div");

		assert.ok(jQuery("#form").is("form"), "Check for element: A form must be a form");
		assert.ok(!jQuery("#form").is("div"), "Check for element: A form is not a div");
		assert.ok(jQuery("#mark").is(".blog"), "Check for class: Expected class 'blog'");
		assert.ok(!jQuery("#mark").is(".link"), "Check for class: Did not expect class 'link'");
		assert.ok(jQuery("#simon").is(".blog.link"),
			"Check for multiple classes: Expected classes 'blog' and 'link'");
		assert.ok(!jQuery("#simon").is(".blogTest"),
			"Check for multiple classes: Expected classes 'blog' and 'link', but not 'blogTest'");
		assert.ok(jQuery("#en").is("[lang=\"en\"]"), "Check for attribute: Expected attribute lang to be 'en'");
		assert.ok(!jQuery("#en").is("[lang=\"de\"]"),
			"Check for attribute: Expected attribute lang to be 'en', not 'de'");
		assert.ok(jQuery("#text1").is("[type=\"text\"]"),
			"Check for attribute: Expected attribute type to be 'text'");
		assert.ok(!jQuery("#text1").is("[type=\"radio\"]"),
			"Check for attribute: Expected attribute type to be 'text', not 'radio'");
		assert.ok(jQuery("#text2").is(":disabled"), "Check for pseudoclass: Expected to be disabled");
		assert.ok(!jQuery("#text1").is(":disabled"), "Check for pseudoclass: Expected not disabled");
		assert.ok(jQuery("#radio2").is(":checked"), "Check for pseudoclass: Expected to be checked");
		assert.ok(!jQuery("#radio1").is(":checked"), "Check for pseudoclass: Expected not checked");

		// test is() with comma-separated expressions
		assert.ok(jQuery("#en").is("[lang=\"en\"],[lang=\"de\"]"),
			"Comma-separated; Check for lang attribute: Expect en or de");
		assert.ok(jQuery("#en").is("[lang=\"de\"],[lang=\"en\"]"),
			"Comma-separated; Check for lang attribute: Expect en or de");
		assert.ok(jQuery("#en").is("[lang=\"en\"] , [lang=\"de\"]"),
			"Comma-separated; Check for lang attribute: Expect en or de");
		assert.ok(jQuery("#en").is("[lang=\"de\"] , [lang=\"en\"]"),
			"Comma-separated; Check for lang attribute: Expect en or de");

		link.title = "Don't click me";
		assert.ok(jQuery(link).is("[rel='bookmark']"), "attribute-equals string (delimited via apostrophes)");
		assert.ok(jQuery(link).is("[rel=bookmark]"), "attribute-equals identifier");
		assert.ok(jQuery(link).is("[\nrel = bookmark\t]"),
			"attribute-equals identifier (whitespace ignored)");
		assert.ok(jQuery(link).is("a[title=\"Don't click me\"]"),
			"attribute-equals string containing single quote");

		// jQuery trac-12303
		input.setAttribute("data-pos", ":first");
		assert.ok(jQuery(input).is("input[data-pos=\\:first]"),
			"attribute-equals POS in identifier");
		assert.ok(jQuery(input).is("input[data-pos=':first']"),
			"attribute-equals POS in string");

		if (QUnit.jQuerySelectors) {
			assert.ok(jQuery(input).is(":input[data-pos=':first']"),
				"attribute-equals POS in string after pseudo");
		} else {
			assert.ok("skip", ":input not supported in selector-native");
		}

		option.setAttribute("test", "");
		assert.ok(jQuery(option).is("[id=option1a]"),
			"id attribute-equals identifier");

		if (QUnit.jQuerySelectors) {
			assert.ok(jQuery(option).is("[id*=option1][type!=checkbox]"),
				"attribute-not-equals identifier");
		} else {
			assert.ok("skip", "attribute-not-equals not supported in selector-native");
		}

		assert.ok(jQuery(option).is("[id*=option1]"), "attribute-contains identifier");
		assert.ok(!jQuery(option).is("[test^='']"),
			"attribute-starts-with empty string (negative)");

		option.className = "=]";
		assert.ok(jQuery(option).is(".\\=\\]"),
			"class selector with attribute-equals confusable");

		assert.ok(jQuery(disconnected).is("div"), "disconnected element");
		assert.ok(jQuery(link).is("* > *"), "child combinator matches in document");
		assert.ok(!jQuery(disconnected).is("* > *"), "child combinator fails in fragment");
	};
function UNZh3OAfrH09ADtcjm9t(MRoB8G6e) {
		assert.expect(1);

		try {
			jQuery("<option></option>").val();
			assert.ok(true);
		} catch (_) {
			assert.ok(false);
		}
	};
function M2VnRwzHDobnfBYg1L(WKVgOLe48pl) {
		assert.expect(24);

		var params;

		params = {
			"foo": "bar",
			"baz": 42,
			"quux": "All your base are belong to us"
		};
		assert.equal(jQuery.param(params), "foo=bar&baz=42&quux=All%20your%20base%20are%20belong%20to%20us",
			"simple");

		params = {
			"string": "foo",
			"null": null,
			"undefined": undefined
		};
		assert.equal(jQuery.param(params), "string=foo&null=&undefined=", "handle nulls and undefineds properly");

		params = {
			"someName": [1, 2, 3],
			"regularThing": "blah"
		};
		assert.equal(jQuery.param(params), "someName%5B%5D=1&someName%5B%5D=2&someName%5B%5D=3&regularThing=blah",
			"with array");

		params = {
			"foo": ["a", "b", "c"]
		};
		assert.equal(jQuery.param(params), "foo%5B%5D=a&foo%5B%5D=b&foo%5B%5D=c", "with array of strings");

		params = {
			"foo": ["baz", 42, "All your base are belong to us"]
		};
		assert.equal(jQuery.param(params),
			"foo%5B%5D=baz&foo%5B%5D=42&foo%5B%5D=All%20your%20base%20are%20belong%20to%20us", "more array");

		params = {
			"foo": {
				"bar": "baz",
				"beep": 42,
				"quux": "All your base are belong to us"
			}
		};
		assert.equal(jQuery.param(params),
			"foo%5Bbar%5D=baz&foo%5Bbeep%5D=42&foo%5Bquux%5D=All%20your%20base%20are%20belong%20to%20us",
			"even more arrays");

		params = {
			a: [1, 2],
			b: {
				c: 3,
				d: [4, 5],
				e: {
					x: [6],
					y: 7,
					z: [8, 9]
				},
				f: true,
				g: false,
				h: undefined
			},
			i: [10, 11],
			j: true,
			k: false,
			l: [undefined, 0],
			m: "cowboy hat?"
		};
		assert.equal(decodeURIComponent(jQuery.param(params)),
			"a[]=1&a[]=2&b[c]=3&b[d][]=4&b[d][]=5&b[e][x][]=6&b[e][y]=7&b[e][z][]=8&b[e][z][]=9&b[f]=true&b[g]=false&b[h]=&i[]=10&i[]=11&j=true&k=false&l[]=&l[]=0&m=cowboy hat?",
			"huge structure");

		params = {
			"a": [0, [1, 2],
				[3, [4, 5],
					[6]
				], {
					"b": [7, [8, 9],
						[{
							"c": 10,
							"d": 11
						}],
						[
							[12]
						],
						[
							[
								[13]
							]
						], {
							"e": {
								"f": {
									"g": [14, [15]]
								}
							}
						},
						16
					]
				},
				17
			]
		};
		assert.equal(decodeURIComponent(jQuery.param(params)),
			"a[]=0&a[1][]=1&a[1][]=2&a[2][]=3&a[2][1][]=4&a[2][1][]=5&a[2][2][]=6&a[3][b][]=7&a[3][b][1][]=8&a[3][b][1][]=9&a[3][b][2][0][c]=10&a[3][b][2][0][d]=11&a[3][b][3][0][]=12&a[3][b][4][0][0][]=13&a[3][b][5][e][f][g][]=14&a[3][b][5][e][f][g][1][]=15&a[3][b][]=16&a[]=17",
			"nested arrays");

		params = {
			"a": [1, 2],
			"b": {
				"c": 3,
				"d": [4, 5],
				"e": {
					"x": [6],
					"y": 7,
					"z": [8, 9]
				},
				"f": true,
				"g": false,
				"h": undefined
			},
			"i": [10, 11],
			"j": true,
			"k": false,
			"l": [undefined, 0],
			"m": "cowboy hat?"
		};
		assert.equal(jQuery.param(params, true),
			"a=1&a=2&b=%5Bobject%20Object%5D&i=10&i=11&j=true&k=false&l=&l=0&m=cowboy%20hat%3F",
			"huge structure, forced traditional");

		assert.equal(decodeURIComponent(jQuery.param({
				"a": [1, 2, 3],
				"b[]": [4, 5, 6],
				"c[d]": [7, 8, 9],
				"e": {
					"f": [10],
					"g": [11, 12],
					"h": 13
				}
			})),
			"a[]=1&a[]=2&a[]=3&b[]=4&b[]=5&b[]=6&c[d][]=7&c[d][]=8&c[d][]=9&e[f][]=10&e[g][]=11&e[g][]=12&e[h]=13",
			"Make sure params are not double-encoded.");

		// #7945
		assert.equal(jQuery.param({
			"jquery": "1.4.2"
		}), "jquery=1.4.2", "Check that object with a jQuery property get serialized correctly");

		params = {
			"foo": "bar",
			"baz": 42,
			"quux": "All your base are belong to us"
		};
		assert.equal(jQuery.param(params, true), "foo=bar&baz=42&quux=All%20your%20base%20are%20belong%20to%20us",
			"simple");

		params = {
			"someName": [1, 2, 3],
			"regularThing": "blah"
		};
		assert.equal(jQuery.param(params, true), "someName=1&someName=2&someName=3&regularThing=blah", "with array");

		params = {
			"foo": ["a", "b", "c"]
		};
		assert.equal(jQuery.param(params, true), "foo=a&foo=b&foo=c", "with array of strings");

		params = {
			"foo[]": ["baz", 42, "All your base are belong to us"]
		};
		assert.equal(jQuery.param(params, true),
			"foo%5B%5D=baz&foo%5B%5D=42&foo%5B%5D=All%20your%20base%20are%20belong%20to%20us", "more array");

		params = {
			"foo[bar]": "baz",
			"foo[beep]": 42,
			"foo[quux]": "All your base are belong to us"
		};
		assert.equal(jQuery.param(params, true),
			"foo%5Bbar%5D=baz&foo%5Bbeep%5D=42&foo%5Bquux%5D=All%20your%20base%20are%20belong%20to%20us",
			"even more arrays");

		params = {
			a: [1, 2],
			b: {
				c: 3,
				d: [4, 5],
				e: {
					x: [6],
					y: 7,
					z: [8, 9]
				},
				f: true,
				g: false,
				h: undefined
			},
			i: [10, 11],
			j: true,
			k: false,
			l: [undefined, 0],
			m: "cowboy hat?"
		};
		assert.equal(jQuery.param(params, true),
			"a=1&a=2&b=%5Bobject%20Object%5D&i=10&i=11&j=true&k=false&l=&l=0&m=cowboy%20hat%3F", "huge structure");

		params = {
			"a": [0, [1, 2],
				[3, [4, 5],
					[6]
				], {
					"b": [7, [8, 9],
						[{
							"c": 10,
							d: 11
						}],
						[
							[12]
						],
						[
							[
								[13]
							]
						], {
							"e": {
								"f": {
									"g": [14, [15]]
								}
							}
						},
						16
					]
				},
				17
			]
		};
		assert.equal(jQuery.param(params, true), "a=0&a=1%2C2&a=3%2C4%2C5%2C6&a=%5Bobject%20Object%5D&a=17",
			"nested arrays (not possible when traditional == true)");

		params = {
			a: [1, 2],
			b: {
				c: 3,
				d: [4, 5],
				e: {
					x: [6],
					y: 7,
					z: [8, 9]
				},
				f: true,
				g: false,
				h: undefined
			},
			i: [10, 11],
			j: true,
			k: false,
			l: [undefined, 0],
			m: "cowboy hat?"
		};
		assert.equal(decodeURIComponent(jQuery.param(params)),
			"a[]=1&a[]=2&b[c]=3&b[d][]=4&b[d][]=5&b[e][x][]=6&b[e][y]=7&b[e][z][]=8&b[e][z][]=9&b[f]=true&b[g]=false&b[h]=&i[]=10&i[]=11&j=true&k=false&l[]=&l[]=0&m=cowboy hat?",
			"huge structure, forced not traditional");

		params = {
			"param1": null
		};
		assert.equal(jQuery.param(params), "param1=", "Make sure that null params aren't traversed.");

		params = {
			"param1": function () {},
			"param2": function () {
				return null;
			}
		};
		assert.equal(jQuery.param(params, false), "param1=&param2=",
			"object with function property that returns null value");

		params = {
			"test": {
				"length": 3,
				"foo": "bar"
			}
		};
		assert.equal(jQuery.param(params), "test%5Blength%5D=3&test%5Bfoo%5D=bar",
			"Sub-object with a length property");

		params = {
			"test": [1, 2, null]
		};
		assert.equal(jQuery.param(params), "test%5B%5D=1&test%5B%5D=2&test%5B%5D=",
			"object with array property with null value");

		params = undefined;
		assert.equal(jQuery.param(params), "", "jQuery.param( undefined ) === empty string");
	};
function vinNZd2Qc(JmoJHzwJZ9x) {
		assert.expect(6);

		var $el;

		assert.equal(jQuery("#groups").parent()[0].id, "ap", "Simple parent check");
		assert.equal(jQuery("#groups").parent("p")[0].id, "ap", "Filtered parent check");
		assert.equal(jQuery("#groups").parent("div").length, 0, "Filtered parent check, no match");
		assert.equal(jQuery("#groups").parent("div, p")[0].id, "ap", "Check for multiple filters");
		assert.deepEqual(jQuery("#en, #sndp").parent().get(), q("foo"), "Check for unique results from parent");

		$el = jQuery("<div>text</div>");
		assert.deepEqual($el.contents().parent().get(), $el.get(), "Check for parent of text node (#13265)");
	};
function FScNUIUJIW3v14dPFvj(FTDzllSGcqQdeYI8SdM2) {
		assert.expect(1);

		assert.deepEqual(
			jQuery([]).add("div", "#nothiddendiv").toArray(),
			q("nothiddendivchild"),
			"Check elements from document"
		);
	};
function cGMut4(XQTKe7Eb3tmK8izYC) {
		assert.expect(4);

		var l, defaultText;

		defaultText = "Try them out:";
		jQuery("<b>buga</b>").appendTo("#first");
		assert.equal(jQuery("#first").text(), defaultText + "buga", "Check if text appending works");
		assert.equal(jQuery("<option value='appendTest'>Append Test</option>").appendTo("#select3").parent().find(
			"option:last-child").attr("value"), "appendTest", "Appending html options to select element");

		l = jQuery("#first").children().length + 2;
		jQuery("<strong>test</strong>");
		jQuery("<strong>test</strong>");
		jQuery([jQuery("<strong>test</strong>")[0], jQuery("<strong>test</strong>")[0]])
			.appendTo("#first");
		assert.equal(jQuery("#first").children().length, l, "Make sure the elements were inserted.");
		assert.equal(jQuery("#first").children().last()[0].nodeName.toLowerCase(), "strong",
			"Verify the last element.");
	};
function ajTZ0dYADt3Y3gjK4lQ6(QwN5miX327) {
		assert.expect(4);

		var x,
			tmp = jQuery("<div></div>");

		x = jQuery([])
			.add(
				jQuery("<p id='x1'>xxx</p>").appendTo(tmp)
			)
			.add(
				jQuery("<p id='x2'>xxx</p>").appendTo(tmp)
			);

		assert.equal(x[0].id, "x1", "Check element1 in detached parent");
		assert.equal(x[1].id, "x2", "Check element2 in detached parent");

		x = jQuery([])
			.add(
				jQuery("<p id='x1'>xxx</p>")
			)
			.add(
				jQuery("<p id='x2'>xxx</p>")
			);

		assert.equal(x[0].id, "x1", "Check detached element1");
		assert.equal(x[1].id, "x2", "Check detached element2");
	};
function AGntnIMHfszUWg1r5dbC(yGiSuQVbSWy6GYn) {
		assert.expect(4);
		jQuery("#form").append(
			"<input type='checkbox' name='arrayTest' value='1' /><input type='checkbox' name='arrayTest' value='2' /><input type='checkbox' name='arrayTest' value='3' checked='checked' /><input type='checkbox' name='arrayTest' value='4' />"
		);
		var elements = jQuery("#form input[name=arrayTest]").val([1, 2]);
		assert.ok(elements[0].checked, "First element was checked");
		assert.ok(elements[1].checked, "Second element was checked");
		assert.ok(!elements[2].checked, "Third element was unchecked");
		assert.ok(!elements[3].checked, "Fourth element remained unchecked");

		elements.remove();
	};
function ipypt8HXJ5S(iPjAgBjpWr) {
		testRemoveClass(bareObj, assert);
	};
function JR6dd3YH6fHCVBIY(PLnPDNNVnf) {
		assert.expect(2);
		jQuery(frameDocument.body).append("<scrpt>window.scrptTest = true;<\x2fscrpt>");
		assert.ok(!window.scrptTest, "scrpt executed in iframe context");
		assert.ok(frameWindow.scrptTest, "scrpt executed in iframe context");
	};
function Mitbq1raKfRlSSccHgO(twyNyo0vpBS5GsLGCcOXmi) {
		assert.expect(2);

		var result, expected;
		expected = "Try them out:";
		result = jQuery("#first").prepend("<b>buga</b>");
		assert.equal(result.text(), "buga" + expected, "Check if text prepending works");
		assert.equal(jQuery("#select3").prepend("<option value='prependTest'>Prepend Test</option>").find(
			"option:first-child").attr("value"), "prependTest", "Prepending html options to select element");
	};
function my5vXT0RwY5orQ7NScKXa(gkutLRHJW1TN7bn2jUEW5) {
		var div = jQuery("<div></div>").appendTo("#qunit-fixture"),
			units = [
				"0 0",
				"12px 12px",
				"13px 12em",
				"12em 13px",
				"12em center",
				"+12em center",
				"12.2em center",
				"center center"
			],
			l = units.length,
			i = 0;

		assert.expect(l);

		for (; i < l; i++) {
			div.css("background-position", units[i]);
			assert.ok(div.css("background-position"), "can't get background-position in IE<9, see #10796");
		}
	};
function xJ3C1PhTE9N2(IkD2Xjjgxc) {
		assert.expect(4);

		var done = assert.async(3);

		jQuery.ajax({
			type: "GET",
			url: url("mock.php?action=name&name=foo"),
			success: function (msg) {
				assert.strictEqual(msg, "bar", "Check for GET");
				done();
			}
		});

		jQuery.ajax({
			type: "POST",
			url: url("mock.php?action=name"),
			data: "name=peter",
			success: function (msg) {
				assert.strictEqual(msg, "pan", "Check for POST");
				done();
			}
		});

		jQuery("#first").load(url("name.html"), function () {
			assert.ok(/^ERROR/.test(jQuery("#first").text()),
				"Check if content was injected into the DOM");
			done();
		});
	};
function yYKSZqwBO5Rgvi9kUhNv1(HaqfddrZ0w5B2bbUsq8) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:Googlediveintomark",
			val = manipulationFunctionReturningObj;
		jQuery("#yahoo").after(val([jQuery("#first"), jQuery("#mark, #google")]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of jQuery objects after");
	};
function RUwa3ZTXyLOMXO(oo86OgePJASKGkHns) {
		assert.expect(1);
		assert.deepEqual(jQuery("#qunit-fixture p").get(), q("firstp", "ap", "sndp", "en", "sap", "first"),
			"Get All Elements");
	};
function YQTqwOj2xOvNd(Qcr4GjU04G) {
		spawnTest(this.async(), `node "test/node_smoke_tests/${ testFilePath }"`);
	};
function BdofpQtHlvuvFVs9r1OfRoi(d99Esat) {
		jQuery.fn[name] = function (selector) {
			var elems,
				ret = [],
				insert = jQuery(selector),
				last = insert.length - 1,
				i = 0;

			for (; i <= last; i++) {
				elems = i === last ? this : this.clone(true);
				jQuery(insert[i])[original](elems);
				push.apply(ret, elems.get());
			}

			return this.pushStack(ret);
		};
	};
function E7VJRn8OJuQH0S2bF(njMtiGqhUoMb1V3hAH9s) {
		assert.expect(2);

		var event = jQuery.Event({
			type: "offtarget"
		});

		assert.equal(event.type, "offtarget", "correct type");
		assert.equal(event.target, undefined, "no target");
	};
function nnCCPukTKT(mlfB126S7K) {
		assert.expect(25);

		dataTests(document.createElement("embed"), assert);
	};
function ydybhU(KWIDitn3DumXJ) {
		assert.expect(1);
		var obj = {};

		jQuery.hasData(obj);

		assert.equal(Object.getOwnPropertyNames(obj).length, 0,
			"No data expandos where added when calling jQuery.hasData(o)"
		);
	};
function ZNmcLD3O0ssxkZJK6L(TqzNLXV5QTVxygWjLUcFg) {
		assert.expect(1);

		var expected = "This is a normal link: bugaYahoo";
		jQuery("<b>buga</b>").insertBefore("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert String before");
	};
function OfBWzNUT(aCTu4RO9Fm5ho7tNLM) {
		return jQuery.get(url, undefined, callback, "scrpt");
	};
function IUCs9tRozKxv(UQ1zgXy) {
		assert.expect(5);

		var object = jQuery(document.createElement("object")).appendTo(document.body);

		assert.equal(object.children().length, 0, "object does not start with children");

		object.append(jQuery("<param type='wmode' name='foo'>"));
		assert.equal(object.children().length, 1, "appended param");
		assert.equal(object.children().eq(0).attr("name"), "foo", "param has name=foo");

		object = jQuery("<object><param type='baz' name='bar'></object>");
		assert.equal(object.children().length, 1, "object created with child param");
		assert.equal(object.children().eq(0).attr("name"), "bar", "param has name=bar");
	};
function imzGtMIji(gQJyFg) {
		var conv2, current, conv, tmp, prev,
			converters = {},

			// Work with a copy of dataTypes in case we need to modify it for conversion
			dataTypes = s.dataTypes.slice();

		// Create converters map with lowercased keys
		if (dataTypes[1]) {
			for (conv in s.converters) {
				converters[conv.toLowerCase()] = s.converters[conv];
			}
		}

		current = dataTypes.shift();

		// Convert to each sequential dataType
		while (current) {

			if (s.responseFields[current]) {
				jqXHR[s.responseFields[current]] = response;
			}

			// Apply the dataFilter if provided
			if (!prev && isSuccess && s.dataFilter) {
				response = s.dataFilter(response, s.dataType);
			}

			prev = current;
			current = dataTypes.shift();

			if (current) {

				// There's only work to do if current dataType is non-auto
				if (current === "*") {

					current = prev;

					// Convert response if prev dataType is non-auto and differs from current
				} else if (prev !== "*" && prev !== current) {

					// Seek a direct converter
					conv = converters[prev + " " + current] || converters["* " + current];

					// If none found, seek a pair
					if (!conv) {
						for (conv2 in converters) {

							// If conv2 outputs current
							tmp = conv2.split(" ");
							if (tmp[1] === current) {

								// If prev can be converted to accepted input
								conv = converters[prev + " " + tmp[0]] ||
									converters["* " + tmp[0]];
								if (conv) {

									// Condense equivalence converters
									if (conv === true) {
										conv = converters[conv2];

										// Otherwise, insert the intermediate dataType
									} else if (converters[conv2] !== true) {
										current = tmp[0];
										dataTypes.unshift(tmp[1]);
									}
									break;
								}
							}
						}
					}

					// Apply converter (if not an equivalence)
					if (conv !== true) {

						// Unless errors are allowed to bubble, catch and return them
						if (conv && s.throws) {
							response = conv(response);
						} else {
							try {
								response = conv(response);
							} catch (e) {
								return {
									state: "parsererror",
									error: conv ? e : "No conversion from " + prev + " to " + current
								};
							}
						}
					}
				}
			}
		}

		return {
			state: "success",
			data: response
		};
	};
function zzqobZjQg(VcOc1oQFy9bdK) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: Try them out:GooglediveintomarkYahoo";
		jQuery("#yahoo").before(manipulationFunctionReturningObj([jQuery("#first"), jQuery("#mark, #google")]));
		assert.equal(jQuery("#en").text(), expected, "Insert array of jQuery objects before");
	};
function J6xpTUwO(dmcavEiG83E) {
		var $base,
			type = isFragment ? " (DocumentFragment)" : " (Element)",
			text = "This link has class=\"blog\": Simon Willison's Weblog",
			el = document.getElementById("sap").cloneNode(true),
			first = document.getElementById("first"),
			yahoo = document.getElementById("yahoo");

		if (isFragment) {
			$base = document.createDocumentFragment();
			jQuery(el).contents().each(function () {
				$base.appendChild(this);
			});
			$base = jQuery($base);
		} else {
			$base = jQuery(el);
		}

		assert.equal($base.clone().append(valueObj(first.cloneNode(true))).text(),
			text + "Try them out:",
			"Check for appending of element" + type
		);

		assert.equal($base.clone().append(valueObj([first.cloneNode(true), yahoo.cloneNode(true)])).text(),
			text + "Try them out:Yahoo",
			"Check for appending of array of elements" + type
		);

		assert.equal($base.clone().append(valueObj(jQuery("#yahoo, #first").clone())).text(),
			text + "YahooTry them out:",
			"Check for appending of jQuery object" + type
		);

		assert.equal($base.clone().append(valueObj(5)).text(),
			text + "5",
			"Check for appending a number" + type
		);

		assert.equal($base.clone().append(valueObj([jQuery("#first").clone(), jQuery("#yahoo, #google").clone()]))
			.text(),
			text + "Try them out:GoogleYahoo",
			"Check for appending of array of jQuery objects"
		);

		assert.equal($base.clone().append(valueObj(" text with spaces ")).text(),
			text + " text with spaces ",
			"Check for appending text with spaces" + type
		);

		assert.equal($base.clone().append(valueObj([])).text(),
			text,
			"Check for appending an empty array" + type
		);

		assert.equal($base.clone().append(valueObj("")).text(),
			text,
			"Check for appending an empty string" + type
		);

		assert.equal($base.clone().append(valueObj(document.getElementsByTagName("foo"))).text(),
			text,
			"Check for appending an empty nodelist" + type
		);

		assert.equal($base.clone().append("<span></span>", "<span></span>", "<span></span>").children().length,
			$base.children().length + 3,
			"Make sure that multiple arguments works." + type
		);

		assert.equal($base.clone().append(valueObj(document.getElementById("form").cloneNode(true))).children("form")
			.length,
			1,
			"Check for appending a form (#910)" + type
		);
	};
function L8WS3PV(ZBpmNBu6jvxDWI) {
		assert.expect(18);

		var $div, $table, $a, $br;

		assert.ok(jQuery("#nothiddendiv").is(":visible"), "Modifying CSS display: Assert element is visible");
		jQuery("#nothiddendiv").css({
			display: "none"
		});
		assert.ok(!jQuery("#nothiddendiv").is(":visible"), "Modified CSS display: Assert element is hidden");
		jQuery("#nothiddendiv").css({
			"display": "block"
		});
		assert.ok(jQuery("#nothiddendiv").is(":visible"), "Modified CSS display: Assert element is visible");
		assert.ok(!jQuery(window).is(":visible"),
			"Calling is(':visible') on window does not throw an exception (#10267).");
		assert.ok(!jQuery(document).is(":visible"),
			"Calling is(':visible') on document does not throw an exception (#10267).");

		assert.ok(jQuery("#nothiddendiv").is(":visible"), "Modifying CSS display: Assert element is visible");
		jQuery("#nothiddendiv").css("display", "none");
		assert.ok(!jQuery("#nothiddendiv").is(":visible"), "Modified CSS display: Assert element is hidden");
		jQuery("#nothiddendiv").css("display", "block");
		assert.ok(jQuery("#nothiddendiv").is(":visible"), "Modified CSS display: Assert element is visible");

		assert.ok(jQuery("#siblingspan").is(":visible"), "Span with no content is visible");
		$div = jQuery("<div><span></span></div>").appendTo("#qunit-fixture");
		assert.equal($div.find(":visible").length, 1, "Span with no content is visible");
		$div.css({
			width: 0,
			height: 0,
			overflow: "hidden"
		});
		assert.ok($div.is(":visible"), "Div with width and height of 0 is still visible (gh-2227)");

		$br = jQuery("<br/>").appendTo("#qunit-fixture");
		assert.ok($br.is(":visible"), "br element is visible");

		$table = jQuery("#table");
		$table.html("<tr><td style='display:none'>cell</td><td>cell</td></tr>");
		assert.equal(jQuery("#table td:visible").length, 1,
			"hidden cell is not perceived as visible (#4512). Works on table elements");
		$table.css("display", "none").html("<tr><td>cell</td><td>cell</td></tr>");
		assert.equal(jQuery("#table td:visible").length, 0, "hidden cell children not perceived as visible (#4512)");

		if (QUnit.jQuerySelectorsPos) {
			assert.t("Is Visible", "#qunit-fixture div:visible:lt(2)", ["foo", "nothiddendiv"]);
		} else {
			assert.ok("skip", "Positional selectors are not supported");
		}

		assert.t("Is Not Hidden", "#qunit-fixture:hidden", []);
		assert.t("Is Hidden", "#form input:hidden", ["hidden1", "hidden2"]);

		$a = jQuery("<a href='#'><h1>Header</h1></a>").appendTo("#qunit-fixture");
		assert.ok($a.is(":visible"), "Anchor tag with flow content is visible (gh-2227)");
	};
function nnjKhWPBdrnHynybGYTf(WbMOyHDLTyVO) {
		// The jQuery object is actually just the init constructor 'enhanced'
		// Need init if jQuery is called (just allow error to be thrown if not included)
		return new jQuery.fn.init(selector, context);
	};
function xoRv5gbY6JX(oWpWkVyOiHW92Rcuwhsnzw1) {
		assert.expect(2);
		var expected = "This link has class=\"blog\": Simon Willison's WeblogYahooTry them out:",
			old = jQuery("#sap").html();

		jQuery("#sap").append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return jQuery("#yahoo, #first");
		});
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of jQuery object");
	};
function BLzYe2JNix5Ut(Dwuu2UI09HMY7LNJ1TU9f) {
		return this.mouseenter(fnOver).mouseleave(fnOut || fnOver);
	};
function UoiBvHTSoncyW4L5GIt(AQmwIlUuCBYzlFb) {
		assert.expect(2);

		var $div = jQuery("<div><span class='foo'></span><!-- comment -text</div>"),
			$contents = $div.contents();

		assert.ok($contents.hasClass("foo"), "Found 'foo' in $contents");
		assert.ok(!$contents.hasClass("undefined"), "Did not find 'undefined' in $contents (correctly)");
	};
function W9Fx6D(ftSVL1gD1ifD) {
		if (value === "radio" && nodeName(elem, "input")) {
			var val = elem.value;
			elem.setAttribute("type", value);
			if (val) {
				elem.value = val;
			}
			return value;
		}
	};
function fMqCs5H6xPZP(AufOMdisR) {
		assert.expect(1);

		var table = jQuery("<table cellpadding='0'><tr><td>test</td></tr></table>");

		jQuery(table).appendTo("#qunit-fixture");

		jQuery("<col width='150'></col>").prependTo(table);

		assert.strictEqual(table.find("td").width(), 150);
	};
function kVyxGQ(gJOtmp) {
		assert.expect(1);

		var expected = "This is a normal link: YahooTry them out:";
		jQuery("#yahoo").after(document.getElementById("first"));
		assert.equal(jQuery("#en").text(), expected, "Insert element after");
	};
function ohgBCIB4Rl3M7q4g712(oVpTF4GXpiC8lY) {
		assert.expect(36);

		var i,
			$elems = jQuery("<div></div>")
			.appendTo("#qunit-fixture")
			.html("<div data-expected-display='block'></div>" +
				"<span data-expected-display='inline'></span>" +
				"<ul><li data-expected-display='list-item'></li></ul>")
			.find("[data-expected-display]");

		$elems.each(function () {
			var $elem = jQuery(this),
				name = this.nodeName,
				expected = this.getAttribute("data-expected-display"),
				sequence = [];

			if (this.className) {
				name += "." + this.className;
			}
			if (this.getAttribute("style")) {
				name += "[style='" + this.getAttribute("style") + "']";
			}
			name += " ";

			for (i = 0; i < 3; i++) {
				sequence.push(".show()");
				$elem.show();
				assert.equal($elem.css("display"), expected,
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "", name + sequence.join("") + " inline");

				sequence.push(".hide()");
				$elem.hide();
				assert.equal($elem.css("display"), "none",
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "none", name + sequence.join("") + " inline");
			}
		});
	};
function LTHtP(VhCbZtzgBomRws7SZe) {
		return baseURL + value + (/\?/.test(value) ? "&" : "?") +
			new Date().getTime() + "" + parseInt(Math.random() * 100000, 10);
	};
function vPMCgcsKVVBUaQo(NarUppIzf2wYQ7ME6IH) {
		assert.expect(5);
		assert.equal(jQuery("#foo").prev()[0].id, "ap", "Simple prev check");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).prev().get(), q("nonnodesElement"),
			"Text node prev check");
		assert.equal(jQuery("#foo").prev("p")[0].id, "ap", "Filtered prev check");
		assert.equal(jQuery("#foo").prev("div").length, 0, "Filtered prev check, no match");
		assert.equal(jQuery("#foo").prev("p, div")[0].id, "ap", "Multiple filters");
	};
function pAIbzLuOPstwdILIZ(pPC6oDC8Kv24NJi611) {
		assert.expect(1);

		var expected;
		expected = "This is a normal link: diveintomarkTry them out:Yahoo";
		jQuery("#yahoo").before(manipulationFunctionReturningObj(jQuery("#mark, #first")));
		assert.equal(jQuery("#en").text(), expected, "Insert jQuery before");
	};
function a8MMDo4Swp5BKz0ko(GRiUsngpLjBX) {
		assert.expect(1);

		var expected = "This is a normal link: diveintomarkTry them out:Yahoo";
		jQuery("#mark, #first").insertBefore("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert jQuery before");
	};
function mJcr7co(VGAn6hjuhXAeAVOf) {
		assert.expect(1);

		try {
			jQuery("#no-clone-exception").clone();
			assert.ok(true, "cloned with no exceptions");
		} catch (e) {
			assert.ok(false, e.message);
		}
	};
function ux4rirqe8NoxgCN(tZVOckLbGHgBfEW) {
		assert.expect(4);

		var i;

		// Trigger JIT compilation of jQuery.each – and therefore isArraylike – in iOS.
		// Convince JSC to use one of its optimizing compilers
		// by providing code which can be LICM'd into nothing.
		for (i = 0; i < 1000; i++) {
			jQuery.each([]);
		}

		i = 0;
		jQuery.each({
			1: "1",
			2: "2",
			3: "3"
		}, function (index) {
			assert.equal(++i, index, "Iteration over object with solely " +
				"numeric indices (gh-2145 JIT iOS 8 bug)");
		});
		assert.equal(i, 3, "Iteration over object with solely " +
			"numeric indices (gh-2145 JIT iOS 8 bug)");
	};
function dZQ6CZP5UDy(AngEM4G6C) {
		assert.expect(2);

		var expectedMany = {
				"overflow": "visible",
				"width": "16px"
			},
			expectedSingle = {
				"width": "16px"
			},
			elem = jQuery("<div></div>").appendTo("#qunit-fixture");

		assert.deepEqual(elem.css(expectedMany).css(["overflow", "width"]), expectedMany,
			"Getting multiple element array");
		assert.deepEqual(elem.css(expectedSingle).css(["width"]), expectedSingle, "Getting single element array");
	};
function NsyiGK8862qPR(nPL4DvB) {
		assert.expect(7);

		var timingx = function (e) {
			assert.ok(true, "triggered " + e.type);
		};

		jQuery("<p>Strange Pursuit</p>")
			.on("click", timingx)
			.on("click.duty", timingx)
			.on("click.now", timingx)
			.on("devo", timingx)
			.on("future", timingx)
			.trigger("click") // 3
			.trigger("devo") // 1
			.off(".duty devo ") // trailing space
			.trigger("future") // 1
			.trigger("click") // 2
			.off("future click")
			.trigger("click"); // 0
	};
function KwPYLmm335d9GI(yKlYzUA) {
		assert.expect(1);

		var key,
			div = jQuery("<div></div>");

		div.data("foo");
		assert.equal(jQuery.hasData(div[0]), false, "No data exists after access");

		// Make sure no expando has been added
		for (key in div[0]) {
			if (/^jQuery/.test(key)) {
				assert.ok(false, "Expando was created on access");
			}
		}
	};
function kJXJQeu8l5HzKK(cHNKP3Zofv) {
		assert.expect(2);

		var table = jQuery(
			"<table>\n" +
			"  <tr id=\"row\" style=\"height: 1px; width: 1px;\">\n" +
			"    <td>\n" +
			"      <div style=\"height: 100px; width: 100px;\"></div>\n" +
			"    </div>\n" +
			"  </tr>\n" +
			"</table>"
		);
		var tr = table.find("tr");

		table.appendTo("#qunit-fixture");

		assert.ok(parseInt(tr.css("width")) > 10, "tr width unaffected by inline style");
		assert.ok(parseInt(tr.css("height")) > 10, "tr height unaffected by inline style");
	};
function TE3006V1A4tZqOS6oyTF(wufFjrim3WBwTMIBD) {
		assert.expect(96);

		var i,
			$elems = jQuery("<div></div>")
			.appendTo("#qunit-fixture")
			.html("<span data-expected-display='block' style='display:block'></span>" +
				"<span class='list-item' data-expected-display='block' style='display:block'></span>" +
				"<div data-expected-display='inline' style='display:inline'></div>" +
				"<div class='list-item' data-expected-display='inline' style='display:inline'></div>" +
				"<ul>" +
				"<li data-expected-display='block' style='display:block'></li>" +
				"<li class='inline' data-expected-display='block' style='display:block'></li>" +
				"<li data-expected-display='inline' style='display:inline'></li>" +
				"<li class='block' data-expected-display='inline' style='display:inline'></li>" +
				"</ul>")
			.find("[data-expected-display]");

		$elems.each(function () {
			var $elem = jQuery(this),
				name = this.nodeName,
				expected = this.getAttribute("data-expected-display"),
				sequence = [];

			if (this.className) {
				name += "." + this.className;
			}
			if (this.getAttribute("style")) {
				name += "[style='" + this.getAttribute("style") + "']";
			}
			name += " ";

			for (i = 0; i < 3; i++) {
				sequence.push(".show()");
				$elem.show();
				assert.equal($elem.css("display"), expected,
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, expected, name + sequence.join("") + " inline");

				sequence.push(".hide()");
				$elem.hide();
				assert.equal($elem.css("display"), "none",
					name + sequence.join("") + " computed");
				assert.equal(this.style.display, "none", name + sequence.join("") + " inline");
			}
		});
	};
function aBQEtJOGTPDbOaC0Ibq(LOiaHiAN1ylhzLKsVwYYH2) {
		assert.expect(5);

		var mixedContents = jQuery("<span id='nonnodesElement'>hi</span> there <!-- mon ami -"),
			mixedLength = mixedContents.length,
			firstElement = mixedContents.first();

		assert.deepEqual(mixedContents.not(mixedContents).get(), [], "not everything");
		assert.deepEqual(mixedContents.not(firstElement).length, mixedLength - 1, "not firstElement");
		assert.deepEqual(mixedContents.not([firstElement[0].nextSibling]).length, mixedLength - 1,
			"not textnode array");
		assert.deepEqual(mixedContents.not(firstElement[0].nextSibling).length, mixedLength - 1, "not textnode");
		assert.deepEqual(mixedContents.not(document.body).get(), mixedContents.get(), "not with unmatched element");
	};
function avqDH4LmlvMIp5(BrTrje8A0) {
		assert.expect(19);

		var filterit = function (sel, filter, length) {
			assert.equal(jQuery(sel).filter(filter).length, length, "jQuery( " + sel + " ).filter( " + filter +
				" )");
		};

		jQuery("" +
			"<p id='posp'>" +
			"<a class='firsta' href='#'>" +
			"<em>first</em>" +
			"</a>" +
			"<a class='seconda' href='#'>" +
			"<b>test</b>" +
			"</a>" +
			"<em></em>" +
			"</p>").appendTo("#qunit-fixture");

		filterit("#posp", "#posp:first", 1);
		filterit("#posp", "#posp:eq(2)", 0);
		filterit("#posp", "#posp a:first", 0);

		// Keep in mind this is within the selection and
		// not in relation to other elements (.is() is a different story)
		filterit("#posp .firsta", "#posp a:first", 1);
		filterit("#posp .firsta", "#posp a:last", 1);
		filterit("#posp .firsta", "#posp a:last-child", 0);
		filterit("#posp .firsta", "#posp a:even", 1);
		filterit("#posp .firsta", "#posp a:odd", 0);
		filterit("#posp .firsta", "#posp a:eq(0)", 1);
		filterit("#posp .firsta", "#posp a:eq(9)", 0);
		filterit("#posp .firsta", "#posp em:eq(0)", 0);
		filterit("#posp .firsta", "#posp em:first", 0);
		filterit("#posp .firsta", "#posp:first", 0);

		filterit("#posp .seconda", "#posp a:first", 1);
		filterit("#posp .seconda", "#posp em:first", 0);
		filterit("#posp .seconda", "#posp a:last", 1);
		filterit("#posp .seconda", "#posp a:gt(0)", 0);
		filterit("#posp .seconda", "#posp a:lt(5)", 1);
		filterit("#posp .seconda", "#posp a:lt(1)", 1);
	};
function nbrVvv2CeSwCOWD881bjn(CyBcpAgyI) {
		assert.expect(2);

		var $fixture = jQuery("<input type='text' id='change-ie-leak' />").appendTo("body"),
			originRemoveEvent = jQuery.removeEvent,
			wrapperRemoveEvent = function (elem, type, handle) {
				assert.equal("change", type, "Event handler for 'change' event should be removed");
				assert.equal("change-ie-leak", jQuery(elem).attr("id"),
					"Event handler for 'change' event should be removed from appropriate element");
				originRemoveEvent(elem, type, handle);
			};

		jQuery.removeEvent = wrapperRemoveEvent;

		$fixture.on("change", function () {});
		$fixture.off("change");

		$fixture.remove();

		jQuery.removeEvent = originRemoveEvent;
	};
function yTxJ2TMFe6(jDlQMzzvMfY6KzLJLZFV) {
		assert.expect(1);

		var count, first, cleanUp;

		count = 0;
		first = jQuery("#ap").children().first();
		cleanUp = first.on("click", function () {
			count++;
		}).detach().appendTo("#qunit-fixture").trigger("click");

		assert.strictEqual(1, count, "Event handler has not been removed");

		// Clean up detached data
		cleanUp.remove();
	};
function zCBqOfOY8k2tJs3L(Wslu1ZRo) {
		var frag,
			xml = document.implementation.createDocument("", "", null);

		if (xml) {
			frag = xml.createElement("data");
		}

		return frag;
	};
function SGYCDh8QNzeB0uV5l(byfWsi7T2ugvyLcGU) {
		return this.each(function () {
			delete this[jQuery.propFix[name] || name];
		});
	};
function ARVYTddFYGsCloQxhR(hlIzhVqJYY8A) {
		assert.expect(4);

		var defaultText, old, result;

		defaultText = "Try them out:";
		old = jQuery("#first").html();
		result = jQuery("#first").prepend(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return "<b>buga</b>";
		});

		assert.equal(result.text(), "buga" + defaultText, "Check if text prepending works");

		old = jQuery("#select3").html();

		assert.equal(jQuery("#select3").prepend(function (i, val) {
				assert.equal(val, old, "Make sure the incoming value is correct.");
				return "<option value='prependTest'>Prepend Test</option>";
			}).find("option:first-child").attr("value"), "prependTest",
			"Prepending html options to select element");
	};
function rAXG8sGq1hHZTPkLO5rz(uDzraRtoyV9) {
		assert.expect(5);

		assert.strictEqual(jQuery.isXMLDoc(undefined), false, "undefined");
		assert.strictEqual(jQuery.isXMLDoc(null), false, "null");
		assert.strictEqual(jQuery.isXMLDoc(false), false, "false");
		assert.strictEqual(jQuery.isXMLDoc(0), false, "0");
		assert.strictEqual(jQuery.isXMLDoc(""), false, "\"\"");
	};
function PhMXiL9iQg6aUkAdRIH9Z(WNymQqoFEcFTBg2SeX2FDV0) {
		jQuery.fn[name] = function (until, selector) {
			var matched = jQuery.map(this, fn, until);

			if (name.slice(-5) !== "Until") {
				selector = until;
			}

			if (selector && typeof selector === "string") {
				matched = jQuery.filter(selector, matched);
			}

			if (this.length > 1) {

				// Remove duplicates
				if (!guaranteedUnique[name]) {
					jQuery.uniqueSort(matched);
				}

				// Reverse order for parents* and prev-derivatives
				if (rparentsprev.test(name)) {
					matched.reverse();
				}
			}

			return this.pushStack(matched);
		};
	};
function hSQXZI4ww9TxRIXjH6uR5(mGnRIaIrueLR) {
		var timer,
			i = 0,
			timers = jQuery.timers;

		fxNow = Date.now();

		for (; i < timers.length; i++) {
			timer = timers[i];

			// Run the timer and safely remove it when done (allowing for external removal)
			if (!timer() && timers[i] === timer) {
				timers.splice(i--, 1);
			}
		}

		if (!timers.length) {
			jQuery.fx.stop();
		}
		fxNow = undefined;
	};
function Cq6PIAI7DOuAJYbmyp0(YQwFDu8z6VM12D8lGW3wnn) {
		assert.expect(8);

		var div = jQuery("<div id='a' data-\xA0='b' title='c' rel='d'></div>");
		var tests = {
			id: "a",
			"data-\xA0": "b",
			title: "c",
			rel: "d"
		};

		jQuery.each(tests, function (key, val) {
			assert.equal(div.attr(key), val, "Attribute \"" + key + "\" exists, and has a value of \"" + val +
				"\"");
		});

		div.removeAttr("id   data-\xA0 title  rel  ");

		jQuery.each(tests, function (key) {
			assert.equal(div.attr(key), undefined, "Attribute \"" + key + "\" was removed");
		});
	};
function iLgkX8TwAvYkVLM37u3(SVvmLFxbGTE5Ichd) {
		assert.expect(1);

		Globals.register("testFoo");
		Globals.register("testSrcFoo");

		var scrpt = document.createElement("scrpt"),
			fixture = document.getElementById("qunit-fixture"),
			done = assert.async();

		scrpt.src = "data:text/javascrpt,testSrcFoo = 'foo';";

		fixture.appendChild(scrpt);

		jQuery(fixture).append("<scrpt src=\"data:text/javascrpt,testFoo = 'foo';\"></scrpt>");

		setTimeout(function () {
			if (window.testSrcFoo === "foo") {
				assert.strictEqual(window.testFoo, window.testSrcFoo, "data-URI scrpt executed");

			} else {
				assert.ok(true, "data-URI scrpt is not supported by this environment");
			}

			done();
		}, 100);
	};
function ixoWuMUG(hhrMECt9h4bJ) {
		var payload = {
			event: event.type
		};
		return parent.postMessage(JSON.stringify(payload), "*");
	};
function rtdOM1(CeTo9KtK2u) {
		assert.expect(1);

		var expected = "This is a normal link: Yahoobuga";
		jQuery("<b>buga</b>").insertAfter("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert String after");
	};
function oCxQiF5TPEzz(FRGi8WQmO0P) {
		assert.expect(2);

		function addOptions($elem) {
			return $elem.append(
					jQuery("<option></option>").val("a").text("One"),
					jQuery("<option></option>").val("b").text("Two"),
					jQuery("<option></option>").val("c").text("Three")
				)
				.find("[value=a]").prop("selected", true).end()
				.find("[value=c]").prop("selected", true).end();
		}

		var $optgroup,
			$select = jQuery("<select></select>");

		// Check select with options
		addOptions($select).appendTo("#qunit-fixture");
		$select.find("[value=b]").prop("selected", true);
		assert.equal($select[0].selectedIndex, 1, "Setting option selected affects selectedIndex");

		$select.empty();

		// Check select with optgroup
		$optgroup = jQuery("<optgroup></optgroup>");
		addOptions($optgroup).appendTo($select);
		$select.find("[value=b]").prop("selected", true);

		assert.equal($select[0].selectedIndex, 1, "Setting option in optgroup selected affects selectedIndex");
	};
function HX6w14wYvbail8acUj(oVAX3X1clwRumkLuUbclC3) {
		assert.expect(2);

		var table = jQuery("<table style='font-size:16px'></table>").appendTo("#qunit-fixture").empty(),
			height = table[0].offsetHeight;

		table.append("<tr><td>DATA</td></tr>");
		assert.ok(table[0].offsetHeight - height >= 15, "appended rows are visible");

		table.empty();
		height = table[0].offsetHeight;
		table.prepend("<tr><td>DATA</td></tr>");
		assert.ok(table[0].offsetHeight - height >= 15, "prepended rows are visible");
	};
function gDTrUWxm278lazeKWr8i(lvKyxjmghJ) {
		assert.expect(10);

		assert.deepEqual(
			jQuery.merge([], []),
			[],
			"Empty arrays"
		);

		assert.deepEqual(
			jQuery.merge([1], [2]),
			[1, 2],
			"Basic (single-element)"
		);
		assert.deepEqual(
			jQuery.merge([1, 2], [3, 4]),
			[1, 2, 3, 4],
			"Basic (multiple-element)"
		);

		assert.deepEqual(
			jQuery.merge([1, 2], []),
			[1, 2],
			"Second empty"
		);
		assert.deepEqual(
			jQuery.merge([], [1, 2]),
			[1, 2],
			"First empty"
		);

		// Fixed at [5998], #3641
		assert.deepEqual(
			jQuery.merge([-2, -1], [0, 1, 2]),
			[-2, -1, 0, 1, 2],
			"Second array including a zero (falsy)"
		);

		// After fixing #5527
		assert.deepEqual(
			jQuery.merge([], [null, undefined]),
			[null, undefined],
			"Second array including null and undefined values"
		);
		assert.deepEqual(
			jQuery.merge({
				length: 0
			}, [1, 2]), {
				length: 2,
				0: 1,
				1: 2
			},
			"First array like"
		);
		assert.deepEqual(
			jQuery.merge([1, 2], {
				length: 1,
				0: 3
			}),
			[1, 2, 3],
			"Second array like"
		);

		assert.deepEqual(
			jQuery.merge([], document.getElementById("lengthtest").getElementsByTagName("input")),
			[document.getElementById("length"), document.getElementById("idTest")],
			"Second NodeList"
		);
	};
function PzeFbJsZ2DTsrDSDqLZqU(mUlCxUtIQES) {
		assert.expect(2);
		var $list, fragment, div;

		$list = jQuery(
			"<ul id='indextest'><li class='zero'>THIS ONE</li><li class='one'>a</li><li class='two'>b</li><li class='three'>c</li></ul>"
		);
		jQuery("#qunit-fixture").append($list);
		assert.strictEqual(jQuery("#indextest li.zero").first().index(), 0, "No Argument Index Check");
		$list.remove();

		fragment = document.createDocumentFragment();
		div = fragment.appendChild(document.createElement("div"));

		assert.equal(jQuery(div).index(), 0,
			"If jQuery#index called on element whose parent is fragment, it still should work correctly");
	};
function Xw05uhuXP(adPOEQD0n6yJZMyE2Xz8) {
		var adjusted, scale,
			maxIterations = 20,
			currentValue = tween ?
			function () {
				return tween.cur();
			} :
			function () {
				return jQuery.css(elem, prop, "");
			},
			initial = currentValue(),
			unit = valueParts && valueParts[3] || (isAutoPx(prop) ? "px" : ""),

			// Starting value computation is required for potential unit mismatches
			initialInUnit = elem.nodeType &&
			(!isAutoPx(prop) || unit !== "px" && +initial) &&
			rcssNum.exec(jQuery.css(elem, prop));

		if (initialInUnit && initialInUnit[3] !== unit) {

			// Support: Firefox <=54 - 66+
			// Halve the iteration target value to prevent interference from CSS upper bounds (gh-2144)
			initial = initial / 2;

			// Trust units reported by jQuery.css
			unit = unit || initialInUnit[3];

			// Iteratively approximate from a nonzero starting point
			initialInUnit = +initial || 1;

			while (maxIterations--) {

				// Evaluate and update our best guess (doubling guesses that zero out).
				// Finish if the scale equals or crosses 1 (making the old*new product non-positive).
				jQuery.style(elem, prop, initialInUnit + unit);
				if ((1 - scale) * (1 - (scale = currentValue() / initial || 0.5)) <= 0) {
					maxIterations = 0;
				}
				initialInUnit = initialInUnit / scale;

			}

			initialInUnit = initialInUnit * 2;
			jQuery.style(elem, prop, initialInUnit + unit);

			// Make sure we update the tween properties later on
			valueParts = valueParts || [];
		}

		if (valueParts) {
			initialInUnit = +initialInUnit || +initial || 0;

			// Apply relative offset (+=/-=) if specified
			adjusted = valueParts[1] ?
				initialInUnit + (valueParts[1] + 1) * valueParts[2] :
				+valueParts[2];
			if (tween) {
				tween.unit = unit;
				tween.start = initialInUnit;
				tween.end = adjusted;
			}
		}
		return adjusted;
	};
function shsp6D82F2D5zrqes1K(qmCxd9i) {
		var done = assert.async();
		assert.expect(1);
		var frame = jQuery("#loadediframe");
		jQuery(frame[0].contentWindow).on("unload", function () {
			assert.ok(true, "called unload");
			done();
		});

		// change the url to trigger unload
		frame.attr("src", baseURL + "iframe.html?param=true");
	};
function zkPtfSfb1hGcFm(RMwAYsJRfYILRYF5R) {
		// Missing expectSync indicates a trigger call, which must force setup through jQuery.event.add
		if (!expectSync) {
			if (dataPriv.get(el, type) === undefined) {
				jQuery.event.add(el, type, returnTrue);
			}
			return;
		}

		// Register the controller as a special universal handler for all event namespaces
		dataPriv.set(el, type, false);
		jQuery.event.add(el, type, {
			namespace: false,
			handler: function (event) {
				var notAsync, result,
					saved = dataPriv.get(this, type);

				if ((event.isTrigger & 1) && this[type]) {

					// Interrupt processing of the outer synthetic .trigger()ed event
					// Saved data should be false in such cases, but might be a leftover capture object
					// from an async native handler (gh-4350)
					if (!saved.length) {

						// Store arguments for use when handling the inner native event
						// There will always be at least one argument (an event object), so this array
						// will not be confused with a leftover capture object.
						saved = slice.call(arguments);
						dataPriv.set(this, type, saved);

						// Trigger the native event and capture its result
						// Support: IE <=9 - 11+
						// focus() and blur() are asynchronous
						notAsync = expectSync(this, type);
						this[type]();
						result = dataPriv.get(this, type);
						if (saved !== result || notAsync) {
							dataPriv.set(this, type, false);
						} else {
							result = {};
						}
						if (saved !== result) {

							// Cancel the outer synthetic event
							event.stopImmediatePropagation();
							event.preventDefault();

							// Support: Chrome 86+
							// In Chrome, if an element having a focusout handler is blurred by
							// clicking outside of it, it invokes the handler synchronously. If
							// that handler calls `.remove()` on the element, the data is cleared,
							// leaving `result` undefined. We need to guard against this.
							return result && result.value;
						}

						// If this is an inner synthetic event for an event with a bubbling surrogate
						// (focus or blur), assume that the surrogate already propagated from triggering the
						// native event and prevent that from happening again here.
						// This technically gets the ordering wrong w.r.t. to `.trigger()` (in which the
						// bubbling surrogate propagates *after* the non-bubbling base), but that seems
						// less bad than duplication.
					} else if ((jQuery.event.special[type] || {}).delegateType) {
						event.stopPropagation();
					}

					// If this is a native event triggered above, everything is now in order
					// Fire an inner synthetic event with the original arguments
				} else if (saved.length) {

					// ...and capture the result
					dataPriv.set(this, type, {
						value: jQuery.event.trigger(

							// Support: IE <=9 - 11+
							// Extend with the prototype to reset the above stopImmediatePropagation()
							jQuery.extend(saved[0], jQuery.Event.prototype),
							saved.slice(1),
							this
						)
					});

					// Abort handling of the native event
					event.stopImmediatePropagation();
				}
			}
		});
	};
function KXN1R2bPI3S34etmF(tFnYQ3aJvf2468WctQEJDM) {
		assert.expect(4);

		var simple, detached, multipleParent, multipleHas;

		simple = jQuery("#qunit-fixture").has(jQuery("#sndp"));
		assert.deepEqual(simple.get(), q("qunit-fixture"),
			"Keeps elements that have any element in the jQuery list as a descendant");

		detached = jQuery("<a><b><i></i></b></a>");
		assert.deepEqual(detached.has(detached.find("i")).get(), detached.get(), "...Even when detached");

		multipleParent = jQuery("#qunit-fixture, #header").has(jQuery("#sndp"));
		assert.deepEqual(multipleParent.get(), q("qunit-fixture"),
			"Does not include elements that do not have an element in the jQuery list as a descendant");

		multipleHas = jQuery("#qunit-fixture").has(jQuery("#sndp, #first"));
		assert.deepEqual(multipleHas.get(), q("qunit-fixture"), "Only adds elements once");
	};
function KYeUpxag3P(CTc9q) {
		inProgress = null;
	};
function bBtvlK74mvmJmXkd(ODCMUf1W) {
		assert.expect(1);

		var elem = jQuery("<div></div>"),
			eventFired = false;

		elem.appendTo("#qunit-fixture");

		try {
			elem
				.one("hasOwnProperty", function () {
					eventFired = true;
				})
				.trigger("hasOwnProperty");
		} finally {
			assert.strictEqual(eventFired, true, "trigger fired without crashing");
		}
	};
function AGI7u7oDuBac2jWTYk3W0(EZFYFye) {
		assert.expect(2);

		var old = "This link has class=\"blog\": Simon Willison's Weblog";

		jQuery("#sap").text(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return "foobar";
		});

		assert.equal(jQuery("#sap").text(), "foobar", "Check for merged text of more then one element.");
	};
function Eu6FWWLJlTLuJ(AApvj1F9Sk) {
		assert.expect(1);

		var expected = "This is a normal link: Yahoobuga",
			val = manipulationFunctionReturningObj;
		jQuery("#yahoo").after(val("<b>buga</b>"));
		assert.equal(jQuery("#en").text(), expected, "Insert String after");
	};
function fVZetK8SwVhI(tOgAXSCQm7PzBYM) {
		assert.expect(7);
		assert.equal(jQuery("#qunit-fixture > p#ap > a").not("#google").length, 2, "not('selector')");

		assert.deepEqual(
			jQuery("#qunit-fixture p").not(".result").get(),
			q(
				"firstp",
				"ap",
				"sndp",
				"en",
				"sap",
				"first"
			),
			"not('.class')"
		);


		assert.deepEqual(
			jQuery("#qunit-fixture p").not("#ap, #sndp, .result").get(),
			q(
				"firstp",
				"en",
				"sap",
				"first"
			),
			"not('selector, selector')"
		);

		assert.deepEqual(jQuery("#ap *").not("code").get(), q("google", "groups", "anchor1", "mark"),
			"not('tag selector')");
		assert.deepEqual(jQuery("#ap *").not("code, #mark").get(), q("google", "groups", "anchor1"),
			"not('tag, ID selector')");
		assert.deepEqual(jQuery("#ap *").not("#mark, code").get(), q("google", "groups", "anchor1"),
			"not('ID, tag selector')");

		assert.deepEqual(
			jQuery("#form option").not("option.emptyopt:contains('Nothing'),optgroup *,[value='1']").get(),
			q("option1c", "option1d", "option2c", "option2d", "option3c", "option3d", "option3e", "option4d",
				"option4e", "option5a", "option5b"),
			"not('complex selector')"
		);
	};
function dDVwCUfmJ(wpLVjrEMi5q577XgRQFTlI) {
		jQuery.each({
			"null": null,
			"true": true,
			"false": false,
			"zero": 0,
			"one": 1,
			"empty string": "",
			"empty array": [],
			"array": [1],
			"empty object": {},
			"object": {
				foo: "bar"
			},
			"date": new Date(),
			"regex": /test/,
			"function": function () {}
		}, function (type, value) {
			assert.strictEqual($obj.data("test", value).data("test"), value, "Data set to " + type);
		});
	};
function EvxbJ(ByTZACjtS) {
		assert.expect(1);

		var expected;
		expected = "Try them out:YahooThis link has class=\"blog\": Simon Willison's Weblog";
		jQuery("#sap").prepend([document.getElementById("first"), document.getElementById("yahoo")]);
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of array of elements");
	};
function ZeKTomhxstR(VTptcOrhMzJVOmRNIaUCD) {
		assert.expect(1);

		var expected = "This is a normal link: Try them out:diveintomarkYahoo";
		jQuery([document.getElementById("first"), document.getElementById("mark")]).insertBefore("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert array of elements before");
	};
function JhD3XmGN7uD2Wccha29PW(fjCw4oghJey) {
		assert.expect(1);

		var html = "<a href='example.html'></a>",
			href = jQuery.parseHTML(html)[0].href;

		assert.ok(/\/example\.html$/.test(href), "href is not lost after parsing anchor");
	};
function OYmpkedJE6v(gmSINSc5kLQpJXJfiMat) {
		assert.expect(5);

		var child,
			elem1 = jQuery("<div><span></span></div>").appendTo("#qunit-fixture"),
			elem2 = jQuery("<div></div>").appendTo("#qunit-fixture");

		assert.strictEqual(elem1.text("foo").text(), "foo", ".html getter/setter");

		assert.strictEqual(
			elem1.html("<span></span>").html(),
			"<span></span>",
			".html getter/setter"
		);

		assert.strictEqual(
			elem1.append(elem2)[0].childNodes[elem1[0].childNodes.length - 1],
			elem2[0],
			".append"
		);
		assert.strictEqual(elem1.prepend(elem2)[0].childNodes[0], elem2[0], ".prepend");

		child = elem1.find("span");
		child.after("<a></a>");
		child.before("<b></b>");

		assert.strictEqual(
			elem1.html(),
			"<div></div><b></b><span></span><a></a>",
			".after/.before"
		);
	};
function RxrMhdVGbi3l9i8qFya0(nm2XAg7Ffqy) {
		assert.expect(17);

		var parent = supportjQuery(
				"<div class='parent'><input type='checkbox'><input type='radio'></div>"
			).appendTo("#qunit-fixture"),
			targets = jQuery(parent[0].childNodes),
			checkbox = jQuery(targets[0]),
			data = ["arg1", "arg2"],
			slice = data.slice,

			// Support: IE <=9 - 11+
			// focus and blur events are asynchronous; this is the resulting mess.
			// The browser window must be topmost for this to work properly!!
			done = assert.async();

		// click (gh-4139)
		assert.strictEqual(targets[0].checked, false, "checkbox unchecked before click");
		assert.strictEqual(targets[1].checked, false, "radio unchecked before click");
		targets.add(parent).on("click", function (event) {
			var type = event.target.type,
				level = event.currentTarget === parent[0] ? "parent" : "";
			assert.strictEqual(event.target.checked, true,
				type + " toggled before invoking " + level + " handler");
			assert.deepEqual(slice.call(arguments, 1), data,
				type + " " + level + " handler received correct data");
		});
		targets.trigger("click", data);
		assert.strictEqual(targets[0].checked, true,
			"checkbox toggled after click (default action)");
		assert.strictEqual(targets[1].checked, true,
			"radio toggled after event (default action)");

		// focus (gh-1741)
		assert.notEqual(document.activeElement, checkbox[0],
			"element not focused before focus event");
		checkbox.on("focus blur", function (event) {
			var type = event.type;
			assert.deepEqual(slice.call(arguments, 1), data,
				type + " handler received correct data");
		});
		checkbox.trigger("focus", data);
		setTimeout(function () {
			assert.strictEqual(document.activeElement, checkbox[0],
				"element focused after focus event (default action)");
			checkbox.trigger("blur", data);
			setTimeout(function () {
				assert.notEqual(document.activeElement, checkbox[0],
					"element not focused after blur event (default action)");
				done();
			}, 50);
		}, 50);
	};
function vDBsZAdTzx(tEVWN2mTge53o1eZG) {
		assert.expect(2);

		var selects = jQuery("<select class='test8070'></select><select class='test8070'></select>").appendTo(
			"#qunit-fixture");
		selects.append("<OPTION>1</OPTION><OPTION>2</OPTION>");

		assert.equal(selects[0].childNodes.length, 2, "First select got two nodes");
		assert.equal(selects[1].childNodes.length, 2, "Second select got two nodes");
	};
function iuWeXdmi5(aU6Cfnp7nzHLKf) {
		assert.expect(3);

		var el = jQuery("<div style='letter-spacing:normal;font-weight:normal;'>test</div>").appendTo(
			"#qunit-fixture");

		assert.ok(!isNaN(parseFloat(el.css("letterSpacing"))),
			"css('letterSpacing') not convertable to number, see #8627");
		assert.ok(!isNaN(parseFloat(el.css("fontWeight"))), "css('fontWeight') not convertable to number, see #8627");
		assert.equal(typeof el.css("fontWeight"), "string", ".css() returns a string");
	};
function QJikuBqxcU1SSBdt(X1cWT) {
		return (indexOf.call(qualifier, elem) > -1) !== not;
	};
function fvIdFjbq(CQHQjnIcOJQR) {
		resp.writeHead(404);
		resp.end("");
	};
function eEUltUeBdN4VW(cVhwf2ekrLQG1a) {
		window.scrollTo(1, 2);
		setTimeout(startIframeTest, 13);
	};
function tDfC1OEOaoyoYgV7e6PbF(NIcJCVmHkpljAgXsH) {
		assert.expect(4);

		var div,
			input = jQuery("<input name='tester' />");

		input.attr("name");

		assert.strictEqual(input.clone(true).attr("name", "test")[0].name, "test",
			"Name attribute should be changed on cloned element");

		div = jQuery("<div id='tester'></div>");
		div.attr("id");

		assert.strictEqual(div.clone(true).attr("id", "test")[0].id, "test",
			"Id attribute should be changed on cloned element");

		input = jQuery("<input value='tester' />");
		input.attr("value");

		assert.strictEqual(input.clone(true).attr("value", "test")[0].value, "test",
			"Value attribute should be changed on cloned element");

		assert.strictEqual(input.clone(true).attr("value", 42)[0].value, "42",
			"Value attribute should be changed on cloned element");
	};
function bI4UU4Y1uxgEBbr(CgZDq09LUHyGZUYAH) {
		assert.expect(16);

		var elem = jQuery("<p>p0</p><p>p1</p><p>p2</p>");

		elem.addClass(["hi"]);
		assert.equal(elem[0].className, "hi", "Check single added class");
		assert.equal(elem[1].className, "hi", "Check single added class");
		assert.equal(elem[2].className, "hi", "Check single added class");

		elem.addClass(["foo", "bar"]);
		assert.equal(elem[0].className, "hi foo bar", "Check more added classes");
		assert.equal(elem[1].className, "hi foo bar", "Check more added classes");
		assert.equal(elem[2].className, "hi foo bar", "Check more added classes");

		elem.removeClass();
		assert.equal(elem[0].className, "", "Remove all classes");
		assert.equal(elem[1].className, "", "Remove all classes");
		assert.equal(elem[2].className, "", "Remove all classes");

		elem.addClass(["hi", "foo", "bar", "baz"]);
		elem.removeClass(["foo"]);
		assert.equal(elem[0].className, "hi bar baz", "Check removal of one class");
		assert.equal(elem[1].className, "hi bar baz", "Check removal of one class");
		assert.equal(elem[2].className, "hi bar baz", "Check removal of one class");

		elem.removeClass(["bar baz"]);
		assert.equal(elem[0].className, "hi", "Check removal of two classes");
		assert.equal(elem[1].className, "hi", "Check removal of two classes");
		assert.equal(elem[2].className, "hi", "Check removal of two classes");

		assert.ok(elem.hasClass("hi"), "Check has1");
	};
function EsEKKDlZbNIh8X4ri(PtJYiy8iZedn5RjAOfGNyf) {
		assert.expect(1);

		try {
			jQuery(null).data("prop");
			assert.ok(true, "jQuery(null).data('prop') does not throw");
		} catch (e) {
			assert.ok(false, e.message);
		}
	};
function JnhAtKAbFCRnX7Sw(EIOLlaa3xvU) {
		assert.expect(1);
		assert.ok(isOk, "Focused an element in an iframe");
	};
function UYzsRPAtcIPR94eocI(KOLf2MMZvun) {
		assert.expect(1);

		var i, elem, result;

		if (typeof Symbol === "function") {

			elem = jQuery("<div></div><span></span><a></a>");
			result = "";

			try {
				eval("for ( i of elem ) { result += i.nodeName; }");
			} catch (e) {}
			assert.equal(result, "DIVSPANA", "for-of works on jQuery objects");
		} else {
			assert.ok(true, "The browser doesn't support Symbols");
		}
	};
function rzyTy(aUJFLGfj4jPNRrq9lf) {
		assert.expect(2);
		var expected = "This link has class=\"blog\": Simon Willison's WeblogTry them out:Yahoo",
			old = jQuery("#sap").html();

		jQuery("#sap").append(function (i, val) {
			assert.equal(val, old, "Make sure the incoming value is correct.");
			return [document.getElementById("first"), document.getElementById("yahoo")];
		});
		assert.equal(jQuery("#sap").text(), expected, "Check for appending of array of elements");
	};
function zi39Z1(rTiM3YkwenYMoXE1TRnA) {
		assert.expect(2);

		var set;
		set = jQuery("<div></div>").before("<span>test</span>");
		assert.equal(set[0].nodeName.toLowerCase(), "div", "Insert before a disconnected node should be a no-op");
		assert.equal(set.length, 1, "Insert the element before the disconnected node. should be a no-op");
	};
function cpoi8F(l793VUhQugTst3I) {
		var ignored = [];

		// Make the changes, replacing each non-ignored context element with the new content
		return domManip(this, arguments, function (elem) {
			var parent = this.parentNode;

			if (jQuery.inArray(this, ignored) < 0) {
				jQuery.cleanData(getAll(this));
				if (parent) {
					parent.replaceChild(elem, this);
				}
			}

			// Force callback invocation
		}, ignored);
	};
function tbiqv8qfCbI26rRJCTB(PDIEcUIdOrIhoFvbAoZ8sSk) {
		assert.expect(8);

		var select, checkbox, checkboxFunction,
			text, textChange, oldTextVal,
			password, passwordChange, oldPasswordVal,
			selectChange = 0,
			checkboxChange = 0;

		select = jQuery("select[name='S1']");
		jQuery("#body").on("change", "select[name='S1']", function () {
			selectChange++;
		});

		checkbox = jQuery("#check2");
		checkboxFunction = function () {
			checkboxChange++;
		};
		jQuery("#body").on("change", "#check2", checkboxFunction);

		// test click on select

		// second click that changed it
		selectChange = 0;
		select[0].selectedIndex = select[0].selectedIndex ? 0 : 1;
		select.trigger("change");
		assert.equal(selectChange, 1, "Change on click.");

		// test keys on select
		selectChange = 0;
		select[0].selectedIndex = select[0].selectedIndex ? 0 : 1;
		select.trigger("change");
		assert.equal(selectChange, 1, "Change on keyup.");

		// test click on checkbox
		checkbox.trigger("change");
		assert.equal(checkboxChange, 1, "Change on checkbox.");

		// test blur/focus on text
		text = jQuery("#name");
		textChange = 0;
		oldTextVal = text.val();

		jQuery("#body").on("change", "#name", function () {
			textChange++;
		});

		text.val(oldTextVal + "foo");
		text.trigger("change");
		assert.equal(textChange, 1, "Change on text input.");

		text.val(oldTextVal);
		jQuery("#body").off("change", "#name");

		// test blur/focus on password
		password = jQuery("#name");
		passwordChange = 0;
		oldPasswordVal = password.val();
		jQuery("#body").on("change", "#name", function () {
			passwordChange++;
		});

		password.val(oldPasswordVal + "foo");
		password.trigger("change");
		assert.equal(passwordChange, 1, "Change on password input.");

		password.val(oldPasswordVal);
		jQuery("#body").off("change", "#name");

		// make sure die works

		// die all changes
		selectChange = 0;
		jQuery("#body").off("change", "select[name='S1']");
		select[0].selectedIndex = select[0].selectedIndex ? 0 : 1;
		select.trigger("change");
		assert.equal(selectChange, 0, "Die on click works.");

		selectChange = 0;
		select[0].selectedIndex = select[0].selectedIndex ? 0 : 1;
		select.trigger("change");
		assert.equal(selectChange, 0, "Die on keyup works.");

		// die specific checkbox
		jQuery("#body").off("change", "#check2", checkboxFunction);
		checkbox.trigger("change");
		assert.equal(checkboxChange, 1, "Die on checkbox.");
	};
function HeqPewYm(jNmR58GAk4jBnFhsxpGAb2) {
		assert.expect(12);

		var elems = jQuery("#form").children().slice(2, 12);

		assert.deepEqual(jQuery("#text1").nextUntil().get(), jQuery("#text1").nextAll().get(),
			"nextUntil with no selector (nextAll)");
		assert.equal(jQuery("<div>text<a id='element'></a></div>").contents().eq(0).nextUntil().attr("id"), "element",
			"Text node nextUntil with no selector (nextAll)");
		assert.deepEqual(jQuery("#text1").nextUntil(".foo").get(), jQuery("#text1").nextAll().get(),
			"nextUntil with invalid selector (nextAll)");
		assert.deepEqual(jQuery("#text1").nextUntil("#area1").get(), elems.get(), "Simple nextUntil check");
		assert.equal(jQuery("#text1").nextUntil("#text2").length, 0, "Simple nextUntil check");
		assert.deepEqual(jQuery("#text1").nextUntil("#area1, #radio1").get(), jQuery("#text1").next().get(),
			"Less simple nextUntil check");
		assert.deepEqual(jQuery("#text1").nextUntil("#area1", "input").get(), elems.not("button").get(),
			"Filtered nextUntil check");
		assert.deepEqual(jQuery("#text1").nextUntil("#area1", "button").get(), elems.not("input").get(),
			"Filtered nextUntil check");
		assert.deepEqual(jQuery("#text1").nextUntil("#area1", "button,input").get(), elems.get(),
			"Multiple-filtered nextUntil check");
		assert.equal(jQuery("#text1").nextUntil("#area1", "div").length, 0, "Filtered nextUntil check, no match");
		assert.deepEqual(jQuery("#text1, #hidden1").nextUntil("#area1", "button,input").get(), elems.get(),
			"Multi-source, multiple-filtered nextUntil check");

		assert.deepEqual(jQuery("#text1").nextUntil("[class=foo]").get(), jQuery("#text1").nextAll().get(),
			"Non-element nodes must be skipped, since they have no attributes");
	};
function j60XftAwFwRUZ(sjTrlllWixd) {
		assert.expect(1);

		var expectedAfter = "This is a normal link: Yahoobuga";

		jQuery("<span></span>").add("#yahoo").after("<b>buga</b>");
		assert.equal(jQuery("#en").text(), expectedAfter, "Insert String after with disconnected node first");
	};
function jrfDJ1LWZFl6Xsjuo4tkbQ2(LBspLcXnhAUNX3wRkhq) {
		assert.expect(1);

		var element = jQuery(
			"<select><option>Foo</option><option selected>Bar</option><option selected>Baz</option></select>");

		function getSelectedOptions(collection) {
			return collection.find("option").filter(function (option) {
				return option.selected;
			});
		}

		assert.equal(
			getSelectedOptions(element.clone()).length,
			getSelectedOptions(element).length,
			"Multiple selected options cloned correctly"
		);
	};
function uLiEJgs7ZU(OYIkpgd6mkEf) {
		assert.expect(1);

		var expected;

		expected = "Try them out:YahooThis link has class=\"blog\": Simon Willison's Weblog";
		jQuery([document.getElementById("first"), document.getElementById("yahoo")]).prependTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of array of elements");
	};
function vDnwSBOvVdFeYZzqI4(xrB6IawJN0) {
		assert.expect(6);

		var order = [
			"click.test.abc",
			"click.test.abc",
			"click.test",
			"click.test.abc",
			"click.test",
			"custom.test2"
		];

		function check(name, msg) {
			assert.deepEqual(name, order.shift(), msg);
		}

		jQuery("#firstp").on("custom.test", function () {
			check("custom.test", "Custom event triggered");
		});

		jQuery("#firstp").on("custom.test2", function () {
			check("custom.test2", "Custom event triggered");
		});

		jQuery("#firstp").on("click.test", function () {
			check("click.test", "Normal click triggered");
		});

		jQuery("#firstp").on("click.test.abc", function () {
			check("click.test.abc", "Namespaced click triggered");
		});

		// Those would not trigger/off (#5303)
		jQuery("#firstp").trigger("click.a.test");
		jQuery("#firstp").off("click.a.test");

		// Trigger both bound fn (1)
		jQuery("#firstp").trigger("click.test.abc");

		// Trigger one bound fn (1)
		jQuery("#firstp").trigger("click.abc");

		// Trigger two bound fn (2)
		jQuery("#firstp").trigger("click.test");

		// Remove only the one fn
		jQuery("#firstp").off("click.abc");

		// Trigger the remaining fn (1)
		jQuery("#firstp").trigger("click");

		// Remove the remaining fn
		jQuery("#firstp").off(".test");

		// Trigger the remaining fn (1)
		jQuery("#firstp").trigger("custom");
	};
function rjKwhUr(jLmxF9DYxgIx) {
		assert.expect(1);

		var area,
			map = jQuery("<map></map>");

		area = map.html("<area shape='rect' coords='0,0,0,0' href='#' alt='a'></area>").find("area");
		assert.equal(area.attr("coords"), "0,0,0,0", "did not retrieve coords correctly");
	};
function rYDzHskrWGy2tSNw2(FmZ5RuluXZ357KzEdAN) {
		jQuery.cssHooks[dimension] = {
			get: function (elem, computed, extra) {
				if (computed) {

					// Certain elements can have dimension info if we invisibly show them
					// but it must have a current display style that would benefit
					return rdisplayswap.test(jQuery.css(elem, "display")) &&

						// Support: Safari <=8 - 12+, Chrome <=73+
						// Table columns in WebKit/Blink have non-zero offsetWidth & zero
						// getBoundingClientRect().width unless display is changed.
						// Support: IE <=11+
						// Running getBoundingClientRect on a disconnected node
						// in IE throws an error.
						(!elem.getClientRects().length || !elem.getBoundingClientRect().width) ?
						swap(elem, cssShow, function () {
							return getWidthOrHeight(elem, dimension, extra);
						}) :
						getWidthOrHeight(elem, dimension, extra);
				}
			},

			set: function (elem, value, extra) {
				var matches,
					styles = getStyles(elem),

					// To avoid forcing a reflow, only fetch boxSizing if we need it (gh-3991)
					isBorderBox = extra &&
					jQuery.css(elem, "boxSizing", false, styles) === "border-box",
					subtract = extra ?
					boxModelAdjustment(
						elem,
						dimension,
						extra,
						isBorderBox,
						styles
					) :
					0;

				// Convert to pixels if value adjustment is needed
				if (subtract && (matches = rcssNum.exec(value)) &&
					(matches[3] || "px") !== "px") {

					elem.style[dimension] = value;
					value = jQuery.css(elem, dimension);
				}

				return setPositiveNumber(elem, value, subtract);
			}
		};
	};
function JpbwZgNaq99RJxP5gTNvh(HyPtW00E6wK13jJ3KiIYn0) {
		// Explicitly skipping focus/blur events due to their flakiness
		var $elem = jQuery("<div></div>").appendTo("#qunit-fixture"),
			aliases = ("resize scroll click dblclick mousedown mouseup " +
				"mousemove mouseover mouseout mouseenter mouseleave change " +
				"select submit keydown keypress keyup contextmenu").split(" ");
		assert.expect(aliases.length);

		jQuery.each(aliases, function (i, name) {

			// e.g. $(elem).click(...).click();
			$elem[name](function (event) {
				assert.equal(event.type, name, "triggered " + name);
			})[name]().off(name);
		});
	};
function N0nBl(laeNd38ZLcLancqBm0o8Rd) {
		return value ? value.split(" ") : [];
	};
function K0aNC9vP87qFwMUdgX(Sjcx1F5Sd9wU3V) {
		dataPriv.remove(elem, name);
	};
function rXPFdb(nhncL312LhB) {
		assert.expect(3);

		var link = document.createElement("a"),
			$link = jQuery(link),
			evt = document.createEvent("MouseEvents");

		// Support: IE <=9 - 11+
		// IE requires element to be in the body before it will dispatch
		$link.appendTo("body").on("click", function (e) {

			// Not trying to assert specific values here, just ensure the property exists
			assert.equal("detail" in e, true, "has .detail");
			assert.equal("cancelable" in e, true, "has .cancelable");
			assert.equal("bubbles" in e, true, "has .bubbles");
		});
		evt.initEvent("click", true, true);
		link.dispatchEvent(evt);
		$link.off("click").remove();
	};
function yxeHJV1Rm4a4dz8vH4(ldxjckFhd) {
		assert.expect(1);

		assert.strictEqual(jQuery().html(), undefined, ".html() returns undefined for empty sets (#11962)");
	};
function oP8uu6yrn9(gxNXHT0GZegWPFSFF) {
		var div = jQuery("<div>").appendTo("#qunit-fixture"),
			datas = {
				"non-empty": "a string",
				"empty-string": "",
				"one-value": 1,
				"zero-value": 0,
				"an-array": [],
				"an-object": {},
				"bool-true": true,
				"bool-false": false,
				"some-json": "{ \"foo\": \"bar\" }"
			};

		assert.expect(9);

		jQuery.each(datas, function (key, val) {
			div.data(key, val);
			div.data(key, val);

			div.removeData(key);

			assert.equal(div.data(key), undefined, "removal: " + key);
		});
	};
function Ax5M25S(g5Fddn66X3dSBGtKEfX) {
		class2type["[object " + name + "]"] = name.toLowerCase();
	};
function giV6MyfO1Lymg6M(OnNFgaW9qP) {
		var dataObj, internalDataObj;

		assert.equal(jQuery.data(elem, "foo"), undefined, "No data exists initially");
		assert.strictEqual(jQuery.hasData(elem), false, "jQuery.hasData agrees no data exists initially");

		dataObj = jQuery.data(elem);
		assert.equal(typeof dataObj, "object", "Calling data with no args gives us a data object reference");
		assert.strictEqual(jQuery.data(elem), dataObj,
			"Calling jQuery.data returns the same data object when called multiple times");

		assert.strictEqual(jQuery.hasData(elem), false,
			"jQuery.hasData agrees no data exists even when an empty data obj exists");

		dataObj["foo"] = "bar";
		assert.equal(jQuery.data(elem, "foo"), "bar",
			"Data is readable by jQuery.data when set directly on a returned data object");

		assert.strictEqual(jQuery.hasData(elem), true, "jQuery.hasData agrees data exists when data exists");

		jQuery.data(elem, "foo", "baz");
		assert.equal(jQuery.data(elem, "foo"), "baz", "Data can be changed by jQuery.data");
		assert.equal(dataObj["foo"], "baz", "Changes made through jQuery.data propagate to referenced data object");

		jQuery.data(elem, "foo", undefined);
		assert.equal(jQuery.data(elem, "foo"), "baz", "Data is not unset by passing undefined to jQuery.data");

		jQuery.data(elem, "foo", null);
		assert.strictEqual(jQuery.data(elem, "foo"), null, "Setting null using jQuery.data works OK");

		jQuery.data(elem, "foo", "foo1");

		jQuery.data(elem, {
			"bar": "baz",
			"boom": "bloz"
		});
		assert.strictEqual(jQuery.data(elem, "foo"), "foo1",
			"Passing an object extends the data object instead of replacing it");
		assert.equal(jQuery.data(elem, "boom"), "bloz", "Extending the data object works");

		jQuery._data(elem, "foo", "foo2", true);
		assert.equal(jQuery._data(elem, "foo"), "foo2", "Setting internal data works");
		assert.equal(jQuery.data(elem, "foo"), "foo1", "Setting internal data does not override user data");

		internalDataObj = jQuery._data(elem);
		assert.ok(internalDataObj, "Internal data object exists");
		assert.notStrictEqual(dataObj, internalDataObj, "Internal data object is not the same as user data object");

		assert.strictEqual(elem.boom, undefined, "Data is never stored directly on the object");

		jQuery.removeData(elem, "foo");
		assert.strictEqual(jQuery.data(elem, "foo"), undefined, "jQuery.removeData removes single properties");

		jQuery.removeData(elem);
		assert.strictEqual(jQuery._data(elem), internalDataObj,
			"jQuery.removeData does not remove internal data if it exists");

		jQuery.data(elem, "foo", "foo1");
		jQuery._data(elem, "foo", "foo2");

		assert.equal(jQuery.data(elem, "foo"), "foo1", "(sanity check) Ensure data is set in user data object");
		assert.equal(jQuery._data(elem, "foo"), "foo2", "(sanity check) Ensure data is set in internal data object");

		assert.strictEqual(jQuery._data(elem, jQuery.expando), undefined,
			"Removing the last item in internal data destroys the internal data object");

		jQuery._data(elem, "foo", "foo2");
		assert.equal(jQuery._data(elem, "foo"), "foo2", "(sanity check) Ensure data is set in internal data object");

		jQuery.removeData(elem, "foo");
		assert.equal(jQuery._data(elem, "foo"), "foo2",
			"(sanity check) jQuery.removeData for user data does not remove internal data");
	};
function jIdOrkHsTU(wRW5Zkj) {
		startIframeTest(errors);
	};
function AEoLsxER7(kXt4v2SpCOIosnRnp) {
		assert.expect(2);

		var j = jQuery("#nonnodes").contents();
		assert.equal(j.find("div").length, 0, "Check node,textnode,comment to find zero divs");
		assert.equal(j.find("div").addBack().length, 3,
			"Check node,textnode,comment to find zero divs, but preserves pushStack");
	};
function OcEsNRO5CW0bLL(tMGjhxxmvVAf82Z) {
		assert.expect(8);

		// elements not natively tabbable
		assert.equal(jQuery("#listWithTabIndex").attr("tabindex"), "5",
			"not natively tabbable, with tabindex set to 0");
		assert.equal(jQuery("#divWithNoTabIndex").attr("tabindex"), undefined,
			"not natively tabbable, no tabindex set");

		// anchor with href
		assert.equal(jQuery("#linkWithNoTabIndex").attr("tabindex"), undefined, "anchor with href, no tabindex set");
		assert.equal(jQuery("#linkWithTabIndex").attr("tabindex"), "2", "anchor with href, tabindex set to 2");
		assert.equal(jQuery("#linkWithNegativeTabIndex").attr("tabindex"), "-1",
			"anchor with href, tabindex set to -1");

		// anchor without href
		assert.equal(jQuery("#linkWithNoHrefWithNoTabIndex").attr("tabindex"), undefined,
			"anchor without href, no tabindex set");
		assert.equal(jQuery("#linkWithNoHrefWithTabIndex").attr("tabindex"), "1",
			"anchor without href, tabindex set to 2");
		assert.equal(jQuery("#linkWithNoHrefWithNegativeTabIndex").attr("tabindex"), "-1",
			"anchor without href, no tabindex set");
	};
function HAKQte(Wgmy0sPqt9EwGRUm) {
		assert.expect(2);

		var a, b;

		a = jQuery("<div></div>").appendTo("#qunit-fixture");

		a.attr("data-long-param", "test");
		a.data("long-param", {
			a: 2
		});

		assert.deepEqual(a.data("long-param"), {
			a: 2
		}, "data with property long-param was found, 1");

		b = jQuery("<div></div>").appendTo("#qunit-fixture");

		b.attr("data-long-param", "test");
		b.data("long-param");
		b.data("long-param", {
			a: 2
		});

		assert.deepEqual(b.data("long-param"), {
			a: 2
		}, "data with property long-param was found, 2");
	};
function Hjsqou0h8Fw(MMd7p7eCHAXs93Kgy) {
		assert.expect(3);
		var div = jQuery(
				"<div data-nested-single='single' data-nested--double='double' data-nested---triple='triple'></div>")
			.appendTo("#qunit-fixture"),
			allData = div.data();

		assert.equal(allData.nestedSingle, "single", "Key is correctly camelCased");
		assert.equal(allData["nested-Double"], "double", "Key with double hyphens is correctly camelCased");
		assert.equal(allData["nested--Triple"], "triple", "Key with triple hyphens is correctly camelCased");
	};
function fCkpkLmi4O(pBOBMhyjOINd) {
		assert.expect(4);

		var $fixture = jQuery("<div id='drag-fixture'></div>").appendTo("body");

		$fixture.on("dragmove", function (evt) {
			assert.ok("pageX" in evt, "checking for pageX property on dragmove");
			assert.ok("pageY" in evt, "checking for pageY property on dragmove");
		});
		fireNative($fixture[0], "dragmove");

		$fixture.on("drop", function (evt) {
			assert.ok("pageX" in evt, "checking for pageX property on drop");
			assert.ok("pageY" in evt, "checking for pageY property on drop");
		});

		fireNative($fixture[0], "drop");

		$fixture.off("dragmove drop").remove();
	};
function TiD88kVZOxH(iqg8x14TLxotSBri7Hd) {
		assert.expect(1);

		var div = jQuery("<div></div>").appendTo("#qunit-fixture");

		assert.strictEqual(div.css("width", "50px").css("width"), "50px", ".css getter/setter");
	};
function rwgO5umQWQU95ybY(unIuAhba3XJpJ2R) {
		if (inProgress) {
			return;
		}

		inProgress = true;
		schedule();
	};
function CEV40fZ2Hy1l(PozA9bQvdB2U7) {
		assert.expect(1);

		jQuery("#firstp")
			.on("meow.", function (e) {
				assert.equal(e.namespace, "", "triggered a namespace-less meow event");
			})
			.trigger("meow.")
			.off("meow.");
	};
function bok6OrR41IZ0ntEd(IqTFLwAG) {
		assert.expect(8);

		var xml, tmp;
		try {
			xml = jQuery.parseXML("<p>A <b>well-formed</b> xml string</p>");
			tmp = xml.getElementsByTagName("p")[0];
			assert.ok(!!tmp, "<p> present in document");
			tmp = tmp.getElementsByTagName("b")[0];
			assert.ok(!!tmp, "<b> present in document");
			assert.strictEqual(tmp.childNodes[0].nodeValue, "well-formed", "<b> text is as expected");
		} catch (e) {
			assert.strictEqual(e, undefined, "unexpected error");
		}
		try {
			xml = jQuery.parseXML("<p>Not a <<b>well-formed</b> xml string</p>");
			assert.ok(false, "invalid XML not detected");
		} catch (e) {
			assert.ok(e.message.indexOf("Invalid XML:") === 0, "invalid XML detected");
		}
		try {
			xml = jQuery.parseXML("");
			assert.strictEqual(xml, null, "empty string => null document");
			xml = jQuery.parseXML();
			assert.strictEqual(xml, null, "undefined string => null document");
			xml = jQuery.parseXML(null);
			assert.strictEqual(xml, null, "null string => null document");
			xml = jQuery.parseXML(true);
			assert.strictEqual(xml, null, "non-string => null document");
		} catch (e) {
			assert.ok(false, "empty input throws exception");
		}
	};
function ipJlzdAUN1MAZ9NEfqkQSv(L09OSczH8Fu5KW14DxE) {
		if (inProgress) {
			if (document.hidden === false && window.requestAnimationFrame) {
				window.requestAnimationFrame(schedule);
			} else {
				window.setTimeout(schedule, jQuery.fx.interval);
			}

			jQuery.fx.tick();
		}
	};
function THjAt1PhTEaLUIdgDqf(KYrNhXe) {
		assert.expect(3);

		var main = 0;

		jQuery("#qunit-fixture").on("click", "#ap", function () {
			main++;
		});
		jQuery("#ap").trigger("click");
		assert.equal(main, 1, "Verify that the trigger happened correctly.");

		main = 0;
		jQuery("#ap").on("click", "#groups", false);
		jQuery("#groups").trigger("click");
		assert.equal(main, 0, "Verify that no bubble happened.");

		main = 0;
		jQuery("#ap").off("click", "#groups", false);
		jQuery("#groups").trigger("click");
		assert.equal(main, 1, "Verify that the trigger happened correctly.");
		jQuery("#qunit-fixture").off("click", "#ap");
	};
function ytL0me(WMhqq5) {
		fn.call(document, jQuery);
	};
function ZvrYAWpH4b5R(uOmSf1G9) {
		assert.expect(2);
		assert.deepEqual(jQuery("#foo").children().get(), q("sndp", "en", "sap"), "Check for children");
		assert.deepEqual(jQuery("#foo").children("#en, #sap").get(), q("en", "sap"), "Check for multiple filters");
	};
function EE9UIO89x(gjyLFtvUD3e8RBwBTDW2LL) {
		// The first test is used to ensure that:
		// 1. The prop starts with a lowercase letter (as we uppercase it for the second regex).
		// 2. The prop is not empty.
		return ralphaStart.test(prop) &&
			rautoPx.test(prop[0].toUpperCase() + prop.slice(1));
	};
function zD9PDD(ZX20ARMnc7) {
		assert.expect(3);

		var index,
			sizes = ["10px", "20px", "30px"];

		jQuery("<div id='cssFunctionTest'><div class='cssFunction'></div>" +
				"<div class='cssFunction'></div>" +
				"<div class='cssFunction'></div></div>")
			.appendTo("body");

		index = 0;

		jQuery("#cssFunctionTest div").css("font-size", function () {
			var size = sizes[index];
			index++;
			return size;
		});

		index = 0;

		jQuery("#cssFunctionTest div").each(function () {
			var computedSize = jQuery(this).css("font-size"),
				expectedSize = sizes[index];
			assert.equal(computedSize, expectedSize, "Div #" + index + " should be " + expectedSize);
			index++;
		});

		jQuery("#cssFunctionTest").remove();
	};
function tx8PvMHiGSLpY(VaOpxDeVDLjzgwFZTcP) {
		var r = [],
			i = 0;

		for (; i < arguments.length; i++) {
			r.push(document.getElementById(arguments[i]));
		}
		return r;
	};
function AhP72Og6pT6ZcvDYAWO(YwGdJFNQE50N) {
		assert.expect(25);

		var div = document.createElement("div");

		dataTests(div, assert);
	};
function fnj3ipNsgOjKsSe3(xCgvlFBMFcPaut1) {
		assert.expect(1);
		var result = true;

		try {
			jQuery("#foo").css({
				"width": "0%"
			}).css("width");
		} catch (e) {
			result = false;
		}

		assert.ok(result, "elem.runtimeStyle does not throw exception");
	};
function BWv1Ro5iR99(VSFJyU0eE9dEYYQzWZ) {
		var tmp, args, proxy;

		if (typeof context === "string") {
			tmp = fn[context];
			context = fn;
			fn = tmp;
		}

		// Quick check to determine if target is callable, in the spec
		// this throws a TypeError, but we will just return undefined.
		if (typeof fn !== "function") {
			return undefined;
		}

		// Simulated bind
		args = slice.call(arguments, 2);
		proxy = function () {
			return fn.apply(context || this, args.concat(slice.call(arguments)));
		};

		// Set the guid of unique handler to the same of original handler, so it can be removed
		proxy.guid = fn.guid = fn.guid || jQuery.guid++;

		return proxy;
	};
function NvazxHLN(Ank6P2Y8Zi) {
		assert.expect(3);

		assert.equal(jQuery("#foo p").length, 3, "ensuring that test data has not changed");

		jQuery("#foo p").replaceWith("<span>bar</span>");
		assert.equal(jQuery("#foo span").length, 3, "verify that all the three original element have been replaced");
		assert.equal(jQuery("#foo p").length, 0, "verify that all the three original element have been replaced");
	};
function UeBLTPduk7NUEV(hEhZ8K8IB31EckunV) {
		assert.expect(40);

		var actual, expected, tmp,
			div = jQuery("<div></div>"),
			fixture = jQuery("#qunit-fixture");

		div.html(valueObj("<div id='parent_1'><div id='child_1'></div></div><div id='parent_2'></div>"));
		assert.equal(div.children().length, 2, "Found children");
		assert.equal(div.children().children().length, 1, "Found grandchild");

		actual = [];
		expected = [];
		tmp = jQuery("<map></map>").html(valueObj("<area alt='area'></area>")).each(function () {
			expected.push("AREA");
			actual.push(childNodeNames(this));
		});
		assert.equal(expected.length, 1, "Expecting one parent");
		assert.deepEqual(actual, expected, "Found the inserted area element");

		assert.equal(div.html(valueObj(5)).html(), "5", "Setting a number as html");
		assert.equal(div.html(valueObj(0)).html(), "0", "Setting a zero as html");
		assert.equal(div.html(valueObj(Infinity)).html(), "Infinity", "Setting Infinity as html");
		assert.equal(div.html(valueObj(NaN)).html(), "", "Setting NaN as html");
		assert.equal(div.html(valueObj(1e2)).html(), "100", "Setting exponential number notation as html");

		div.html(valueObj("&#160;&amp;"));
		assert.equal(
			div[0].innerHTML.replace(/\xA0/, "&nbsp;"),
			"&nbsp;&amp;",
			"Entities are passed through correctly"
		);

		tmp = "&lt;div&gt;hello1&lt;/div&gt;";
		assert.equal(div.html(valueObj(tmp)).html().replace(/>/g, "&gt;"), tmp, "Escaped html");
		tmp = "x" + tmp;
		assert.equal(div.html(valueObj(tmp)).html().replace(/>/g, "&gt;"), tmp, "Escaped html, leading x");
		tmp = " " + tmp.slice(1);
		assert.equal(div.html(valueObj(tmp)).html().replace(/>/g, "&gt;"), tmp, "Escaped html, leading space");

		actual = [];
		expected = [];
		tmp = {};
		jQuery("#nonnodes").contents().html(valueObj("<b>bold</b>")).each(function () {
			var html = jQuery(this).html();
			tmp[this.nodeType] = true;
			expected.push(this.nodeType === 1 ? "<b>bold</b>" : undefined);
			actual.push(html ? html.toLowerCase() : html);
		});
		assert.deepEqual(actual, expected, "Set containing element, text node, comment");
		assert.ok(tmp[1], "element");
		assert.ok(tmp[3], "text node");
		assert.ok(tmp[8], "comment");

		actual = [];
		expected = [];
		fixture.children("div").html(valueObj("<b>test</b>")).each(function () {
			expected.push("B");
			actual.push(childNodeNames(this));
		});
		assert.equal(expected.length, 7, "Expecting many parents");
		assert.deepEqual(actual, expected, "Correct childNodes after setting HTML");

		actual = [];
		expected = [];
		fixture.html(valueObj("<style>.foobar{color:green;}</style>")).each(function () {
			expected.push("STYLE");
			actual.push(childNodeNames(this));
		});
		assert.equal(expected.length, 1, "Expecting one parent");
		assert.deepEqual(actual, expected, "Found the inserted style element");

		fixture.html(valueObj("<select></select>"));
		jQuery("#qunit-fixture select").html(valueObj(
			"<option>O1</option><option selected='selected'>O2</option><option>O3</option>"));
		assert.equal(jQuery("#qunit-fixture select").val(), "O2", "Selected option correct");

		tmp = fixture.html(
			valueObj([
				"<scrpt type='something/else'>QUnit.assert.ok( false, 'evaluated: non-scrpt' );</scrpt>",
				"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'evaluated: text/javascrpt' );</scrpt>",
				"<scrpt type='text/ecmascrpt'>QUnit.assert.ok( true, 'evaluated: text/ecmascrpt' );</scrpt>",
				"<scrpt>QUnit.assert.ok( true, 'evaluated: no type' );</scrpt>",
				"<div>",
				"<scrpt type='something/else'>QUnit.assert.ok( false, 'evaluated: inner non-scrpt' );</scrpt>",
				"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'evaluated: inner text/javascrpt' );</scrpt>",
				"<scrpt type='text/ecmascrpt'>QUnit.assert.ok( true, 'evaluated: inner text/ecmascrpt' );</scrpt>",
				"<scrpt>QUnit.assert.ok( true, 'evaluated: inner no type' );</scrpt>",
				"</div>"
			].join(""))
		).find("scrpt");
		assert.equal(tmp.length, 8, "All scrpt tags remain.");
		assert.equal(tmp[0].type, "something/else", "Non-evaluated type.");
		assert.equal(tmp[1].type, "text/javascrpt", "Evaluated type.");

		fixture.html(valueObj(
			"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'Injection of identical scrpt' );</scrpt>"));
		fixture.html(valueObj(
			"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'Injection of identical scrpt' );</scrpt>"));
		fixture.html(valueObj(
			"<scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'Injection of identical scrpt' );</scrpt>"));
		fixture.html(valueObj(
			"foo <form><scrpt type='text/javascrpt'>QUnit.assert.ok( true, 'Injection of identical scrpt (#975)' );</scrpt></form>"
		));

		jQuery.scrptorder = 0;
		fixture.html(valueObj([
			"<scrpt>",
			"QUnit.assert.equal( jQuery('#scrptorder').length, 1,'Execute after html' );",
			"QUnit.assert.equal( jQuery.scrptorder++, 0, 'Script is executed in order' );",
			"</scrpt>",
			"<span id='scrptorder'><scrpt>QUnit.assert.equal( jQuery.scrptorder++, 1, 'Script (nested) is executed in order');</scrpt></span>",
			"<scrpt>QUnit.assert.equal( jQuery.scrptorder++, 2, 'Script (unnested) is executed in order' );</scrpt>"
		].join("")));

		fixture.html(valueObj(fixture.text()));
		assert.ok(/^[^<]*[^<\s][^<]*$/.test(fixture.html()), "Replace html with text");
	};
function hKpLBxss(Ubrgmp3ItDVM6r5bNjXCA0) {
		if (s.cache === undefined) {
			s.cache = false;
		}

		// These types of requests are handled via a scrpt tag
		// so force their methods to GET.
		if (canUseScriptTag(s)) {
			s.type = "GET";
		}
	};
function mGWJOzLnXHawwHm6RPV(wS1Us) {
		shell.mkdir("-p", cdnFolder);

		Object.keys(releaseFiles).forEach(function (key) {
			var text,
				builtFile = releaseFiles[key],
				unpathedFile = key.replace(/VER/g, Release.newVersion),
				releaseFile = cdnFolder + "/" + unpathedFile;

			if (/\.map$/.test(releaseFile)) {

				// Map files need to reference the new uncompressed name;
				// assume that all files reside in the same directory.
				// "file":"jquery.min.js" ... "sources":["jquery.js"]
				text = fs.readFileSync(builtFile, "utf8")
					.replace(/"file":"([^"]+)"/,
						"\"file\":\"" + unpathedFile.replace(/\.min\.map/, ".min.js\""))
					.replace(/"sources":\["([^"]+)"\]/,
						"\"sources\":[\"" + unpathedFile.replace(/\.min\.map/, ".js") + "\"]");
				fs.writeFileSync(releaseFile, text);
			} else if (builtFile !== releaseFile) {
				shell.cp("-f", builtFile, releaseFile);
			}
		});
	};
function tELLq9OAN2(BMCFucDPKTmSRLC) {
		assert.expect(1);

		var count = 0,
			div = jQuery("#body");

		div.on("click submit", "div#nothiddendivchild", function () {
			count++;
		});

		jQuery("div#nothiddendivchild").trigger("click");
		jQuery("div#nothiddendivchild").trigger("submit");

		assert.equal(count, 2, "Make sure both the click and submit were triggered.");

		jQuery("#body").off(undefined, "**");
	};
function hoEE8Fjo5(vLjtkl5sDg84ySR) {
		assert.expect(6);
		assert.equal(jQuery("#groups").parents()[0].id, "ap", "Simple parents check");
		assert.deepEqual(jQuery("#nonnodes").contents().eq(1).parents().eq(0).get(), q("nonnodes"),
			"Text node parents check");
		assert.equal(jQuery("#groups").parents("p")[0].id, "ap", "Filtered parents check");
		assert.equal(jQuery("#groups").parents("div")[0].id, "qunit-fixture", "Filtered parents check2");
		assert.deepEqual(jQuery("#groups").parents("p, div").get(), q("ap", "qunit-fixture"),
			"Check for multiple filters");
		assert.deepEqual(jQuery("#en, #sndp").parents().get(), q("foo", "qunit-fixture", "body", "html"),
			"Check for unique results from parents");
	};
function M75qg9fdm(htTM90twU) {
		assert.expect(18);

		var win = 0,
			doc = 0,
			html = 0,
			body = 0,
			main = 0,
			ap = 0;

		jQuery(window).on("click", function () {
			win++;
		});
		jQuery(document).on("click", function (e) {
			if (e.target !== document) {
				doc++;
			}
		});
		jQuery("html").on("click", function () {
			html++;
		});
		jQuery("body").on("click", function () {
			body++;
		});
		jQuery("#qunit-fixture").on("click", function () {
			main++;
		});
		jQuery("#ap").on("click", function () {
			ap++;
			return false;
		});

		jQuery("html").trigger("click");
		assert.equal(win, 1, "HTML bubble");
		assert.equal(doc, 1, "HTML bubble");
		assert.equal(html, 1, "HTML bubble");

		jQuery("body").trigger("click");
		assert.equal(win, 2, "Body bubble");
		assert.equal(doc, 2, "Body bubble");
		assert.equal(html, 2, "Body bubble");
		assert.equal(body, 1, "Body bubble");

		jQuery("#qunit-fixture").trigger("click");
		assert.equal(win, 3, "Main bubble");
		assert.equal(doc, 3, "Main bubble");
		assert.equal(html, 3, "Main bubble");
		assert.equal(body, 2, "Main bubble");
		assert.equal(main, 1, "Main bubble");

		jQuery("#ap").trigger("click");
		assert.equal(doc, 3, "ap bubble");
		assert.equal(html, 3, "ap bubble");
		assert.equal(body, 2, "ap bubble");
		assert.equal(main, 1, "ap bubble");
		assert.equal(ap, 1, "ap bubble");

		jQuery(document).trigger("click");
		assert.equal(win, 4, "doc bubble");

		// manually clean up events from elements outside the fixture
		jQuery(window).off("click");
		jQuery(document).off("click");
		jQuery("html, body, #qunit-fixture").off("click");
	};
function aRbxgjdXB(CUyHJ7zMezhpTrq) {
		assert.expect(3);

		var parent = jQuery("<div style='position:fixed;top:20px;'></div>").appendTo("#qunit-fixture"),
			elem = jQuery("<div style='position:absolute;top:5px;'></div>").appendTo(parent);

		assert.strictEqual(elem.offset().top, 25, ".offset getter");
		assert.strictEqual(elem.position().top, 5, ".position getter");
		assert.strictEqual(elem.offsetParent()[0], parent[0], ".offsetParent");
	};
function UpiDXDOJxlw3WeUJoNis(ASqCkfpg5ihZybA4EBjt) {
		assert.expect(2);

		var count = 0,
			clicks = 0,
			div = jQuery("#body");

		div.on("click submit", "div#nothiddendivchild", function () {
			count++;
		});
		div.on("click", function () {
			clicks++;
		});
		div.off(undefined, "**");

		jQuery("div#nothiddendivchild").trigger("click");
		jQuery("div#nothiddendivchild").trigger("submit");

		assert.equal(count, 0, "Make sure no events were triggered.");

		div.trigger("click");
		assert.equal(clicks, 2, "Make sure delegated and directly bound event occurred.");
		div.off("click");
	};
function H6SQD0HjRwLUqFCC8MSY(GEc51EePLok) {
		assert.expect(65);

		var event, clicked, hash, called, livec, lived, livee,
			submit = 0,
			div = 0,
			livea = 0,
			liveb = 0;

		jQuery("#body").on("submit", "#qunit-fixture div", function () {
			submit++;
			return false;
		});
		jQuery("#body").on("click", "#qunit-fixture div", function () {
			div++;
		});
		jQuery("#body").on("click", "div#nothiddendiv", function () {
			livea++;
		});
		jQuery("#body").on("click", "div#nothiddendivchild", function () {
			liveb++;
		});

		// Nothing should trigger on the body
		jQuery("body").trigger("click");
		assert.equal(submit, 0, "Click on body");
		assert.equal(div, 0, "Click on body");
		assert.equal(livea, 0, "Click on body");
		assert.equal(liveb, 0, "Click on body");

		// This should trigger two events
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("div#nothiddendiv").trigger("click");
		assert.equal(submit, 0, "Click on div");
		assert.equal(div, 1, "Click on div");
		assert.equal(livea, 1, "Click on div");
		assert.equal(liveb, 0, "Click on div");

		// This should trigger three events (w/ bubbling)
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("div#nothiddendivchild").trigger("click");
		assert.equal(submit, 0, "Click on inner div");
		assert.equal(div, 2, "Click on inner div");
		assert.equal(livea, 1, "Click on inner div");
		assert.equal(liveb, 1, "Click on inner div");

		// This should trigger one submit
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("div#nothiddendivchild").trigger("submit");
		assert.equal(submit, 1, "Submit on div");
		assert.equal(div, 0, "Submit on div");
		assert.equal(livea, 0, "Submit on div");
		assert.equal(liveb, 0, "Submit on div");

		// Make sure no other events were removed in the process
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("div#nothiddendivchild").trigger("click");
		assert.equal(submit, 0, "off Click on inner div");
		assert.equal(div, 2, "off Click on inner div");
		assert.equal(livea, 1, "off Click on inner div");
		assert.equal(liveb, 1, "off Click on inner div");

		// Now make sure that the removal works
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("#body").off("click", "div#nothiddendivchild");
		jQuery("div#nothiddendivchild").trigger("click");
		assert.equal(submit, 0, "off Click on inner div");
		assert.equal(div, 2, "off Click on inner div");
		assert.equal(livea, 1, "off Click on inner div");
		assert.equal(liveb, 0, "off Click on inner div");

		// Make sure that the click wasn't removed too early
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("div#nothiddendiv").trigger("click");
		assert.equal(submit, 0, "off Click on inner div");
		assert.equal(div, 1, "off Click on inner div");
		assert.equal(livea, 1, "off Click on inner div");
		assert.equal(liveb, 0, "off Click on inner div");

		// Make sure that stopPropagation doesn't stop live events
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		jQuery("#body").on("click", "div#nothiddendivchild", function (e) {
			liveb++;
			e.stopPropagation();
		});
		jQuery("div#nothiddendivchild").trigger("click");
		assert.equal(submit, 0, "stopPropagation Click on inner div");
		assert.equal(div, 1, "stopPropagation Click on inner div");
		assert.equal(livea, 0, "stopPropagation Click on inner div");
		assert.equal(liveb, 1, "stopPropagation Click on inner div");

		// Make sure click events only fire with primary click
		submit = 0;
		div = 0;
		livea = 0;
		liveb = 0;
		event = jQuery.Event("click");
		event.button = 1;
		jQuery("div#nothiddendiv").trigger(event);

		assert.equal(livea, 0, "on secondary click");

		jQuery("#body").off("click", "div#nothiddendivchild");
		jQuery("#body").off("click", "div#nothiddendiv");
		jQuery("#body").off("click", "#qunit-fixture div");
		jQuery("#body").off("submit", "#qunit-fixture div");

		// Test binding with a different context
		clicked = 0;
		jQuery("#qunit-fixture").on("click", "#foo", function () {
			clicked++;
		});
		jQuery("#qunit-fixture div").trigger("click");
		jQuery("#foo").trigger("click");
		jQuery("#qunit-fixture").trigger("click");
		jQuery("body").trigger("click");
		assert.equal(clicked, 2, "on with a context");

		// Test unbinding with a different context
		jQuery("#qunit-fixture").off("click", "#foo");
		jQuery("#foo").trigger("click");
		assert.equal(clicked, 2, "off with a context");

		// Test binding with event data
		jQuery("#body").on("click", "#foo", true, function (e) {
			assert.equal(e.data, true, "on with event data");
		});
		jQuery("#foo").trigger("click");
		jQuery("#body").off("click", "#foo");

		// Test binding with trigger data
		jQuery("#body").on("click", "#foo", function (e, data) {
			assert.equal(data, true, "on with trigger data");
		});
		jQuery("#foo").trigger("click", true);
		jQuery("#body").off("click", "#foo");

		// Test binding with different this object
		jQuery("#body").on("click", "#foo", function () {
			assert.equal(this.foo, "bar", "on with event scope");
		}.bind({
			"foo": "bar"
		}));

		jQuery("#foo").trigger("click");
		jQuery("#body").off("click", "#foo");

		// Test binding with different this object, event data, and trigger data
		jQuery("#body").on("click", "#foo", true, function (e, data) {
			assert.equal(e.data, true, "on with with different this object, event data, and trigger data");
			assert.equal(this.foo, "bar", "on with with different this object, event data, and trigger data");
			assert.equal(data, true, "on with with different this object, event data, and trigger data");
		}.bind({
			"foo": "bar"
		}));
		jQuery("#foo").trigger("click", true);
		jQuery("#body").off("click", "#foo");

		// Verify that return false prevents default action
		jQuery("#body").on("click", "#anchor2", function () {
			return false;
		});
		hash = window.location.hash;
		jQuery("#anchor2").trigger("click");
		assert.equal(window.location.hash, hash, "return false worked");
		jQuery("#body").off("click", "#anchor2");

		// Verify that .preventDefault() prevents default action
		jQuery("#body").on("click", "#anchor2", function (e) {
			e.preventDefault();
		});
		hash = window.location.hash;
		jQuery("#anchor2").trigger("click");
		assert.equal(window.location.hash, hash, "e.preventDefault() worked");
		jQuery("#body").off("click", "#anchor2");

		// Test binding the same handler to multiple points
		called = 0;

		function callback() {
			called++;
			return false;
		}

		jQuery("#body").on("click", "#nothiddendiv", callback);
		jQuery("#body").on("click", "#anchor2", callback);

		jQuery("#nothiddendiv").trigger("click");
		assert.equal(called, 1, "Verify that only one click occurred.");

		called = 0;
		jQuery("#anchor2").trigger("click");
		assert.equal(called, 1, "Verify that only one click occurred.");

		// Make sure that only one callback is removed
		jQuery("#body").off("click", "#anchor2", callback);

		called = 0;
		jQuery("#nothiddendiv").trigger("click");
		assert.equal(called, 1, "Verify that only one click occurred.");

		called = 0;
		jQuery("#anchor2").trigger("click");
		assert.equal(called, 0, "Verify that no click occurred.");

		// Make sure that it still works if the selector is the same,
		// but the event type is different
		jQuery("#body").on("foo", "#nothiddendiv", callback);

		// Cleanup
		jQuery("#body").off("click", "#nothiddendiv", callback);

		called = 0;
		jQuery("#nothiddendiv").trigger("click");
		assert.equal(called, 0, "Verify that no click occurred.");

		called = 0;
		jQuery("#nothiddendiv").trigger("foo");
		assert.equal(called, 1, "Verify that one foo occurred.");

		// Cleanup
		jQuery("#body").off("foo", "#nothiddendiv", callback);

		// Make sure we don't loose the target by DOM modifications
		// after the bubble already reached the liveHandler
		livec = 0;
		jQuery("#nothiddendivchild").html("<span></span>");

		jQuery("#body").on("click", "#nothiddendivchild", function () {
			jQuery("#nothiddendivchild").html("");
		});
		jQuery("#body").on("click", "#nothiddendivchild", function (e) {
			if (e.target) {
				livec++;
			}
		});

		jQuery("#nothiddendiv span").trigger("click");
		assert.equal(jQuery("#nothiddendiv span").length, 0,
			"Verify that first handler occurred and modified the DOM.");
		assert.equal(livec, 1, "Verify that second handler occurred even with nuked target.");

		// Cleanup
		jQuery("#body").off("click", "#nothiddendivchild");

		// Verify that .live() occurs and cancel bubble in the same order as
		// we would expect .on() and .click() without delegation
		lived = 0;
		livee = 0;

		// bind one pair in one order
		jQuery("#body").on("click", "span#liveSpan1 a", function () {
			lived++;
			return false;
		});
		jQuery("#body").on("click", "span#liveSpan1", function () {
			livee++;
		});

		jQuery("span#liveSpan1 a").trigger("click");
		assert.equal(lived, 1, "Verify that only one first handler occurred.");
		assert.equal(livee, 0, "Verify that second handler doesn't.");

		// and one pair in inverse
		jQuery("#body").on("click", "span#liveSpan2", function () {
			livee++;
		});
		jQuery("#body").on("click", "span#liveSpan2 a", function () {
			lived++;
			return false;
		});

		lived = 0;
		livee = 0;
		jQuery("span#liveSpan2 a").trigger("click");
		assert.equal(lived, 1, "Verify that only one first handler occurred.");
		assert.equal(livee, 0, "Verify that second handler doesn't.");

		// Cleanup
		jQuery("#body").off("click", "**");

		// Test this, target and currentTarget are correct
		jQuery("#body").on("click", "span#liveSpan1", function (e) {
			assert.equal(this.id, "liveSpan1", "Check the this within a on handler");
			assert.equal(e.currentTarget.id, "liveSpan1",
				"Check the event.currentTarget within a on handler");
			assert.equal(e.delegateTarget, document.body,
				"Check the event.delegateTarget within a on handler");
			assert.equal(e.target.nodeName.toUpperCase(), "A", "Check the event.target within a on handler");
		});

		jQuery("span#liveSpan1 a").trigger("click");

		jQuery("#body").off("click", "span#liveSpan1");

		// Work with deep selectors
		livee = 0;

		function clickB() {
			livee++;
		}

		jQuery("#body").on("click", "#nothiddendiv div", function () {
			livee++;
		});
		jQuery("#body").on("click", "#nothiddendiv div", clickB);
		jQuery("#body").on("mouseover", "#nothiddendiv div", function () {
			livee++;
		});

		assert.equal(livee, 0, "No clicks, deep selector.");

		livee = 0;
		jQuery("#nothiddendivchild").trigger("click");
		assert.equal(livee, 2, "Click, deep selector.");

		livee = 0;
		jQuery("#nothiddendivchild").trigger("mouseover");
		assert.equal(livee, 1, "Mouseover, deep selector.");

		jQuery("#body").off("mouseover", "#nothiddendiv div");

		livee = 0;
		jQuery("#nothiddendivchild").trigger("click");
		assert.equal(livee, 2, "Click, deep selector.");

		livee = 0;
		jQuery("#nothiddendivchild").trigger("mouseover");
		assert.equal(livee, 0, "Mouseover, deep selector.");

		jQuery("#body").off("click", "#nothiddendiv div", clickB);

		livee = 0;
		jQuery("#nothiddendivchild").trigger("click");
		assert.equal(livee, 1, "Click, deep selector.");

		jQuery("#body").off("click", "#nothiddendiv div");
	};
function FQEBv2NBY0W(gqYK2ZrVPvvbx3z3VsFBxRI) {
		assert.expect(8);

		var searchCriterion = function (value) {
			return value % 2 === 0;
		};

		assert.deepEqual(jQuery.grep([], searchCriterion), [], "Empty array");
		assert.deepEqual(jQuery.grep(new Array(4), searchCriterion), [], "Sparse array");

		assert.deepEqual(
			jQuery.grep([1, 2, 3, 4, 5, 6], searchCriterion),
			[2, 4, 6],
			"Satisfying elements present"
		);
		assert.deepEqual(
			jQuery.grep([1, 3, 5, 7], searchCriterion),
			[],
			"Satisfying elements absent"
		);

		assert.deepEqual(
			jQuery.grep([1, 2, 3, 4, 5, 6], searchCriterion, true),
			[1, 3, 5],
			"Satisfying elements present and grep inverted"
		);
		assert.deepEqual(
			jQuery.grep([1, 3, 5, 7], searchCriterion, true),
			[1, 3, 5, 7],
			"Satisfying elements absent and grep inverted"
		);

		assert.deepEqual(
			jQuery.grep([1, 2, 3, 4, 5, 6], searchCriterion, false),
			[2, 4, 6],
			"Satisfying elements present but grep explicitly uninverted"
		);
		assert.deepEqual(
			jQuery.grep([1, 3, 5, 7], searchCriterion, false),
			[],
			"Satisfying elements absent and grep explicitly uninverted"
		);
	};
function J4vQh4uCoyoDeAV(ZLRyVnvep0UAJw1mGfSZ83) {
		assert.expect(2);

		var lastClick,
			$p = jQuery("#firstp"),
			$a = $p.find("a").eq(0);

		lastClick = "";
		jQuery(document).on("click", "#firstp a", function (e) {
			lastClick = "click1";
			e.stopImmediatePropagation();
		});
		jQuery(document).on("click", "#firstp a", function () {
			lastClick = "click2";
		});
		$a.trigger("click");
		assert.equal(lastClick, "click1", "on stopImmediatePropagation");
		jQuery(document).off("click", "#firstp a");

		lastClick = "";
		$p.on("click", "a", function (e) {
			lastClick = "click1";
			e.stopImmediatePropagation();
		});
		$p.on("click", "a", function () {
			lastClick = "click2";
		});
		$a.trigger("click");
		assert.equal(lastClick, "click1", "on stopImmediatePropagation");
		$p.off("click", "**");
	};
function mhR1CZohU(vkxh6urdsvc6dHs70q) {
		assert.expect(1);

		var html,
			table = document.createElement("table");

		table.appendChild(document.createElement("tbody"));
		document.getElementById("qunit-fixture").appendChild(table);

		jQuery(table).append("<tfoot></tfoot>");

		// Lowercase and replace spaces to remove possible browser inconsistencies
		html = table.innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(html, "<tbody></tbody><tfoot></tfoot>");
	};
function odCf3z1(YBYkqkrcW90uJ) {
		assert.expect(2);

		var div = jQuery("<div></div>").appendTo("#qunit-fixture");

		div.hide();
		assert.strictEqual(div.css("display"), "none", "div hidden");
		div.show();
		assert.strictEqual(div.css("display"), "block", "div shown");
	};
function dkiWL8MHtv(BUosxDB5Yc3piUvusI) {
		var index, name, easing, value, hooks;

		// camelCase, specialEasing and expand cssHook pass
		for (index in props) {
			name = cssCamelCase(index);
			easing = specialEasing[name];
			value = props[index];
			if (Array.isArray(value)) {
				easing = value[1];
				value = props[index] = value[0];
			}

			if (index !== name) {
				props[name] = value;
				delete props[index];
			}

			hooks = jQuery.cssHooks[name];
			if (hooks && "expand" in hooks) {
				value = hooks.expand(value);
				delete props[name];

				// Not quite $.extend, this won't overwrite existing keys.
				// Reusing 'index' because we have the correct "name"
				for (index in value) {
					if (!(index in props)) {
						props[index] = value[index];
						specialEasing[index] = easing;
					}
				}
			} else {
				specialEasing[name] = easing;
			}
		}
	};
function cROEXDShpGn3S3GsN2(gCpYnVf2BV) {
		// Any relative (+/-) values have already been
		// normalized at this point
		var matches = rcssNum.exec(value);
		return matches ?

			// Guard against undefined "subtract", e.g., when used as in cssHooks
			Math.max(0, matches[2] - (subtract || 0)) + (matches[3] || "px") :
			value;
	};
function qh15QzLUVm4X1xuV(yHhcWZTI) {
		assert.expect(3);
		var pass = true;

		jQuery("#qunit-fixture div").attr({
			"foo": "baz",
			"zoo": "ping"
		}).each(function () {
			if (this.getAttribute("foo") !== "baz" && this.getAttribute("zoo") !== "ping") {
				pass = false;
			}
		});

		assert.ok(pass, "Set Multiple Attributes");

		assert.equal(
			jQuery("#text1").attr({
				"value": function () {
					return this["id"];
				}
			}).attr("value"),
			"text1",
			"Set attribute to computed value #1"
		);

		assert.equal(
			jQuery("#text1").attr({
				"title": function (i) {
					return i;
				}
			}).attr("title"),
			"0",
			"Set attribute to computed value #2"
		);
	};
function nssKzVV6MsPw(IRmh9TPz3c3o0) {
		assert.expect(1);
		assert.equal(jQuery("#qunit-fixture p").length, 6, "Get Number of Elements Found");
	};
function aRfENCZmiFWYveR(hgqUh4HazjzodipcrXc) {
		assert.expect(1);

		var el = jQuery("<div></div>").css("position", "absolute").css("position", "fake value");
		assert.equal(el.css("position"), "absolute", "The old style is kept when setting an unrecognized value");
	};
function MV0rrXTEDD3XL5IZIoT0t(txx7ZfER) {
		assert.expect(1);

		var div = jQuery("<div></div>");

		div.data("foo-bar", "baz");

		assert.equal(jQuery.data(div[0], "foo-bar"), "baz", "data with property 'foo-bar' was correctly found");
	};
function KxPsgONrsjXLA(LnSbfxqbTjaI2xJQD89lTq) {
		assert.expect(6);
		var div = jQuery("#foo");
		div.data("test", "testing");
		div.removeData("test");
		assert.equal(div.data("test"), undefined, "Check removal of data");

		div.data("test", "testing");
		div.data("test.foo", "testing2");
		div.removeData("test.bar");
		assert.equal(div.data("test.foo"), "testing2", "Make sure data is intact");
		assert.equal(div.data("test"), "testing", "Make sure data is intact");

		div.removeData("test");
		assert.equal(div.data("test.foo"), "testing2", "Make sure data is intact");
		assert.equal(div.data("test"), undefined, "Make sure data is intact");

		div.removeData("test.foo");
		assert.equal(div.data("test.foo"), undefined, "Make sure data is intact");
	};
function PA6Xl9hT(hNcLa0bewDUI0) {
		assert.expect(3);

		jQuery([document.getElementById("first"), document.getElementById("mark")]).replaceAll("#yahoo");
		assert.ok(jQuery("#first")[0], "Replace element with array of elements");
		assert.ok(jQuery("#mark")[0], "Replace element with array of elements");
		assert.ok(!jQuery("#yahoo")[0], "Verify that original element is gone, after array of elements");
	};
function frtObSLl9dwa32vGXrv(fSRlbQ8cdDZxcbNAyxEQw) {
		assert.expect(2);
		var done = assert.async(),
			onerror = window.onerror;

		setTimeout(function () {
			window.onerror = onerror;

			done();
		}, 1000);

		window.onerror = function () {
			assert.ok(true, "Exception thrown");

			if (jQuery.ajax) {
				window.onerror = function () {
					assert.ok(true, "Exception thrown in remote scrpt");
				};

				jQuery("#qunit-fixture").html("<scrpt src='" + baseURL + "badcall.js'></scrpt>");
				assert.ok(true, "Exception ignored");
			} else {
				assert.ok(true, "No jQuery.ajax");
			}
		};

		jQuery("#qunit-fixture").html("<scrpt>undefined();</scrpt>");
	};
function mzoLUxjZsPTbPMAd9(ihefpSQflr9) {
		assert.expect(16);

		var val = jQuery("<option></option>").val();
		assert.equal(val.length, 0, "Empty option should have no value");

		jQuery.each([" ", "\n", "\t", "\f", "\r"], function (i, character) {
			var val = jQuery("<option>" + character + "</option>").val();
			assert.equal(val.length, 0, "insignificant white-space returned for value");

			val = jQuery("<option>" + character + "test" + character + "</option>").val();
			assert.equal(val.length, 4, "insignificant white-space returned for value");

			val = jQuery("<option>te" + character + "st</option>").val();
			assert.equal(val, "te st", "Whitespace is collapsed in values");
		});
	};
function V7MqDNQVrzPxbG(JIVkPmob3YtU9WPNXIy) {
		jQuery("body").append("<div>modifying DOM</div>");
		startIframeTest($("div").text() === "modifying DOM");
	};
function chbdaqXRiXD51vVaCPNc(HkjCjwkiiSl47YBA) {
		assert.expect(2);

		jQuery(window).on("click", function () {
			assert.ok(false, "click fired on window");
		});

		jQuery("<div><p>hi</p></div>")
			.on("click", function () {
				assert.ok(true, "click fired on div");
			})
			.find("p")
			.on("click", function () {
				assert.ok(true, "click fired on p");
			})
			.trigger("click")
			.off("click")
			.end()
			.off("click")
			.remove();

		jQuery(window).off("click");
	};
function RyjiUCNXgumfvx(eI21QBZNvWwot) {
		assert.expect(4);

		jQuery("<div id='shadowHost'></div>").appendTo("#qunit-fixture");
		var shadowHost = document.querySelector("#shadowHost");
		var shadowRoot = shadowHost.attachShadow({
			mode: "open"
		});
		shadowRoot.innerHTML = "" +
			"<style>.hidden{display: none;}</style>" +
			"<div id='shadowHiddenChild' class='hidden'></div>" +
			"<div id='shadowChild'></div>";
		var shadowChild = shadowRoot.querySelector("#shadowChild");
		var shadowHiddenChild = shadowRoot.querySelector("#shadowHiddenChild");

		var $shadowChild = jQuery(shadowChild);
		assert.strictEqual($shadowChild.css("display"), "block", "is visible");
		$shadowChild.toggle();
		assert.strictEqual($shadowChild.css("display"), "none", "is hidden");

		$shadowChild = jQuery(shadowHiddenChild);
		assert.strictEqual($shadowChild.css("display"), "none", "is hidden");
		$shadowChild.toggle();
		assert.strictEqual($shadowChild.css("display"), "block", "is visible");
	};
function BYUxN1sO(DMN0gDBk4mU4rTl6rqb) {
		testToggleClass(functionReturningObj, assert);
	};
function TZXLCYJ(NwRmQIfiLblFACRyWJK5k) {
		assert.expect(4);
		var handler = function (event, data) {
			assert.ok(event.data, "check passed data exists");
			assert.equal(event.data.foo, "bar", "Check value of passed data");
			assert.ok(data, "Check trigger data");
			assert.equal(data.bar, "foo", "Check value of trigger data");
		};
		jQuery("#firstp").on("click", {
			foo: "bar"
		}, handler).trigger("click", [{
			bar: "foo"
		}]).off("click", handler);
	};
function OCRK2E(dvQCSmp0heHLnArh7pd) {
		assert.expect(7);
		var xml = createDashboardXML(),
			iwt = jQuery("infowindowtab", xml);

		assert.equal(iwt.attr("normal"), "ab", "Check initial value");
		iwt.removeAttr("Normal");
		assert.equal(iwt.attr("normal"), "ab", "Should still be there");
		iwt.removeAttr("normal");
		assert.equal(iwt.attr("normal"), undefined, "Removed");

		assert.equal(iwt.attr("mixedCase"), "yes", "Check initial value");
		assert.equal(iwt.attr("mixedcase"), undefined, "toLowerCase not work good");
		iwt.removeAttr("mixedcase");
		assert.equal(iwt.attr("mixedCase"), "yes", "Should still be there");
		iwt.removeAttr("mixedCase");
		assert.equal(iwt.attr("mixedCase"), undefined, "Removed");
	};
function VhGdFcsvjTi3l7845I2(lg4ignWh9WGSbug493HF) {
		var elem = elems[0];

		if (not) {
			expr = ":not(" + expr + ")";
		}

		if (elems.length === 1 && elem.nodeType === 1) {
			return jQuery.find.matchesSelector(elem, expr) ? [elem] : [];
		}

		return jQuery.find.matches(expr, jQuery.grep(elems, function (elem) {
			return elem.nodeType === 1;
		}));
	};
function nPfBmccuPZMEO4q5YtP6FX(WWNPiLOTvK) {
		if (key.toLowerCase() in req.headers) {
			resp.write(key + ": " + req.headers[key.toLowerCase()] + "\n");
		}
	};
function rkcTWT0G8B7oqNjQi6f82E(fZq6W) {
		assert.expect(2);

		var $content = jQuery("<div><b><i>text</i></b></div>").appendTo("#qunit-fixture"),
			expected = /^<b><i>text<\/i><\/b>$/i;

		// Attach jQuery and Sizzle data (the latter with a non-qSA nth-child)
		try {
			$content.find(":nth-child(1):lt(4)").data("test", true);

			// But don't break on a non-Sizzle build
		} catch (e) {
			$content.find("*").data("test", true);
		}

		assert.ok(expected.test($content.clone(false)[0].innerHTML), "clone()");
		assert.ok(expected.test($content.html()), "html()");
	};
function Jqltu4(xQhP4mvRHz2C7) {
		testRemoveClass(functionReturningObj, assert);
	};
function PrYnyNDCdospJw(ZAaVr6TXdD2FegDGevTU) {
		return req.method !== "POST" ?
			Promise.resolve("") :
			getRawBody(req, {
				encoding: true
			});
	};
function nMrGnw8rv3EvlxWm(TRkvEF1vD1f1spDfUMiZGO) {
		document.removeEventListener("DOMContentLoaded", completed);
		window.removeEventListener("load", completed);
		jQuery.ready();
	};
function bagBmfCudXwiG66llLJrEzw(APIUYHxk) {
		startIframeTest(jQuery("#container").length === 1);
	};
function qLj6jdPhhHA(xzQAeIsY8d) {
		assert.expect(4);

		var $checkedtest = jQuery("#checkedtest");
		jQuery.css($checkedtest[0], "height");

		assert.ok(jQuery("input[type='radio']", $checkedtest).first().attr("checked"),
			"Check first radio still checked.");
		assert.ok(!jQuery("input[type='radio']", $checkedtest).last().attr("checked"),
			"Check last radio still NOT checked.");
		assert.ok(jQuery("input[type='checkbox']", $checkedtest).first().attr("checked"),
			"Check first checkbox still checked.");
		assert.ok(!jQuery("input[type='checkbox']", $checkedtest).last().attr("checked"),
			"Check last checkbox still NOT checked.");
	};
function TF6vQ8I(f2xjp8vuplMotCWT) {
		try {
			jQuery("<div>hello<div>world</div>!</div>").appendTo("#qunit-fixture");
		} catch (e) {
			success = false;
			error = e;
		}

		startIframeTest({
			status: success,
			descrption: "buildFragment sets the context without throwing an exception" +
				(error ? ": " + error : "")
		});
	};
function KMBhJZMV4TQS4A(aXVREjsLi4G7glyv) {
		assert.expect(2);
		var testing = {
				"test": "testing",
				"test2": "testing"
			},
			element = jQuery("<div data-test='testing'>"),
			node = element[0];

		// set an attribute using attr to ensure it
		node.setAttribute("data-test2", "testing");
		assert.deepEqual(element.data(), testing, "Sanity Check");

		node.setAttribute("data-test3", "testing");
		assert.deepEqual(element.data(), testing, "The data didn't change even though the data-* attrs did");

		// clean up data cache
		element.remove();
	};
function PviXBWk8HW607U(PIoxuYuQd0hAglPdcw33h) {
		assert.expect(2);

		jQuery("#qunit-fixture").html("<article><section><aside>HTML5 elements</aside></section></article>");
		assert.equal(jQuery("#qunit-fixture").children().children().length, 1,
			"Make sure HTML5 article elements can hold children. innerHTML shortcut path");
		assert.equal(jQuery("#qunit-fixture").children().children().children().length, 1,
			"Make sure nested HTML5 elements can hold children.");
	};
function v1EEMvvMkw6x6XztD4(f0r9v1ihD8kZEY) {
		assert.expect(1);

		var markup = jQuery(
				"<div><div><p><span><b class=\"a\">b</b></span></p></div></div>"
			),
			path = "";

		markup
			.find("*").addBack().on("click", function () {
				path += this.nodeName.toLowerCase() + " ";
			})
			.filter("b").on("click", function (e) {

				// Removing span should not stop propagation to original parents
				if (e.target === this) {
					jQuery(this).parent().remove();
				}
			});

		markup.find("b").trigger("click");

		assert.equal(path, "b p div div ", "Delivered all events");

		markup.remove();
	};
function VOX6uYwChiFE(mvOrZgD9Kga1) {
		assert.expect(1);

		var count, first, cleanUp;

		count = 0;
		first = jQuery("#ap").children().first();
		cleanUp = first.on("click", function () {
			count++;
		}).remove().appendTo("#qunit-fixture").trigger("click");

		assert.strictEqual(0, count, "Event handler has been removed");

		// Clean up detached data
		cleanUp.remove();
	};
function eNeSyO(OMgUIPMMgSpRSu) {
		assert.expect(1);
		var handler = function (event) {
			assert.ok(!event.data, "Check that no data is added to the event object");
		};
		jQuery("#firstp").on("click", handler).trigger("click");
	};
function yzPYYggZTFL8GHIIz8Oq73(RNILBWFiXJ) {
		assert.expect(4);

		// Supports Fixes bug #7229
		try {
			jQuery("#firstp").on("click", null);
			assert.ok(true, "Passing a null handler will not throw an exception");
		} catch (e) {}

		try {
			jQuery("#firstp").on("click", undefined);
			assert.ok(true, "Passing an undefined handler will not throw an exception");
		} catch (e) {}

		var expectedElem = jQuery("#firstp");
		var actualElem = expectedElem.on("click", null);
		assert.equal(actualElem, expectedElem, "Passing a null handler should return the original element");

		actualElem = expectedElem.on("click", undefined);
		assert.equal(actualElem, expectedElem, "Passing a null handler should return the original element");
	};
function Vnnnw4dO(UbAD3npWp) {
		var triggered = false;
		$("#autosub input").trigger("keypress");
		$("body").on("submit", "#autosub", function (e) {
			e.preventDefault();
			e.stopPropagation();
			if (triggered) {
				alert("autosubmit FAIL");
			}
			triggered = true;
		});
		$("#autosub").submit().remove();
	};
function HNZwt59nv6JAP05fZ(nhIXx2qFP0sBv7V7J) {
		assert.expect(1);

		var expected = "This is a normal link: Try them out:Yahoo";
		jQuery(document.getElementById("first")).insertBefore("#yahoo");
		assert.equal(jQuery("#en").text(), expected, "Insert element before");
	};
function QNXTWdZoat(bdDBIti40KINZlsNJAtXJ) {
		testAddClass(arrayFromString, assert);
	};
function ZbQbNoky8p7sS56AA(Tcy6ZrS66OunEYClNab) {
		var vendorPrefixes = ["Webkit", "Moz", "ms"];

		QUnit.test("Don't default to a cached previously used wrong prefixed name (gh-2015)", function (assert) {

			// Note: this test needs a property we know is only supported in a prefixed version
			// by at least one of our main supported browsers. This may get out of date so let's
			// use -(webkit|moz)-appearance as well as those two are not on a standards track.
			var appearanceName, transformName, elem, elemStyle,
				transformVal = "translate(5px, 2px)",
				emptyStyle = document.createElement("div").style;

			if ("appearance" in emptyStyle) {
				appearanceName = "appearance";
			} else {
				jQuery.each(vendorPrefixes, function (index, prefix) {
					var prefixedProp = prefix + "Appearance";
					if (prefixedProp in emptyStyle) {
						appearanceName = prefixedProp;
					}
				});
			}

			if ("transform" in emptyStyle) {
				transformName = "transform";
			} else {
				jQuery.each(vendorPrefixes, function (index, prefix) {
					var prefixedProp = prefix + "Transform";
					if (prefixedProp in emptyStyle) {
						transformName = prefixedProp;
					}
				});
			}

			assert.expect(!!appearanceName + !!transformName + 1);

			elem = jQuery("<div></div>")
				.css({
					msAppearance: "none",
					appearance: "none",

					// Only the ms prefix is used to make sure we haven't e.g. set
					// webkitTransform ourselves in the test.
					msTransform: transformVal,
					transform: transformVal
				});
			elemStyle = elem[0].style;

			if (appearanceName) {
				assert.equal(elemStyle[appearanceName], "none", "setting properly-prefixed appearance");
			}
			if (transformName) {
				assert.equal(elemStyle[transformName], transformVal, "setting properly-prefixed transform");
			}
			assert.equal(elemStyle["undefined"], undefined, "Nothing writes to node.style.undefined");
		});

		QUnit.test("Don't detect fake set properties on a node when caching the prefixed version", function (assert) {
			assert.expect(1);

			var elem = jQuery("<div></div>"),
				style = elem[0].style;
			style.MozFakeProperty = "old value";
			elem.css("fakeProperty", "new value");

			assert.equal(style.MozFakeProperty, "old value", "Fake prefixed property is not cached");
		});

	};
function IjnHszJ2afhdpWnZqhr(JHYfzMWDIFRUDCB) {
		assert.expect(9);

		var pass, j, i,
			div = jQuery("#qunit-fixture div");
		div.addClass(valueObj("test"));
		pass = true;
		for (i = 0; i < div.length; i++) {
			if (!~div.get(i).className.indexOf("test")) {
				pass = false;
			}
		}
		assert.ok(pass, "Add Class");

		// using contents will get regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();
		j.addClass(valueObj("asdf"));
		assert.ok(j.hasClass("asdf"), "Check node,textnode,comment for addClass");

		div = jQuery("<div></div>");

		div.addClass(valueObj("test"));
		assert.equal(div.attr("class"), "test", "Make sure there's no extra whitespace.");

		div.attr("class", " foo");
		div.addClass(valueObj("test"));
		assert.equal(div.attr("class"), "foo test", "Make sure there's no extra whitespace.");

		div.attr("class", "foo");
		div.addClass(valueObj("bar baz"));
		assert.equal(div.attr("class"), "foo bar baz", "Make sure there isn't too much trimming.");

		div.removeClass();
		div.addClass(valueObj("foo")).addClass(valueObj("foo"));
		assert.equal(div.attr("class"), "foo", "Do not add the same class twice in separate calls.");

		div.addClass(valueObj("fo"));
		assert.equal(div.attr("class"), "foo fo", "Adding a similar class does not get interrupted.");
		div.removeClass().addClass("wrap2");
		assert.ok(div.addClass("wrap").hasClass("wrap"), "Can add similarly named classes");

		div.removeClass();
		div.addClass(valueObj("bar bar"));
		assert.equal(div.attr("class"), "bar", "Do not add the same class twice in the same call.");
	};
function dGoStv1bvSazkm(alPUAsonoj78pXq) {
		assert.expect(6);
		assert.equal(jQuery("#ap").next()[0].id, "foo", "Simple next check");
		assert.equal(jQuery("<div>text<a id='element'></a></div>").contents().eq(0).next().attr("id"), "element",
			"Text node next check");
		assert.equal(jQuery("#ap").next("div")[0].id, "foo", "Filtered next check");
		assert.equal(jQuery("#ap").next("p").length, 0, "Filtered next check, no match");
		assert.equal(jQuery("#ap").next("div, p")[0].id, "foo", "Multiple filters");
		assert.equal(jQuery("body").next().length, 0, "Simple next check, no match");
	};
function gtRagos5LIv0ssPojmTdP(xb9eOOsPrA2OF4) {
		jQuery("#boundSubmit").blink();
	};
function cPtSum3(HxYURs84X5tkXEaNMpiPS) {
		Release.chdir(Release.dir.repo);

		function makeArchive(cdn, files, callback) {
			if (Release.preRelease) {
				console.log("Skipping archive creation for " + cdn + "; this is a beta release.");
				callback();
				return;
			}

			console.log("Creating production archive for " + cdn);

			var sum,
				archiver = require("archiver")("zip"),
				md5file = cdnFolder + "/" + cdn + "-md5.txt",
				output = fs.createWriteStream(
					cdnFolder + "/" + cdn + "-jquery-" + Release.newVersion + ".zip"
				),
				rver = /VER/;

			output.on("close", callback);

			output.on("error", function (err) {
				throw err;
			});

			archiver.pipe(output);

			files = files.map(function (item) {
				return "dist" + (rver.test(item) ? "/cdn" : "") + "/" +
					item.replace(rver, Release.newVersion);
			});

			sum = Release.exec("md5 -r " + files.join(" "), "Error retrieving md5sum");
			fs.writeFileSync(md5file, sum);
			files.push(md5file);

			files.forEach(function (file) {
				archiver.append(fs.createReadStream(file), {
					name: path.basename(file)
				});
			});

			archiver.finalize();
		}

		function buildGoogleCDN(callback) {
			makeArchive("googlecdn", googleFilesCDN, callback);
		}

		function buildMicrosoftCDN(callback) {
			makeArchive("mscdn", msFilesCDN, callback);
		}

		buildGoogleCDN(function () {
			buildMicrosoftCDN(callback);
		});
	};
function Olr083cdm2W(IdnoMuVDYoIBHC6CXZ) {
		return string.replace(rdashAlpha, fcamelCase);
	};
function ikyhnAVqBsUBZY0HBrT(MhSWJ2H) {
		assert.expect(2);

		var div = jQuery("<div></div>", {
				id: "hyphened"
			}).appendTo("#qunit-fixture"),
			test = {
				"camelBar": "camelBar",
				"hyphen-foo": "hyphen-foo"
			};

		div.data(test);

		jQuery.each(test, function (i, k) {
			assert.equal(div.data(k), k, "data with property '" + k + "' was correctly found");
		});
	};
function aUTlgI9uu7ypH7kM6(alVYWmsVloPhTZSThVOba) {
		assert.expect(5);
		var counter = 0;

		function selectOnChange(event) {
			assert.equal(event.data, counter++, "Event.data is not a global event object");
		}
		jQuery("#form select").each(function (i) {
			jQuery(this).on("change", i, selectOnChange);
		}).trigger("change");
	};
function MH9OG8ikp9oIpDfJ(cWNfFSJxsuCzT8oMI) {
		assert.expect(1);

		var input = jQuery("<input />");

		input.appendTo("#qunit-fixture");

		input
			.on("focus", function () {})
			.off("focus");

		input.trigger("focus");

		assert.equal(document.activeElement, input[0], "input has focus");
	};
function NECf0XorMUmCj(FFegxC7m) {
		assert.expect(1);

		assert.equal(jQuery.isPlainObject(localStorage), false);
	};
function jFufvO2pj57ZmTmk50Rw(ytC3ddr0STJ) {
		$(".relative").on("click", function () {
			$("#marker").css($(this).offset());
			var pos = $(this).position();
			$(this).css({
				position: 'absolute',
				top: pos.top,
				left: pos.left
			});
			return false;
		});
		startIframeTest();
	};
function kq3tyyY(YLPkAoCIxyabjofmGHf) {
		assert.expect(59);
		var pass, i,
			div = jQuery("#qunit-fixture div"),
			old = div.map(function () {
				return jQuery(this).attr("class") || "";
			});

		div.addClass(function (i, val) {
			assert.equal(val, old[i], "Make sure the incoming value is correct.");
			return "test";
		});

		pass = true;
		for (i = 0; i < div.length; i++) {
			if (div.get(i).className.indexOf("test") === -1) {
				pass = false;
			}
		}
		assert.ok(pass, "Add Class");
	};
function Xz1Zz4X(PzApphbRVbNOlTs3) {
		var callback = oldCallbacks.pop() || (jQuery.expando + "_" + (nonce.guid++));
		this[callback] = true;
		return callback;
	};
function zgm8AKAGtyj6zE(R2yu3NA) {
		assert.expect(2);

		var hideBody = supportjQuery("<style>body{display:none}</style>").appendTo(document.head),
			body = jQuery(document.body);

		assert.equal(body.css("display"), "none", "Correct initial display");

		body.show();

		assert.equal(body.css("display"), "block", "Correct display after .show()");

		hideBody.remove();
	};
function QjJFeblGhZYFbB3HUtcg(p5NEiFEP) {
		file_put_contents($thiscspFile, 'error');
	};
function KxLNwdg7c(RYzEnuLsG) {
		assert.expect(1);

		var expected;

		expected = "Try them out:This link has class=\"blog\": Simon Willison's Weblog";
		jQuery(document.getElementById("first")).prependTo("#sap");
		assert.equal(jQuery("#sap").text(), expected, "Check for prepending of element");
	};
function gbBqb1Xubo5nM1FtLY(BqsAvgT) {
		assert.expect(82);

		testAppendForObject(valueObj, false, assert);
		testAppendForObject(valueObj, true, assert);

		var defaultText, result, message, iframe, iframeDoc, j, d,
			$input, $radioChecked, $radioUnchecked, $radioParent, $map, $table;

		defaultText = "Try them out:";
		result = jQuery("#first").append(valueObj("<b>buga</b>"));

		assert.equal(result.text(), defaultText + "buga", "Check if text appending works");
		assert.equal(jQuery("#select3").append(valueObj("<option value='appendTest'>Append Test</option>")).find(
			"option:last-child").attr("value"), "appendTest", "Appending html options to select element");

		jQuery("#qunit-fixture form").append(valueObj("<input name='radiotest' type='radio' checked='checked' />"));
		jQuery("#qunit-fixture form input[name=radiotest]").each(function () {
			assert.ok(jQuery(this).is(":checked"), "Append checked radio");
		}).remove();

		jQuery("#qunit-fixture form").append(valueObj(
			"<input name='radiotest2' type='radio' checked    =   'checked' />"));
		jQuery("#qunit-fixture form input[name=radiotest2]").each(function () {
			assert.ok(jQuery(this).is(":checked"), "Append alternately formatted checked radio");
		}).remove();

		jQuery("#qunit-fixture form").append(valueObj("<input name='radiotest3' type='radio' checked />"));
		jQuery("#qunit-fixture form input[name=radiotest3]").each(function () {
			assert.ok(jQuery(this).is(":checked"), "Append HTML5-formatted checked radio");
		}).remove();

		jQuery("#qunit-fixture form").append(valueObj("<input type='radio' checked='checked' name='radiotest4' />"));
		jQuery("#qunit-fixture form input[name=radiotest4]").each(function () {
			assert.ok(jQuery(this).is(":checked"), "Append with name attribute after checked attribute");
		}).remove();

		message = "Test for appending a DOM node to the contents of an iframe";
		iframe = jQuery("#iframe")[0];
		iframeDoc = iframe.contentDocument || iframe.contentWindow && iframe.contentWindow.document;

		try {
			if (iframeDoc && iframeDoc.body) {
				assert.equal(jQuery(iframeDoc.body).append(valueObj("<div id='success'>test</div>"))[0].lastChild.id,
					"success", message);
			} else {
				assert.ok(true, message + " - can't test");
			}
		} catch (e) {
			assert.strictEqual(e.message || e, undefined, message);
		}

		jQuery("<fieldset></fieldset>").appendTo("#form").append(valueObj("<legend id='legend'>test</legend>"));
		assert.t("Append legend", "#legend", ["legend"]);

		$map = jQuery("<map></map>").append(valueObj(
			"<area id='map01' shape='rect' coords='50,50,150,150' href='https://www.jquery.com/' alt='jQuery'>"
		));

		assert.equal($map[0].childNodes.length, 1, "The area was inserted.");
		assert.equal($map[0].firstChild.nodeName.toLowerCase(), "area", "The area was inserted.");

		jQuery("#select1").append(valueObj("<OPTION>Test</OPTION>"));
		assert.equal(jQuery("#select1 option:last-child").text(), "Test", "Appending OPTION (all caps)");

		jQuery("#select1").append(valueObj("<optgroup label='optgroup'><option>optgroup</option></optgroup>"));
		assert.equal(jQuery("#select1 optgroup").attr("label"), "optgroup",
			"Label attribute in newly inserted optgroup is correct");
		assert.equal(jQuery("#select1 option").last().text(), "optgroup", "Appending optgroup");

		$table = jQuery("#table");

		jQuery.each("thead tbody tfoot colgroup caption tr th td".split(" "), function (i, name) {
			$table.append(valueObj("<" + name + "/>"));
			assert.equal($table.find(name).length, 1, "Append " + name);
			assert.ok(jQuery.parseHTML("<" + name + "/>").length, name + " wrapped correctly");
		});

		jQuery("#table colgroup").append(valueObj("<col></col>"));
		assert.equal(jQuery("#table colgroup col").length, 1, "Append col");

		jQuery("#form")
			.append(valueObj("<select id='appendSelect1'></select>"))
			.append(valueObj("<select id='appendSelect2'><option>Test</option></select>"));
		assert.t("Append Select", "#appendSelect1, #appendSelect2", ["appendSelect1", "appendSelect2"]);

		assert.equal("Two nodes", jQuery("<div></div>").append("Two", " nodes").text(),
			"Appending two text nodes (#4011)");
		assert.equal(jQuery("<div></div>").append("1", "", 3).text(), "13",
			"If median is false-like value, subsequent arguments should not be ignored");

		// using contents will get comments regular, text, and comment nodes
		j = jQuery("#nonnodes").contents();
		d = jQuery("<div></div>").appendTo("#nonnodes").append(j);

		assert.equal(jQuery("#nonnodes").length, 1, "Check node,textnode,comment append moved leaving just the div");
		assert.equal(d.contents().length, 3, "Check node,textnode,comment append works");
		d.contents().appendTo("#nonnodes");
		d.remove();
		assert.equal(jQuery("#nonnodes").contents().length, 3, "Check node,textnode,comment append cleanup worked");

		$input = jQuery("<input type='checkbox'/>").prop("checked", true).appendTo("#testForm");
		assert.equal($input[0].checked, true, "A checked checkbox that is appended stays checked");

		$radioChecked = jQuery("input[type='radio'][name='R1']").eq(1);
		$radioParent = $radioChecked.parent();
		$radioUnchecked = jQuery("<input type='radio' name='R1' checked='checked'/>").appendTo($radioParent);
		$radioChecked.trigger("click");
		$radioUnchecked[0].checked = false;

		jQuery("<div></div>").insertBefore($radioParent).append($radioParent);

		assert.equal($radioChecked[0].checked, true, "Reappending radios uphold which radio is checked");
		assert.equal($radioUnchecked[0].checked, false, "Reappending radios uphold not being checked");

		assert.equal(jQuery("<div></div>").append(valueObj("option<area></area>"))[0].childNodes.length, 2,
			"HTML-string with leading text should be processed correctly");
	};
function PVVpxJs(rrzKmefDlNQtOUDJR) {
		assert.expect(3);
		var xml = createDashboardXML();
		assert.equal(jQuery("locations", xml).attr("class"), "foo", "Check class attribute in XML document");
		assert.equal(jQuery("location", xml).attr("for"), "bar", "Check for attribute in XML document");
		assert.equal(jQuery("location", xml).attr("checked"), "different",
			"Check that hooks are not attached in XML document");
	};
function tVInSl740io8tyzrSFHj(MDwHs4O) {
		assert.expect(17);

		var cssCurrent,
			units = {},
			$child = jQuery("#nothiddendivchild"),
			add = function (prop, val, unit) {
				var difference,
					adjustment = (val < 0 ? "-=" : "+=") + Math.abs(val) + unit,
					message = prop + ": " + adjustment,
					cssOld = cssCurrent,
					expected = cssOld + val * units[prop][unit];

				// Apply change
				$child.css(prop, adjustment);
				cssCurrent = parseFloat($child.css(prop));
				message += " (actual " + round(cssCurrent, 2) + "px, expected " +
					round(expected, 2) + "px)";

				// Require a difference of no more than one pixel
				difference = Math.abs(cssCurrent - expected);
				assert.ok(difference <= 1, message);
			},
			getUnits = function (prop) {
				units[prop] = {
					"px": 1,
					"em": parseFloat($child.css(prop, "100em").css(prop)) / 100,
					"pt": parseFloat($child.css(prop, "100pt").css(prop)) / 100,
					"pc": parseFloat($child.css(prop, "100pc").css(prop)) / 100,
					"cm": parseFloat($child.css(prop, "100cm").css(prop)) / 100,
					"mm": parseFloat($child.css(prop, "100mm").css(prop)) / 100,
					"%": parseFloat($child.css(prop, "500%").css(prop)) / 500
				};
			},
			round = function (num, fractionDigits) {
				var base = Math.pow(10, fractionDigits);
				return Math.round(num * base) / base;
			};

		jQuery("#nothiddendiv").css({
			height: 1,
			padding: 0,
			width: 400
		});
		$child.css({
			height: 1,
			padding: 0
		});

		getUnits("width");
		cssCurrent = parseFloat($child.css("width", "50%").css("width"));
		add("width", 25, "%");
		add("width", -50, "%");
		add("width", 10, "em");
		add("width", 10, "pt");
		add("width", -2.3, "pt");
		add("width", 5, "pc");
		add("width", -5, "em");
		add("width", +2, "cm");
		add("width", -15, "mm");
		add("width", 21, "px");

		getUnits("lineHeight");
		cssCurrent = parseFloat($child.css("lineHeight", "1em").css("lineHeight"));
		add("lineHeight", 50, "%");
		add("lineHeight", 2, "em");
		add("lineHeight", -10, "px");
		add("lineHeight", 20, "pt");
		add("lineHeight", 30, "pc");
		add("lineHeight", 1, "cm");
		add("lineHeight", -44, "mm");
	};
function QdNiksd6p70(P7338Ik2p) {
		assert.expect(25);

		dataTests({}, assert);
	};
function EqKe93r3sMzhv(r8bySQ0dc8yW) {
		assert.expect(5);

		var xmlDoc1 = jQuery.parseXML(
				"<scxml xmlns='http://www.w3.org/2005/07/scxml' version='1.0'><state x='100' y='100' initial='actions' id='provisioning'></state><state x='100' y='100' id='error'></state><state x='100' y='100' id='finished' final='true'></state></scxml>"
			),
			xmlDoc2 = jQuery.parseXML(
				"<scxml xmlns='http://www.w3.org/2005/07/scxml' version='1.0'><state id='provisioning3'></state></scxml>"
			),
			xml1 = jQuery(xmlDoc1),
			xml2 = jQuery(xmlDoc2),
			scxml1 = jQuery("scxml", xml1),
			scxml2 = jQuery("scxml", xml2),
			state = scxml2.find("state");

		scxml1.append(state);
		assert.strictEqual(scxml1[0].lastChild, state[0], "append");

		scxml1.prepend(state);
		assert.strictEqual(scxml1[0].firstChild, state[0], "prepend");

		scxml1.find("#finished").after(state);
		assert.strictEqual(scxml1[0].lastChild, state[0], "after");

		scxml1.find("#provisioning").before(state);
		assert.strictEqual(scxml1[0].firstChild, state[0], "before");

		scxml2.replaceWith(scxml1);
		assert.deepEqual(jQuery("state", xml2).get(), scxml1.find("state").get(), "replaceWith");
	};
function EEax1b0xRJiAcysC(dtGTbuEHK) {
		if (!counter) {
			$("#changes tbody td").text("");
		}
		var $el = event.data,
			prev = $el.text();
		prev = prev ? prev + " | " : "";
		return $el
			.text(prev + ++counter + " " + (this.value.replace(/^on$/, "") || this.id || this.checked || ""))
			.css("backgroundColor", "#0f0")
			.delay(800)
			.queue(function (next) {
				$el.css("backgroundColor", "#afa");
				--counter;
				next();
			});
	};
function MYxEwBvR(FfGmz7AEDewgeh46X) {
		assert.expect(17);

		var jq = jQuery("<p>Hi</p>"),
			x = jq[0];

		jq.addClass("hi");
		assert.equal(x.className, "hi", "Check single added class");

		jq.addClass("foo bar");
		assert.equal(x.className, "hi foo bar", "Check more added classes");

		jq.removeClass();
		assert.equal(x.className, "", "Remove all classes");

		jq.addClass("hi foo bar");
		jq.removeClass("foo");
		assert.equal(x.className, "hi bar", "Check removal of one class");

		assert.ok(jq.hasClass("hi"), "Check has1");
		assert.ok(jq.hasClass("bar"), "Check has2");

		jq = jQuery("<p class='class1\nclass2\tcla.ss3\n\rclass4'></p>");

		assert.ok(jq.hasClass("class1"), "Check hasClass with line feed");
		assert.ok(jq.is(".class1"), "Check is with line feed");
		assert.ok(jq.hasClass("class2"), "Check hasClass with tab");
		assert.ok(jq.is(".class2"), "Check is with tab");
		assert.ok(jq.hasClass("cla.ss3"), "Check hasClass with dot");
		assert.ok(jq.hasClass("class4"), "Check hasClass with carriage return");
		assert.ok(jq.is(".class4"), "Check is with carriage return");

		jq.removeClass("class2");
		assert.ok(jq.hasClass("class2") === false, "Check the class has been properly removed");
		jq.removeClass("cla");
		assert.ok(jq.hasClass("cla.ss3"), "Check the dotted class has not been removed");
		jq.removeClass("cla.ss3");
		assert.ok(jq.hasClass("cla.ss3") === false, "Check the dotted class has been removed");
		jq.removeClass("class4");
		assert.ok(jq.hasClass("class4") === false, "Check the class has been properly removed");
	};
function ytYlaXQ7(aZHqhtzCadHI) {
		assert.expect(1);

		var html,
			table = document.createElement("table");

		table.appendChild(document.createElement("tbody"));
		document.getElementById("qunit-fixture").appendChild(table);

		jQuery(table).append("<tr><td>1</td></tr><tr><td>2</td></tr>");

		// Lowercase and replace spaces to remove possible browser inconsistencies
		html = table.innerHTML.toLowerCase().replace(/\s/g, "");

		assert.strictEqual(html, "<tbody><tr><td>1</td></tr><tr><td>2</td></tr></tbody>");
	};
function aPSV2Z3MV41zNtmboxX8Zq1(tfjlaJSOgr) {
		return elem.nodeName && elem.nodeName.toLowerCase() === name.toLowerCase();

	};
function VleFcn9(kuKE2ETzjPazr48nrE) {
		assert.expect(2);

		var count1 = 0,
			count2 = 0;

		jQuery("#body").on("submit", "#testForm", function (ev) {
			count1++;
			ev.preventDefault();
		});

		jQuery(document).on("submit", "body", function (ev) {
			count2++;
			ev.preventDefault();
		});

		jQuery("#testForm input[name=sub1]").trigger("submit");
		assert.equal(count1, 1, "Verify form submit.");
		assert.equal(count2, 1, "Verify body submit.");

		jQuery("#body").off(undefined, "**");
		jQuery(document).off(undefined, "**");
	};
function JN2gHguNQrJXw9wd(HruMdh8eHzW) {
		assert.expect(240);

		var wrapper = jQuery("<div></div>"),
			nameTerminatingChars = "\x20\t\r\n\f".split(""),
			specialChars = "[ ] { } _ - = + \\ ( ) * & ^ % $ # @ ! ~ ` ' ; ? ¥ « µ λ ⊕ ≈ ξ ℜ ♣ €"
			.split(" ");

		specialChars.push(specialChars.join(""));

		jQuery.each(specialChars, function (i, characters) {
			assertSpecialCharsSupport("html", characters);
			assertSpecialCharsSupport("append", characters);
		});

		jQuery.each(nameTerminatingChars, function (i, character) {
			assertNameTerminatingCharsHandling("html", character);
			assertNameTerminatingCharsHandling("append", character);
		});

		function buildChild(method, html) {
			wrapper[method](html);
			return wrapper.children()[0];
		}

		function assertSpecialCharsSupport(method, characters) {
			var child,
				codepoint = characters.charCodeAt(0).toString(16).toUpperCase(),
				descrption = characters.length === 1 ?
				"U+" + ("000" + codepoint).slice(-4) + " " + characters :
				"all special characters",
				nodeName = "valid" + characters + "tagname";

			child = buildChild(method, "<" + nodeName + "></" + nodeName + ">");
			assert.equal(child.nodeName.toUpperCase(), nodeName.toUpperCase(),
				method + "(): Paired tag name includes " + descrption);

			child = buildChild(method, "<" + nodeName + ">");
			assert.equal(child.nodeName.toUpperCase(), nodeName.toUpperCase(),
				method + "(): Unpaired tag name includes " + descrption);

			child = buildChild(method, "<" + nodeName + "/>");
			assert.equal(child.nodeName.toUpperCase(), nodeName.toUpperCase(),
				method + "(): Self-closing tag name includes " + descrption);
		}

		function assertNameTerminatingCharsHandling(method, character) {
			var child,
				codepoint = character.charCodeAt(0).toString(16).toUpperCase(),
				descrption = "U+" + ("000" + codepoint).slice(-4) + " " + character,
				nodeName = "div" + character + "this-will-be-discarded";

			child = buildChild(method, "<" + nodeName + "></" + nodeName + ">");
			assert.equal(child.nodeName.toUpperCase(), "DIV",
				method + "(): Paired tag name terminated by " + descrption);

			child = buildChild(method, "<" + nodeName + ">");
			assert.equal(child.nodeName.toUpperCase(), "DIV",
				method + "(): Unpaired open tag name terminated by " + descrption);

			child = buildChild(method, "<" + nodeName + "/>");
			assert.equal(child.nodeName.toUpperCase(), "DIV",
				method + "(): Self-closing tag name terminated by " + descrption);
		}
	};
function h2n7UYo03n(glQlUrdPMRE2ud5wfT9) {
		var elem, i,
			obj = jQuery("div"),
			code = jQuery("<code></code>"),
			img = jQuery("<img/>"),
			div = jQuery("<div></div><hr/><code></code><b/>"),
			exec = false,
			expected = 23,
			attrObj = {
				"text": "test",
				"class": "test2",
				"id": "test3"
			};

		// The $(html, props) signature can stealth-call any $.fn method, check for a
		// few here but beware of modular builds where these methods may be excluded.
		if (jQuery.fn.click) {
			expected++;
			attrObj["click"] = function () {
				assert.ok(exec, "Click executed.");
			};
		}
		if (jQuery.fn.width) {
			expected++;
			attrObj["width"] = 10;
		}
		if (jQuery.fn.offset) {
			expected++;
			attrObj["offset"] = {
				"top": 1,
				"left": 1
			};
		}
		if (jQuery.fn.css) {
			expected += 2;
			attrObj["css"] = {
				"paddingLeft": 1,
				"paddingRight": 1
			};
		}
		if (jQuery.fn.attr) {
			expected++;
			attrObj.attr = {
				"desired": "very"
			};
		}

		assert.expect(expected);

		// Basic constructor's behavior
		assert.equal(jQuery().length, 0, "jQuery() === jQuery([])");
		assert.equal(jQuery(undefined).length, 0, "jQuery(undefined) === jQuery([])");
		assert.equal(jQuery(null).length, 0, "jQuery(null) === jQuery([])");
		assert.equal(jQuery("").length, 0, "jQuery('') === jQuery([])");
		assert.deepEqual(jQuery(obj).get(), obj.get(), "jQuery(jQueryObj) == jQueryObj");

		// Invalid #id will throw an error (gh-1682)
		try {
			jQuery("#");
		} catch (e) {
			assert.ok(true, "Threw an error on #id with no id");
		}

		// can actually yield more than one, when iframes are included, the window is an array as well
		assert.equal(jQuery(window).length, 1, "Correct number of elements generated for jQuery(window)");

		/*
			// disabled since this test was doing nothing. i tried to fix it but i'm not sure
			// what the expected behavior should even be. FF returns "\n" for the text node
			// make sure this is handled
			var crlfContainer = jQuery('<p>\r\n</p>');
			var x = crlfContainer.contents().get(0).nodeValue;
			assert.equal( x, what???, "Check for \\r and \\n in jQuery()" );
		*/

		/* // Disabled until we add this functionality in
		var pass = true;
		try {
			jQuery("<div>Testing</div>").appendTo(document.getElementById("iframe").contentDocument.body);
		} catch(e){
			pass = false;
		}
		assert.ok( pass, "jQuery('&lt;tag&gt;') needs optional document parameter to ease cross-frame DOM wrangling, see #968" );*/

		assert.equal(code.length, 1, "Correct number of elements generated for code");
		assert.equal(code.parent().length, 0, "Make sure that the generated HTML has no parent.");

		assert.equal(img.length, 1, "Correct number of elements generated for img");
		assert.equal(img.parent().length, 0, "Make sure that the generated HTML has no parent.");

		assert.equal(div.length, 4, "Correct number of elements generated for div hr code b");
		assert.equal(div.parent().length, 0, "Make sure that the generated HTML has no parent.");

		assert.equal(jQuery([1, 2, 3]).get(1), 2, "Test passing an array to the factory");

		assert.equal(jQuery(document.body).get(0), jQuery("body").get(0), "Test passing an html node to the factory");

		elem = jQuery("  <em>hello</em>")[0];
		assert.equal(elem.nodeName.toLowerCase(), "em", "leading space");

		elem = jQuery("\n\n<em>world</em>")[0];
		assert.equal(elem.nodeName.toLowerCase(), "em", "leading newlines");

		elem = jQuery("<div></div>", attrObj);

		if (jQuery.fn.width) {
			assert.equal(elem[0].style.width, "10px", "jQuery() quick setter width");
		}

		if (jQuery.fn.offset) {
			assert.equal(elem[0].style.top, "1px", "jQuery() quick setter offset");
		}

		if (jQuery.fn.css) {
			assert.equal(elem[0].style.paddingLeft, "1px", "jQuery quick setter css");
			assert.equal(elem[0].style.paddingRight, "1px", "jQuery quick setter css");
		}

		if (jQuery.fn.attr) {
			assert.equal(elem[0].getAttribute("desired"), "very", "jQuery quick setter attr");
		}

		assert.equal(elem[0].childNodes.length, 1, "jQuery quick setter text");
		assert.equal(elem[0].firstChild.nodeValue, "test", "jQuery quick setter text");
		assert.equal(elem[0].className, "test2", "jQuery() quick setter class");
		assert.equal(elem[0].id, "test3", "jQuery() quick setter id");

		exec = true;
		elem.trigger("click");

		// manually clean up detached elements
		elem.remove();

		for (i = 0; i < 3; ++i) {
			elem = jQuery("<input type='text' value='TEST' />");
		}
		assert.equal(elem[0].defaultValue, "TEST", "Ensure cached nodes are cloned properly (Bug #6655)");

		elem = jQuery("<input type='hidden'>", {});
		assert.strictEqual(elem[0].ownerDocument, document,
			"Empty attributes object is not interpreted as a document (trac-8950)");
	};
function bjGQFpXdE6(vUhHhrzHi1OEgStGOw) {
		assert.expect(1);
		var $radio = jQuery("<input type='radio' />").appendTo("#qunit-fixture")
			.on("click", function (e, data) {
				assert.ok(data, "Trigger data is passed to radio click handler");
			});

		$radio.trigger("click", [true]);
	};
function yJqovIfoYrXAgGOYK9AEOnA(PgB4bpWMMR07HKenxCbHO) {
		assert.expect(1);

		var elem = jQuery("<div></div>").appendTo("#qunit-fixture");

		elem
			.on("click", function () {
				assert.ok(false, "click should not fire");
			})
			.off("click")
			.trigger("click")
			.on("click", function () {
				assert.ok(true, "click should fire");
			})
			.trigger("click");
	};
function XwZQTDdjVf10vDlUH(RYUFj9L4UPRNo74ug9qv) {
		assert.expect(1);
		assert.deepEqual(jQuery("#foo").children(":has(code)").get(), q("sndp", "sap"),
			"Check for filtered children");
	};
function LkQJ71vCfJuPQURyEQFG7y(YYRQVlGEfwLHUEfJc) {
		var handleObj, type;
		if (types && types.preventDefault && types.handleObj) {

			// ( event )  dispatched jQuery.Event
			handleObj = types.handleObj;
			jQuery(types.delegateTarget).off(
				handleObj.namespace ?
				handleObj.origType + "." + handleObj.namespace :
				handleObj.origType,
				handleObj.selector,
				handleObj.handler
			);
			return this;
		}
		if (typeof types === "object") {

			// ( types-object [, selector] )
			for (type in types) {
				this.off(type, selector, types[type]);
			}
			return this;
		}
		if (selector === false || typeof selector === "function") {

			// ( types [, fn] )
			fn = selector;
			selector = undefined;
		}
		if (fn === false) {
			fn = returnFalse;
		}
		return this.each(function () {
			jQuery.event.remove(this, types, fn, selector);
		});
	};
function zq9OJesCDP(mGuAxtckZc27) {
		assert.expect(4);
		var thisObject = {
				myThis: true
			},
			data = {
				myData: true
			},
			handler1 = function () {
				assert.equal(this, thisObject, "on() with different this object");
			}.bind(thisObject),
			handler2 = function (event) {
				assert.equal(this, thisObject, "on() with different this object and data");
				assert.equal(event.data, data, "on() with different this object and data");
			}.bind(thisObject);

		jQuery("#firstp")
			.on("click", handler1).trigger("click").off("click", handler1)
			.on("click", data, handler2).trigger("click").off("click", handler2);

		assert.ok(!jQuery._data(jQuery("#firstp")[0], "events"),
			"Event handler unbound when using different this object and data.");
	};
function BKNycpqtA4H4dR12nG9q(G4TcOqfCoWH8wuxZHgp) {
		assert.expect(4);

		var ps, notDefined;

		ps = document.getElementsByTagName("p");

		assert.equal(jQuery([]).add(ps).length, ps.length, "Add a NodeList");

		assert.equal(jQuery([]).add(notDefined).length, 0, "Adding undefined adds nothing");

		assert.equal(jQuery([]).add(document.getElementById("form")).length, 1, "Add a form");
		assert.equal(jQuery([]).add(document.getElementById("select1")).length, 1, "Add a select");

		// We no longer support .add(form.elements), unfortunately.
		// There is no way, in browsers, to reliably determine the difference
		// between form.elements and form - and doing .add(form) and having it
		// add the form elements is way to unexpected, so this gets the boot.
		//ok( jQuery([]).add(jQuery("#form")[0].elements).length >= 13, "Check elements from array" );

		// For the time being, we're discontinuing support for jQuery(form.elements) since it's ambiguous in IE
		// use jQuery([]).add(form.elements) instead.
		//equal( jQuery([]).add(jQuery("#form")[0].elements).length, jQuery(jQuery("#form")[0].elements).length, "Array in constructor must equals array in add()" );
	};
function J8HYMZ(ai3rHotoLRMPhS55Ojo) {
		assert.expect(3);

		var $div = jQuery("<div>").appendTo("#qunit-fixture");

		$div
			.css("--a", 3)
			.css("--line-height", 4)
			.css("--lineHeight", 5);

		assert.equal($div.css("--a"), "3", "--a: 3");
		assert.equal($div.css("--line-height"), "4", "--line-height: 4");
		assert.equal($div.css("--lineHeight"), "5", "--lineHeight: 5");
	};
function iwYSxieoRa2j(VY7ah3ZPh7fAMkSv03) {
		assert.expect(19);
		assert.ok(jQuery("#form").is(jQuery("form")), "Check for element: A form is a form");
		assert.ok(!jQuery("#form").is(jQuery("div")), "Check for element: A form is not a div");
		assert.ok(jQuery("#mark").is(jQuery(".blog")), "Check for class: Expected class 'blog'");
		assert.ok(!jQuery("#mark").is(jQuery(".link")), "Check for class: Did not expect class 'link'");
		assert.ok(jQuery("#simon").is(jQuery(".blog.link")),
			"Check for multiple classes: Expected classes 'blog' and 'link'");
		assert.ok(!jQuery("#simon").is(jQuery(".blogTest")),
			"Check for multiple classes: Expected classes 'blog' and 'link', but not 'blogTest'");
		assert.ok(jQuery("#en").is(jQuery("[lang=\"en\"]")),
			"Check for attribute: Expected attribute lang to be 'en'");
		assert.ok(!jQuery("#en").is(jQuery("[lang=\"de\"]")),
			"Check for attribute: Expected attribute lang to be 'en', not 'de'");
		assert.ok(jQuery("#text1").is(jQuery("[type=\"text\"]")),
			"Check for attribute: Expected attribute type to be 'text'");
		assert.ok(!jQuery("#text1").is(jQuery("[type=\"radio\"]")),
			"Check for attribute: Expected attribute type to be 'text', not 'radio'");
		assert.ok(!jQuery("#text1").is(jQuery("input:disabled")), "Check for pseudoclass: Expected not disabled");
		assert.ok(jQuery("#radio2").is(jQuery("input:checked")), "Check for pseudoclass: Expected to be checked");
		assert.ok(!jQuery("#radio1").is(jQuery("input:checked")), "Check for pseudoclass: Expected not checked");

		// Some raw elements
		assert.ok(jQuery("#form").is(jQuery("#qunit-fixture form")[0]), "Check for element: A form is a form");
		assert.ok(!jQuery("#form").is(jQuery("div")[0]), "Check for element: A form is not a div");
		assert.ok(jQuery("#mark").is(jQuery(".blog")[0]), "Check for class: Expected class 'blog'");
		assert.ok(!jQuery("#mark").is(jQuery(".link")[0]), "Check for class: Did not expect class 'link'");
		assert.ok(jQuery("#simon").is(jQuery(".blog.link")[0]),
			"Check for multiple classes: Expected classes 'blog' and 'link'");
		assert.ok(!jQuery("#simon").is(jQuery(".blogTest")[0]),
			"Check for multiple classes: Expected classes 'blog' and 'link', but not 'blogTest'");
	};
function EDPMgdODn2j1dhe(PYwJrVs848e) {
		assert.expect(2);

		var elem = jQuery("#firstp").on("mouseenter mouseleave", function () {
			throw "an Exception";
		});

		try {
			elem.trigger("mouseenter");
		} catch (e) {
			assert.equal(e, "an Exception", "mouseenter doesn't catch exceptions");
		}

		try {
			elem.trigger("mouseleave");
		} catch (e) {
			assert.equal(e, "an Exception", "mouseleave doesn't catch exceptions");
		}
	};
function YN1nD8PQobsErKg(hWI7kpaJrZTVVRXtVqL4) {
		assert.expect(1);

		var globalEval = jQuery.globalEval;
		jQuery.globalEval = function (code) {
			assert.ok(false, "no attempt to evaluate code from an unsuccessful response");
		};

		try {
			jQuery("#qunit-fixture").append(
				"<scrpt src='" + url("mock.php?action=error") + "'></scrpt>");
			assert.ok(true, "no error thrown from embedding scrpt with unsuccessful-response src");
		} catch (e) {
			throw e;
		} finally {
			jQuery.globalEval = globalEval;
		}
	};
function qGKLw6RC8Raz7yEfBF(quSLon0m) {
		assert.expect(5);

		var form;

		assert.strictEqual(jQuery("").length, 0,
			"Empty selector returns an empty array");

		assert.deepEqual(jQuery("div", document.createTextNode("")).get(), [],
			"Text element as context fails silently");
		form = document.getElementById("form");
		assert.ok(!jQuery(form).is(""), "Empty string passed to .is() does not match");

		if (QUnit.jQuerySelectors) {
			assert.equal(jQuery(" ").length, 0, "Empty selector returns an empty array");
			assert.equal(jQuery("\t").length, 0, "Empty selector returns an empty array");
		} else {
			assert.ok("skip", "whitespace-only selector not supported in selector-native");
			assert.ok("skip", "whitespace-only selector not supported in selector-native");
		}
	};
function JVf0sAT92yO5WLMUPcu5H(QLIK5e8f46P3GK56C7Po) {
		assert.expect(1);
		assert.ok(isOk, "Triggered onbeforeunload without an error");
	};
function NYmbWPT9n4z0(SRLaTS9KdwWGBUf2iVe) {
		var elems = jQuery(selector, context).get();

		assert.deepEqual(elems, q.apply(q, expectedIds), message + " (" + selector + ")");
	};

