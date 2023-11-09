```javascript
import './App.css';
import React, { useCallback, useState } from 'react';

// -- WELCOME! --
// Rippling is working on a generic “Form” component as part of 
// a larger component library that will allow our developers
// to quickly stand up forms without having to worry about
// scaffolding individual inputs, submit buttons, etc.
// in our application. Let’s build a quick prototype of that today.
// -- END PROMPT! --

// Part 1: Form Schema Definition 
// What should the "schema" for a component like this look like?
// Let's explore different use cases like:
// - Additional field types
// - Validations: text, number, email, datetime, color
// - Extensability
const formSchema = {
    title: "My custom form",
    fields: [
        {
            "id": "name",
            "label": "Name",
        },
        {
            "id": "age",
            "label": "Age",
            "type": "number",
            "extra": {"min": 0, "max": 10}
        },
        {
            "id": "favoriteColor",
            "label": "Favorite Color",
        },
    ]
}

// Part 2: Let's build our form component
// Let's try to hit a few of the use cases from above
const Form = ({ formSchema, onSubmit }) => {
    const [inputFields, setInputFields] = useState({}); 
    const [errorFields, setErrorFields] = useState({}); 
    // console.log(inputFields);
    const validateForm = useCallback((fieldId, value) => {
        // formSchema.fields.find(...)
        const {fields} = formSchema;
        const field = fields.find(f => f.id == fieldId);
        console.log(field);
        if (field["extra"]){
            if (field["type"] == "number"){
                
                if (field["extra"]["min"] != null && parseInt(field["extra"]["min"]) > parseInt(value)){
                    setErrorFields(
                        prev => {
                            return {
                                ...prev,
                                [field.id]: 'invalid, minimum should be ' + field["extra"]["min"].toString(),
                            }
                        }
                    )
                } else {
                    const errorsfield  = {...errorFields};
                    delete errorsfield[field.id];
                    setErrorFields(
                        // errorFields.filter(
                        //     ef => ef[field.id] != fieldId
                        // )
                        errorsfield
                    )
                }
            
            }
        }
    }, [inputFields]);

    const {title, fields} = formSchema;

    const content = fields.map(field => {
        return (
            <div> 
                <span> {field.label}</span>
                <input
                    key={field.id}
                    name={field.label ?? 'label'}
                    type={field.type ?? 'text'}
                    onChange={(e) => {
                        setInputFields(
                            prev => {
                                return {
                                    ...prev,
                                    [field.id]: e.target.value,
                                }
                            }
                        )
                        validateForm(field.id, e.target.value)
                    }}
                > 
                </input>
                <span>{errorFields[field.id]} </span>
                
            </div> );
    });
    return (
        <div>
            <span>{title}</span>
            <div>
            {content}
            </div>
            <button onClick={() => onSubmit(inputFields)} disable={errorFields.keys().length != 0}> Submit </button>
        </div>
    );
}

const App = () => {
    const onSubmit = useCallback((formData) => {
        console.log('Hooray!', formData)
    }, []);
    
    return (
        <div className="form-container">
            <Form formSchema={formSchema} onSubmit={onSubmit} />
        </div>
    );
}

export default App;

```