
$.validator.addMethod("email1", function(value, element) {
    return this.optional(element) || /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,5}$/i.test(value);
}, "Email inválido");

$.validator.addMethod("email2", function(value, element) {
    return this.optional(element) || /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$/i.test(value);
}, "Email inválido");

$.validator.addMethod("telefono", function(value, element) {
    return this.optional(element) || /^\d{11}$/.test(value);
}, "Teléfono inválido");

$.validator.addMethod("rif", function(value, element) {
    return this.optional(element) || /^\d{9}$/.test(value);
}, "Rif inválido");

$.validator.addMethod("alfanumerico", function(value, element) {
    return this.optional(element) || /^[a-z0-9_]*$/.test(value);
}, "Sólo letras y números");

$.validator.addMethod("alfabetico", function(value, element) {
    return this.optional(element) || /^[a-zA-Z'.\s]{1,100}$/i.test(value);
}, "Sólo letras");

$.validator.addMethod("numerico", function(value, element) {
    return this.optional(element) || /^[0-9]*$/i.test(value);
}, "Sólo números");

$.validator.addMethod("numericocoma", function(value, element) {
    return this.optional(element) || /^([0-9]+,+[0-9]{1,3})*$/i.test(value);
}, "No es un decimal");

$.validator.addMethod("dosdecimales", function(value, element) {
    return this.optional(element) || /^([0-9]{2}+.+[0-9]{2})*$/i.test(value);
}, "No es un decimal valido");
