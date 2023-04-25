const
    groupBy = (array, groups, valueKey) => {
        const
            getKey = o => groups.map(k => o[k]).join('|'),
            getObject = o => Object.fromEntries([...groups.map(k => [k, o[k]]), [valueKey, 0]]);

        groups = [].concat(groups);

        return Object.values(array.reduce((r, o) => {
            console.log(getObject(o));
            // {Phase: "Phase 1", Step: "Step 1", Value: 0}
            // {Phase: "Phase 1", Step: "Step 1", Value: 0}
            // {Phase: "Phase 1", Step: "Step 2", Value: 0}
            (r[getKey(o)] ??= getObject(o))[valueKey] += +o[valueKey];
            return r;
        }, {}));
    },
    data = [{ Phase: "Phase 1", Step: "Step 1", Task: "Task 1", Value: "5" }, { Phase: "Phase 1", Step: "Step 1", Task: "Task 2", Value: "10" }, { Phase: "Phase 1", Step: "Step 2", Task: "Task 1", Value: "15" }, { Phase: "Phase 1", Step: "Step 2", Task: "Task 2", Value: "20" }, { Phase: "Phase 2", Step: "Step 1", Task: "Task 1", Value: "25" }, { Phase: "Phase 2", Step: "Step 1", Task: "Task 2", Value: "30" }, { Phase: "Phase 2", Step: "Step 2", Task: "Task 1", Value: "35" }, { Phase: "Phase 2", Step: "Step 2", Task: "Task 2", Value: "40" }];

console.log(groupBy(data, 'Phase', 'Value'));
console.log(groupBy(data, ['Phase', 'Step'], 'Value'));
