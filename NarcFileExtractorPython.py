import ndspy.narc
import ndspy.rom



game = input('Enter the nds game you want to extract a file from:')

rom = ndspy.rom.NintendoDSRom.fromFile(game)

wanted = input('Enter the name of the narc file you want to extract:')

d = {}


if hasattr(rom.filenames, "files"):
    for i, path in enumerate(rom.files):
        if path is not None:
            d[rom.filenames.filenameOf(i)] = i


narc_index = d[wanted]

narc_data = rom.files[narc_index]
narc = ndspy.narc.NARC(narc_data)


folder_name = input('Enter the name of the saved narc file:')

narc.saveToFile(folder_name)
   
   