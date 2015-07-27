App = Ember.Application.create({
  LOG_TRANSITIONS_INTERNAL: true
});

App.Router.map(function() {
  this.route("expense");
});


App.ExpenseRoute = Ember.Route.extend({
    model: function() {
        return this.store.findAll('expense');
    }
});


App.ExpenseAdapter = DS.RESTAdapter.extend({
  host: 'http://localhost:8001/',
  namespace: 'api',
  //url: 'http://localhost:8001',
/*
  ajax: function (url, type, hash) {
            hash.url = url;
            hash.type = type;
            hash.dataType = 'jsonp';
            hash.contentType = 'application/json; charset=utf-8';
            hash.context = this;

            if (hash.data && type !== 'GET') {
                hash.data = JSON.stringify(hash.data);
            }

            jQuery.ajax(hash);
        },
*/
});

App.Expense = DS.Model.extend({
    Name: DS.attr("string"),
    Cost: DS.attr('number')
});


// https://github.com/rituraj0/simplest-emberjs-rest-example
// https://github.com/swinton/simplest-emberjs-rest-example
