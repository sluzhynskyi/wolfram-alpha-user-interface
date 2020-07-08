module.exports = eleventyConfig => {
    // Copy our components assets to the output folder
    eleventyConfig.addPassthroughCopy('components');

    // Returning something from the configuration function is optional
    return {
        dir: {
            input: 'inputs',
            output: "docs",
        },
    };
};