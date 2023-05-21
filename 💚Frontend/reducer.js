const [state, dispatch] = useReducer(reducer, initialState);

function reducer(state, action) {
    let newState;
    switch (action.type) {
      case 'increase':
        newState = { counter: state.counter + 1 };
        break;
      case 'descrease':
        newState = { counter: state.counter - 1 };
        break;
      default:
        throw new Error();
    }
    return newState;
  }
