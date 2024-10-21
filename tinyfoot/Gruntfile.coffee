module.exports = (grunt) ->
  baseStyles = [
    'src/css/foundation/bigfoot-variables.css'
    'src/css/foundation/bigfoot-mixins.css'
    'src/css/base/bigfoot-button.css'
    'src/css/base/bigfoot-popover.css'
  ]
  variants = [
    'bottom'
    'number'
  ]

  concatSet =
    options:
      stripBanners: true
      banner: "// <%= pkg.name %> - v<%= pkg.version %> - <%= grunt.template.today('yyyy.mm.dd') %>\n\n\n"
      separator: "\n\n\n// -----\n\n\n"

    main:
      src: baseStyles
      dest: 'dist/bigfoot-default.css'

  sassSet = 'dist/bigfoot-default.css': 'dist/bigfoot-default.css'
  autoprefixSet = 'dist/bigfoot-default.css': 'dist/bigfoot-default.css'

  variants.forEach (variant) ->
    css = "dist/bigfoot-#{variant}.css"
    src = css.replace('dist/', 'src/css/variants/')
    conc = baseStyles.slice(0)
    conc.push src
    concatSet[variant] =
      src: conc
      dest: css

    sassSet[css] = css
    autoprefixSet[css] = css


  # 1. CONFIG
  grunt.initConfig
    pkg: grunt.file.readJSON('package.json')

    uglify:
      build:
        src: 'dist/bigfoot.js'
        dest: 'dist/bigfoot.min.js'

    concat: concatSet

    coffee:
      dist:
        src: 'src/coffee/bigfoot.coffee'
        dest: 'dist/bigfoot.js'

    sass:
      dist:
        options:
          style: 'expanded'

        files: sassSet

    autoprefixer:
      dist:
        files: autoprefixSet

    watch:
      options:
        livereload: false

      coffee:
        files: ['src/coffee/bigfoot.coffee']
        tasks: ['coffee', 'uglify']
        options:
          spawn: false

      css:
        files: ['src/**/*.css']
        tasks: [
          'concat'
          'sass'
          'autoprefixer'
        ]
        options:
          spawn: false


  # 2. TASKS
  require('load-grunt-tasks') grunt

  # 3. PERFORM
  grunt.registerTask 'default', [
    'coffee'
    'uglify'
    'concat'
    'sass'
    'autoprefixer'
  ]

  grunt.registerTask 'styles', [
    'concat'
    'sass'
    'autoprefixer'
  ]

  grunt.registerTask 'scripts', [
    'coffee'
    'uglify'
  ]
