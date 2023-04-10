"use strict";

const path = require("path");
const isLocal = typeof process.pkg === "undefined";
const basePath = isLocal ? process.cwd() : path.dirname(process.execPath);
const { MODE } = require(path.join(basePath, "src/blendMode.js"));

const layersDir = path.join(basePath, "../step1_layers_to_spritesheet/output"); // Input is read from previous step
const outputDir = path.join(basePath, "/output"); // Images are written to output folder
const buildDir = path.join(basePath, "../build"); // JSON are written to json folder

/*********************
 * General Generator Options
 ***********************/

const {
    numFramesPerBatch,
    numberOfFrames,
    useBatches,
    description,
    baseUri,
    height,
    width,
    startIndex,
    thumbnailUri,
    generateThumbnail,
    debug,
    totalSupply,
    layersFolder,
    outputType,
    animationUri,
} = require(path.join(basePath, "../global_config.json"));

// let numBaptized = 10260;
// let numAnointed = 1728;
let numBaptized = 24;
let numAnointed = 24;

let numAscended = 12;

// numBaptized - Math.floor(numBaptized / 12) * 11;

/* ONLY VARIABLE THAT YOU NEED TO EDIT IS HERE */
let layerConfigurations = [
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 11,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Asher Bible", trait: "Bible" },
            { name: "Asher Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 10,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Benjamin Bible", trait: "Bible" },
            { name: "Benjamin Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 9,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Gad Bible", trait: "Bible" },
            { name: "Gad Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 8,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Issachar Bible", trait: "Bible" },
            { name: "Issachar Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 7,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Joseph Bible", trait: "Bible" },
            { name: "Joseph Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 6,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Judah Bible", trait: "Bible" },
            { name: "Judah Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 5,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Levi Bible", trait: "Bible" },
            { name: "Levi Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 4,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Manasseh Bible", trait: "Bible" },
            { name: "Manasseh Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 3,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Naphtali Bible", trait: "Bible" },
            { name: "Naphtali Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 2,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Reuben Bible", trait: "Bible" },
            { name: "Reuben Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 1,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Simeon Bible", trait: "Bible" },
            { name: "Simeon Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized - Math.floor(numBaptized / 12) * 0,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Background" },
            { name: "Zebulun Bible", trait: "Bible" },
            { name: "Zebulun Crosses", trait: "Cross" },
            { name: "Verse" },
            { name: "Baptized", trait: "Rarity" },
        ],
    },
    {
        growEditionSizeTo: numBaptized + numAnointed,
        namePrefix: "CyberBibles",
        layersOrder: [
            { name: "Anointed Background", trait: "Background" },
            { name: "Anointed Bible", trait: "Bible" },
            { name: "Verse" },
            { name: "Anointed", trait: "Rarity" },
        ],
    },
    // {
    //     growEditionSizeTo: numBaptized + numAnointed + numAscended,
    //     namePrefix: "CyberBibles",
    //     layersOrder: [
    //         { name: "Ascended Bible", trait: "Bible" },
    //         { name: "Verse" },
    //         { name: "Ascended", trait: "Rarity" },
    //     ],
    // },
];

const format = {
    width: useBatches ? width * numFramesPerBatch : width * numberOfFrames,
    height,
    smoothing: true, // set to false when up-scaling pixel art.
};

const background = {
    generate: false,
    brightness: "80%",
};

const layerConfigurationsZIndex = [
    {
        growEditionSizeTo: totalSupply,
        namePrefix: "Bouncing Ball Z-Index Example:",
        layersOrder: [
            { name: "Background" },
            { name: "Landscape" },
            { name: "Ball" },
        ],
    },
];

// This will create totalSupply - 1 common balls, and 1 rare ball
// They will be in order but you can shuffleLayerConfigurations
const layerConfigurationsGrouping = [
    {
        growEditionSizeTo: totalSupply - 1,
        namePrefix: "Bouncing Ball Common:",
        layersOrder: [
            { name: "Background" },
            { name: "Landscape" },
            { name: "Common Ball", trait: "Ball" },
            { name: "Common Hat", trait: "Hat" },
        ],
    },
    {
        growEditionSizeTo: totalSupply,
        namePrefix: "Bouncing Ball Rare:",
        layersOrder: [
            { name: "Background" },
            { name: "Landscape" },
            { name: "Rare Ball", trait: "Ball" },
            { name: "Rare Hat", trait: "Hat" },
        ],
    },
];

