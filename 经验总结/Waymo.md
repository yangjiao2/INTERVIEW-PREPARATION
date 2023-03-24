How you familiarize yourself with your team’s technical projects
How you consider business and user needs when making technical decisions
How you communicate technical concepts and trade-offs with your team members and stakeholders
How you predict and solve problems early on in a project’s lifecycle
How you understand the big picture and plan for a robust implementation


const myFunction = async => () {
    try {
      let result = await exampleFunction();
      console.log(result);
    } catch (error) {
      console.log(error);
    }
  }

  myFunction();



export function objectOrFunction(x) {
  let type = typeof x;
  return x !== null && (type === 'object' || type === 'function');
}

export function isFunction(x) {
  return typeof x === 'function';
}

export function isMaybeThenable(x) {
  return x !== null && typeof x === 'object';
}

let _isArray;
if (Array.isArray) {
  _isArray = Array.isArray;
} else {
  _isArray = x => Object.prototype.toString.call(x) === '[object Array]';
}

export const isArray = _isArray;