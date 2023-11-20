module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: '@babel/eslint-parser'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'vue/multi-word-component-names': 'off',
    'object-curly-spacing': 'off',
    'quotes': ["off"],
    "space-before-function-paren": ["off"],
    "spaced-comment": ["off"],
    "semi": ["off"],
    "comma-dangle": ["off"],
    "no-unneeded-ternary": ["off"],
    "vue/no-dupe-keys": ["off"],
    "indent": ["off"],
    "padded-blocks": ["off"],
    "no-unused-vars": ["off"],
    "prefer-const": ["off"],
    "vue/no-mutating-props": ["off"],
    "key-spacing": ["off"]

  }
}