const layerConfigurationsIfThen = [
    {
        growEditionSizeTo: totalSupply,
        namePrefix: "", // Use to add a name to Metadata `name:`
        layersOrder: [
            { name: "Background" },
            { name: "Landscape" },
            {
                name: "Ball",
            },
        ],
    },
];

const handler = {
    get: function (target, name) {
        return target.hasOwnProperty(name) ? target[name] : layerConfigurations;
    },
};

const layerConfigurationMapping = new Proxy(
    {
        layers: layerConfigurations,
        layers_z_index: layerConfigurationsZIndex,
        layers_grouping: layerConfigurationsGrouping,
        layers_if_then: layerConfigurationsIfThen,
    },
    handler
);

layerConfigurations = layerConfigurationMapping[layersFolder];

/**
 * Set to true for when using multiple layersOrder configuration
 * and you would like to shuffle all the artwork together
 */
const shuffleLayerConfigurations = true;

const debugLogs = debug;

/*********************
 * Advanced Generator Options
 ***********************/

// if you use an empty/transparent file, set the name here.
const emptyLayerName = "NONE";

/**
 * Incompatible items can be added to this object by a files cleanName
 * This works in layer order, meaning, you need to define the layer that comes
 * first as the Key, and the incompatible items that _may_ come after.
 * The current version requires all layers to have unique names, or you may
 * accidentally set incompatibilities for the _wrong_ item.
 *
 * Try run it with layers_incompatible and see that the Flashing background
 * will not have the flashing ball
 */
const incompatible = {
    // Flashing: ["Multicolor"],
};

/**
 * Require combinations of files when constructing DNA, this bypasses the
 * randomization and weights.
 *
 * The layer order matters here, the key (left side) is an item within
 * the layer that comes first in the stack.
 * the items in the array are "required" items that should be pulled from folders
 * further in the stack
 */
const forcedCombinations = {
    // floral: ["MetallicShades", "Golden Sakura"],
};

/**
 * In the event that a filename cannot be the trait value name, for example when
 * multiple items should have the same value, specify
 * clean-filename: trait-value override pairs. Wrap filenames with spaces in quotes.
 */
const traitValueOverrides = {
    // Helmet: "Space Helmet",
    // "gold chain": "GOLDEN NECKLACE",
};

const extraMetadata = {
    text: "ipfs://WEBUriToReplace",
};

const extraAttributes = () => [
    // Optionally, if you need to overwrite one of your layers attributes.
    // You can include the same name as the layer, here, and it will overwrite
    //
    // {
    // trait_type: "Bottom lid",
    //   value: ` Bottom lid # ${Math.random() * 100}`,
    // },
    // {
    //   display_type: "boost_number",
    //   trait_type: "Aqua Power",
    //   value: Math.random() * 100,
    // },
    // {
    //   display_type: "boost_number",
    //   trait_type: "Health",
    //   value: Math.random() * 100,
    // },
    // {
    //   display_type: "boost_number",
    //   trait_type: "Mana",
    //   value: Math.floor(Math.random() * 100),
    // },
];

const rarityDelimiter = "#";

const uniqueDnaTorrance = 10000;

/**
 * Set to true to always use the root folder as trait_type
 * Set to false to use weighted parent folders as trait_type
 * Default is true.
 */
const useRootTraitType = true;

module.exports = {
    animationUri,
    background,
    baseUri,
    buildDir,
    debugLogs,
    description,
    emptyLayerName,
    extraAttributes,
    extraMetadata,
    forcedCombinations,
    format,
    generateThumbnail,
    incompatible,
    layerConfigurations,
    layersDir,
    outputDir,
    thumbnailUri,
    rarityDelimiter,
    shuffleLayerConfigurations,
    startIndex,
    traitValueOverrides,
    uniqueDnaTorrance,
    useRootTraitType,
    outputType,
};
