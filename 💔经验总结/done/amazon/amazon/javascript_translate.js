function transformJSON(inputJSON) {
    try {
        // Parse the input JSON string into a JavaScript object
        const jsonData = JSON.parse(inputJSON);

        // Find the bucket name from the imageUrl of DailyLookImage type children
        const bucketName = findBucketName(jsonData.children);

        // Remove excess "hero" labels and add an id
        const transformedChildren = transformChildren(jsonData.children, bucketName);

        // Create the transformed JSON object
        const transformedJSON = {
            id: bucketName,
            ...jsonData,
            children: transformedChildren,
        };

        // Convert the transformed object back to a JSON string
        const transformedJSONString = JSON.stringify(transformedJSON, null, 4);

        return transformedJSONString;
    } catch (error) {
        console.error('Error transforming JSON:', error);
        return null;
    }
}

// Function to find the bucket name from the imageUrl of DailyLookImage children
function findBucketName(children) {
    for (const child of children) {
        if (child.type === 'DailyLookImage' && child.imageUrl) {
            const urlParts = child.imageUrl.split('/');
            if (urlParts.length >= 3) {
                return urlParts[2]; // Assuming the bucket name is the third part of the URL
            }
        }
    }
    return ''; // Default to an empty string if no bucket name is found
}

// Function to remove excess "hero" labels and add an id
function transformChildren(children, bucketName) {
    let heroFound = false;

    return children.map((child) => {
        // Check if the child is of type "DailyLookImage"
        if (child.type === 'DailyLookImage') {
            // If this is the first "DailyLookImage," mark it as the "hero"
            if (!heroFound) {
                heroFound = true;
                return {
                    id: child.id || generateUniqueId(), // Generate a unique id if not provided
                    ...child,
                    label: 'hero',
                };
            } else {
                // Remove the "hero" label from any other "DailyLookImage"
                const { label, ...rest } = child;
                return {
                    id: child.id || generateUniqueId(), // Generate a unique id if not provided
                    ...rest,
                };
            }
        } else {
            // For non-"DailyLookImage" children, remove the "hero" label and keep as is
            const { label, ...rest } = child;
            return {
                id: child.id || generateUniqueId(), // Generate a unique id if not provided
                ...rest,
            };
        }
    });
}

// Function to generate a unique ID (you can use a more robust method)
function generateUniqueId() {
    return 'generated-' + Math.random().toString(36).substring(7);
}

// Input JSON String
const inputJSON = `{
    // ... (your input JSON here)
}`;

// Transform the JSON
const transformedJSONString = transformJSON(inputJSON);
console.log(transformedJSONString);