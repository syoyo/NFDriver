#!/usr/bin/env python

import sys

from nfbuildlinux import NFBuildLinux
from build_options import BuildOptions


def main():
    buildOptions = BuildOptions()
    buildOptions.addOption("installDependencies", "Install dependencies")
    buildOptions.addOption("lintCmake", "Lint cmake files")
    buildOptions.addOption("lintCppWithInlineChange",
                           "Lint CPP Files and fix them")

    buildOptions.addOption("makeBuildDirectory",
                           "Wipe existing build directory")
    buildOptions.addOption("generateProject", "Regenerate project")

    buildOptions.addOption("buildTargetCLI", "Build Target: CLI")
    buildOptions.addOption("buildTargetLibrary", "Build Target: Library")

    buildOptions.setDefaultWorkflow("Empty workflow", [])

    buildOptions.addWorkflow("lint", "Run lint workflow", [
        'installDependencies',
        'lintCmake',
        'lintCppWithInlineChange'
    ])

    buildOptions.addWorkflow("build", "Production Build", [
        'installDependencies',
        'lintCmake',
        'makeBuildDirectory',
        'generateProject',
        'buildTargetLibrary',
        'buildTargetCLI'
    ])

    options = buildOptions.parseArgs()
    buildOptions.verbosePrintBuildOptions(options)

    library_target = 'NFDriver'
    cli_target = 'NFDriverCLI'
    nfbuild = NFBuildLinux()


    if buildOptions.checkOption(options, 'installDependencies'):
        nfbuild.installDependencies()

    if buildOptions.checkOption(options, 'lintCmake'):
        nfbuild.lintCmake()

    if buildOptions.checkOption(options, 'lintCppWithInlineChange'):
        nfbuild.lintCPP(make_inline_changes=True)

    if buildOptions.checkOption(options, 'makeBuildDirectory'):
        nfbuild.makeBuildDirectory()

    if buildOptions.checkOption(options, 'generateProject'):
        nfbuild.generateProject()

    if buildOptions.checkOption(options, 'buildTargetCLI'):
        nfbuild.buildTarget(cli_target)

    if buildOptions.checkOption(options, 'buildTargetLibrary'):
        nfbuild.buildTarget(library_target)

if __name__ == "__main__":
    main()