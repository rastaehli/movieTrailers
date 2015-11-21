var N3 = require('n3');
var fs = require('fs');

// console.log(N3);
var parser = N3.Parser();
var inputFileName = 'C:/Users/chq-richards/workspaceLunacy/business-model-browser/src/main/demoDeployments.owl'
var resources = {};

// return resource for subject URI
var lookup = function(uri) {
    if (!resources[uri]) {
      resources[uri] = { uri: uri};
    }
    return resources[uri];
}

// add predicate value to a resource
var setAttribute = function(resource,predicate,object) {
	if (!resource[predicate]) {
      // console.log('adding predicate: ',triple.predicate);
      resource[predicate] = [];  // need array because can be multivalued
      // console.log('resource[triple.predicate] : ',resources[triple.predicate]);
    }
    // console.log('adding predicate: ',triple.predicate, ' value: ', triple.object);
    resource[predicate].push(object);
}

// add this predicate attribute to subject
var tripleAction=function(error,triple,prefixes) {
  if (triple) {
    // console.log(triple.subject, triple.predicate, triple.object, '.');
    var resource = lookup(triple.subject);
    // console.log(resources);
    // console.log('resource[triple.predicate] : ',resource[triple.predicate]);
    setAttribute(resource,triple.predicate,triple.object);
    // console.log('resource[triple.predicate] : ',resources[triple.predicate]);
  } else {
    console.log('end of input file');
    showResources();
    // console.log(resources);
  }
}

var inputParser = function(err,data) {
  if (err) {
    return console.log(err);
  }
  parser.parse(data,tripleAction);
}

var showResources = function() {
  var i = 0;
  for (id in resources) {
    var resource = resources[id];
    if (isService(resource)) {
      // compute integer x,y coordinates for node position
      console.log('{');
      console.log(' "id": "',getLabel(resource),'",');
      console.log(' "x": ',i%8,',');
      console.log(' "y": ',Math.floor(i/8),',');
      console.log(' "size": 3');
      console.log('},');
      i = i + 1;
      // console.log(getLabel(resource), ' is a service');
    }
  }
}

var getLabel = function(resource) {
  var labelPredicate = 'http://www.w3.org/2000/01/rdf-schema#label';
  if (!resource[labelPredicate]) { return nameFromURI(resource) };
  if (resource[labelPredicate].size < 1) { return nameFromURI(resource) };
  return resource[labelPredicate][0];
}

var nameFromURI = function(resource) {
  var parts = resource.uri.split('#');
  // console.log(parts, ' size=',parts.length);
  return parts[parts.length - 1];
}

var isService = function(resource) {
  for (id in resource) {
  // console.log('id: ',id)
  // console.log('location=',id.indexOf('OWLObjectProperty'));
    if (id === 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type') {
      var types = resource[id];
      for (id in types) {
        var type = types[id];
        // console.log('type: ',type);
        if (type.indexOf('Webapp') >= 0) {
          // console.log('type is a service');
          return true
        }
        if (type.indexOf('Database') >= 0) {
          // console.log('type is a service');
          return true
        }
        if (type.indexOf('Service') >= 0) {
          // console.log('type is a service');
          return true
        }
      }

    }
  }
  return false;
}


fs.readFile(inputFileName,'utf8',inputParser)
console.log('all done');