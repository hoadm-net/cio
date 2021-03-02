function absa_init() {
    var $ = go.GraphObject.make;

    myDiagram =
        $(go.Diagram, "myDiagramDiv",
            {
                "toolManager.mouseWheelBehavior": go.ToolManager.WheelZoom,
                "undoManager.isEnabled": false
            });

    myDiagram.nodeTemplate =
        $(go.Node, "Auto",
            new go.Binding("location", "loc", go.Point.parse).makeTwoWay(go.Point.stringify),
            $(go.Shape, "RoundedRectangle", {
                parameter1: 20,
                fill: $(go.Brush, "Linear", {
                    0: "rgb(254, 201, 0)",
                    1: "rgb(254, 162, 0)"
                }),
                stroke: null,
                portId: "",
                fromLinkable: true,
                fromLinkableSelfNode: true,
                fromLinkableDuplicates: true,
                toLinkable: true,
                toLinkableSelfNode: true,
                toLinkableDuplicates: true,
                cursor: "pointer"
            }),
            $(go.TextBlock, {
                    font: "500 13px helvetica, bold arial, sans-serif",
                    editable: false
                },
                new go.Binding("text").makeTwoWay())
        );

    myDiagram.nodeTemplate.selectionAdornmentTemplate =
        $(go.Adornment, "Spot",
            $(go.Panel, "Auto",
                $(go.Shape, {
                    fill: null,
                    stroke: "blue",
                    strokeWidth: 2
                }),
                $(go.Placeholder) // a Placeholder sizes itself to the selected Node
            ),
            // the button to create a "next" node, at the top-right corner
            $("Button", {
                    alignment: go.Spot.TopRight,
                    click: addNodeAndLink // this function is defined below
                },
                $(go.Shape, "PlusLine", {
                    width: 6,
                    height: 6
                })
            )
        );

    function addNodeAndLink(e, obj) {
        var adornment = obj.part;
        var diagram = e.diagram;
        diagram.startTransaction("Add State");

        var fromNode = adornment.adornedPart;
        var fromData = fromNode.data;
        // create a new "State" data object, positioned off to the right of the adorned Node
        var toData = {
            text: "new"
        };
        var p = fromNode.location.copy();
        p.x += 200;
        toData.loc = go.Point.stringify(p); // the "loc" property is a string, not a Point object
        // add the new node data to the model
        var model = diagram.model;
        model.addNodeData(toData);

        // create a link data from the old node data to the new node data
        var linkdata = {
            from: model.getKeyForNodeData(fromData), // or just: fromData.id
            to: model.getKeyForNodeData(toData),
            text: "transition"
        };
        // and add the link data to the model
        model.addLinkData(linkdata);

        // select the new Node
        var newnode = diagram.findNodeForData(toData);
        diagram.select(newnode);

        diagram.commitTransaction("Add State");

        // if the new node is off-screen, scroll the diagram to show the new node
        diagram.scrollToRect(newnode.actualBounds);
    }

    // replace the default Link template in the linkTemplateMap
    myDiagram.linkTemplate =
        $(go.Link, // the whole link panel
            {
                curve: go.Link.Bezier,
                adjusting: go.Link.Stretch,
                reshapable: true,
                relinkableFrom: true,
                relinkableTo: true,
                toShortLength: 3
            },
            new go.Binding("points").makeTwoWay(),
            new go.Binding("curviness"),
            $(go.Shape, // the link shape
                {
                    strokeWidth: 1.5
                }),
            $(go.Shape, // the arrowhead
                {
                    toArrow: "standard",
                    stroke: null
                }),
            $(go.Panel, "Auto",
                $(go.Shape, // the label background, which becomes transparent around the edges
                    {
                        fill: $(go.Brush, "Radial", {
                            0: "rgb(255, 255, 255)",
                            0.3: "rgb(255, 255, 255)",
                            1: "rgba(255, 255, 255, 0)"
                        }),
                        stroke: null
                    }),
                $(go.TextBlock, "transition", // the label text
                    {
                        textAlign: "center",
                        font: "9pt helvetica, arial, sans-serif",
                        margin: 4,
                        editable: true // enable in-place editing
                    },
                    // editing the text automatically updates the model data
                    new go.Binding("text").makeTwoWay())
            )
        );
}