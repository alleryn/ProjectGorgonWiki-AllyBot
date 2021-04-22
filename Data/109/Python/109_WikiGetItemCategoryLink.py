def getItemCategoryLink(keyword):
	plural = ''
	if keyword == "AbilityIngredient":
		plural = "Ability Ingredients"
	elif keyword == "AbilityRecipe":
		plural = "Ability Recipes"
	elif keyword == "AdvancedInk":
		plural = "Advanced Inks"
	elif keyword == "Agate":
		plural = "Agates"
	elif keyword == "Alchemy":
		plural = "Alchemy Items"
	elif keyword == "AlchemyIngredient":
		plural = "Alchemy Ingredients"
	elif keyword == "AlchemyRecipe":
		plural = "Alchemy Recipes"
	elif keyword == "AlchemyRelated":
		plural = "Alchemy-Related Items"
	elif keyword == "AlcoholBarrel":
		plural = "Alcohol Barrels"
	elif keyword == "AlcoholLevel":
		plural = "Alcohol Levels"
	elif keyword == "Alien":
		plural = "Alien Items"
	elif keyword == "AmazingInk":
		plural = "Amazing Ink"
	elif keyword == "Amberjack":
		plural = "Amberjacks"
	elif keyword == "Amethyst":
		plural = "Amethysts"
	elif keyword == "Amulet":
		plural = "Amulets"
	elif keyword == "AmuletOfTheRuggedTraveler":
		plural = "Amulets of the Rugged Traveler"
	elif keyword == "AnchorRune":
		plural = "Anchor Runes"
	elif keyword == "AncientBook":
		plural = "Ancient Books"
	elif keyword == "AncientCoin":
		plural = "Ancient Coins"
	elif keyword == "AnimalHorn":
		plural = "Animal Horns"
	elif keyword == "AnimalShoes":
		plural = "Animal Shoes"
	elif keyword == "Antique":
		plural = "Antiques"
	elif keyword == "Apple":
		plural = "Apples"
	elif keyword == "Aquamarine":
		plural = "Aquamarines"
	elif keyword == "Armor":
		plural = "Pieces of Armor"
	elif keyword == "ArmorOrShield":
		plural = "Armor and Shields"
	elif keyword == "ArmorPatchKit":
		plural = "Armor Patch Kits"
	elif keyword == "ArmorPatchingOnyx":
		plural = "Armor Patching Onyxes"
	elif keyword == "ArmorStake":
		plural = "Armor Stakes"
	elif keyword == "Arrow":
		plural = "Arrows"
	elif keyword == "ArtRecipe":
		plural = "Artistry Recipes"
	elif keyword == "Artwork":
		plural = "Works of Art"
	elif keyword == "AstonishingHumanoidSkull":
		plural = "Astonishing Humanoid Skulls"
	elif keyword == "Augment":
		plural = "Augments"
	elif keyword == "AugmentationRelated":
		plural = "Augmentation-Related Items"
	elif keyword == "AugmentedMantisClaw":
		plural = "Augmented Mantis Claws"
	elif keyword == "AutoCleanUp":
		plural = "Automatically Cleaned Items"
	elif keyword == "AutopsyBasic":
		plural = "Autopsy Kits"
	elif keyword == "Aventurine":
		plural = "Aventurines"
	elif keyword == "Azurite":
		plural = "Azurites"
	elif keyword == "Bacon":
		plural = "Bacon"
	elif keyword == "BaconBasket":
		plural = "Bacon Baskets "
	elif keyword == "BardArmor":
		plural = "Bard Armor"
	elif keyword == "BardHorn":
		plural = "Bard Horns"
	elif keyword == "BardInstrument":
		plural = "Bard Instruments"
	elif keyword == "BardLute":
		plural = "Bard Lutes"
	elif keyword == "BarghestSkin":
		plural = "Barghest Skins"
	elif keyword == "Barrel":
		plural = "Barrels"
	elif keyword == "BarteredHolySymbol":
		plural = "Bartered Holy Symbols"
	elif keyword == "BasicAquamarine":
		plural = "Basic Aquamarines"
	elif keyword == "BasicDiamond":
		plural = "Basic Diamonds"
	elif keyword == "BasicGrass":
		plural = "Basic Grasses"
	elif keyword == "BasicInk":
		plural = "Basic Inks"
	elif keyword == "BasicMoonstone":
		plural = "Basic Moonstones"
	elif keyword == "BasiliskTailTip":
		plural = "Basilisk Tail Tips"
	elif keyword == "BearClaw":
		plural = "Bear Claws"
	elif keyword == "BearSkin":
		plural = "Bear Skins"
	elif keyword == "BeastMeat":
		plural = "Beast Meat"
	elif keyword == "BeeLoversBouquet":
		plural = "Bee Lovers' Bouquets"
	elif keyword == "BeeRepellent":
		plural = "Bee Repellents"
	elif keyword == "Beer":
		plural = "Beer"
	elif keyword == "BeerKeg":
		plural = "Kegs of Beer"
	elif keyword == "BeerTap":
		plural = "Beer Taps"
	elif keyword == "Beet":
		plural = "Beets"
	elif keyword == "Belt":
		plural = "Belts"
	elif keyword == "Bench":
		plural = "Benches"
	elif keyword == "Berry":
		plural = "Berries"
	elif keyword == "BlackFootMorel":
		plural = "Black Foot Morels "
	elif keyword == "Blacksmithing":
		plural = "Blacksmithing Items"
	elif keyword == "Blanket":
		plural = "Blankets"
	elif keyword == "Bloodstone":
		plural = "Bloodstones"
	elif keyword == "BlueCheese":
		plural = "Blue Cheese"
	elif keyword == "BlueCrystal":
		plural = "Blue Crystals"
	elif keyword == "BlueSpinel":
		plural = "Blue Spinels"
	elif keyword == "BoarTusk":
		plural = "Boar Tusks"
	elif keyword == "BodyOrgan":
		plural = "Body Organs"
	elif keyword == "Bone":
		plural = "Bones"
	elif keyword == "BoneHook":
		plural = "Bone Hooks"
	elif keyword == "Book":
		plural = "Books"
	elif keyword == "BottledItem":
		plural = "Bottled Items"
	elif keyword == "Bounceweed":
		plural = "Bounceweed"
	elif keyword == "Bow":
		plural = "Bows"
	elif keyword == "Brain":
		plural = "Brains"
	elif keyword == "BrainBugLobe":
		plural = "Brain Bug Lobes "
	elif keyword == "Brass":
		plural = "Brass Items"
	elif keyword == "BrassGear":
		plural = "Brass Gears"
	elif keyword == "BrassNail":
		plural = "Brass Nails"
	elif keyword == "BreadDish":
		plural = "Bread Dishes"
	elif keyword == "Brewing":
		plural = "Brewing Items"
	elif keyword == "BrewingAnimalPartA5":
		plural = "Animal Parts for Brewing (Class 1)"
	elif keyword == "BrewingAnimalPartB5":
		plural = "Animal Parts for Brewing (Class 2)"
	elif keyword == "BrewingAnimalPartC5":
		plural = "Animal Parts for Brewing (Class 3)"
	elif keyword == "BrewingFruitA3":
		plural = "Fruits for Brewing (Class 1)"
	elif keyword == "BrewingFruitA4":
		plural = "Fruits for Brewing (Class 2)"
	elif keyword == "BrewingFruitB3":
		plural = "Fruits for Brewing (Class 3)"
	elif keyword == "BrewingFruitC3":
		plural = "Fruits for Brewing (Class 4)"
	elif keyword == "BrewingGarnishA2":
		plural = "Garnishes for Brewing (Class 1)"
	elif keyword == "BrewingGarnishA3":
		plural = "Garnishes for Brewing (Class 2)"
	elif keyword == "BrewingGarnishA4":
		plural = "Garnishes for Brewing (Class 3)"
	elif keyword == "BrewingGarnishB2":
		plural = "Garnishes for Brewing (Class 4)"
	elif keyword == "BrewingGarnishB3":
		plural = "Garnishes for Brewing (Class 5)"
	elif keyword == "BrewingGarnishB4":
		plural = "Garnishes for Brewing (Class 6)"
	elif keyword == "BrewingGarnishC3":
		plural = "Garnishes for Brewing (Class 7)"
	elif keyword == "BrewingGarnishC4":
		plural = "Garnishes for Brewing (Class 8)"
	elif keyword == "BrewingIngredient":
		plural = "Brewing Ingredients"
	elif keyword == "BrewingMushroomA3":
		plural = "Mushrooms for Brewing (Class 1)"
	elif keyword == "BrewingMushroomA4":
		plural = "Mushrooms for Brewing (Class 2)"
	elif keyword == "BrewingMushroomB4":
		plural = "Mushrooms for Brewing (Class 3)"
	elif keyword == "BrewingMushroomC4":
		plural = "Mushrooms for Brewing (Class 4)"
	elif keyword == "BrewingRelated":
		plural = "Brewing-Related Items"
	elif keyword == "BrewingVegetableA4":
		plural = "Vegetables for Brewing (Class 1)"
	elif keyword == "BrewingVegetableB4":
		plural = "Vegetables for Brewing (Class 2)"
	elif keyword == "BrinedCheese":
		plural = "Brined Cheese"
	elif keyword == "ButcherKnife":
		plural = "Butchering Knives"
	elif keyword == "ButcheringBonus":
		plural = "Butchering Knives with Bonuses"
	elif keyword == "Butter":
		plural = "Butter"
	elif keyword == "Cabbage":
		plural = "Cabbage"
	elif keyword == "CalligraphyBench":
		plural = "Calligraphy Benches"
	elif keyword == "CalligraphyRecipe":
		plural = "Calligraphy Recipes"
	elif keyword == "Campfire":
		plural = "Campfires"
	elif keyword == "Candle":
		plural = "Candles"
	elif keyword == "CandleRelated":
		plural = "Camdle-Related Items"
	elif keyword == "Candy":
		plural = "Candy"
	elif keyword == "Cantaloupe":
		plural = "Cantaloupes"
	elif keyword == "Carapace":
		plural = "Carapaces"
	elif keyword == "CardedCotton":
		plural = "Carded Cotton"
	elif keyword == "Carnelian":
		plural = "Carnelians"
	elif keyword == "Carpentry":
		plural = "Carpentry Items"
	elif keyword == "CarpentryRecipe":
		plural = "Carpentry Recipes"
	elif keyword == "Carrot":
		plural = "Carrots"
	elif keyword == "CatEye":
		plural = "Cat Eyes"
	elif keyword == "CatMeat":
		plural = "Cat Meat"
	elif keyword == "Cavefish":
		plural = "Cavefish"
	elif keyword == "CedarWood":
		plural = "Cedar Wood"
	elif keyword == "Chair":
		plural = "Chairs"
	elif keyword == "ChargedMycelium":
		plural = "Charged Mycelia"
	elif keyword == "CheapMeat":
		plural = "Cheap Meat"
	elif keyword == "CheapPainting":
		plural = "Cheap Paintings"
	elif keyword == "Cheese":
		plural = "Cheese"
	elif keyword == "Cheesecloth":
		plural = "Cheesecloth"
	elif keyword == "CheesemakingIngredient":
		plural = "Cheesemaking Ingredients"
	elif keyword == "ChemistryBeaker":
		plural = "Battle Chemisty Beakers"
	elif keyword == "ChemistryEquipment":
		plural = "Battle Chemistry Equipment"
	elif keyword == "ChemistryFlask":
		plural = "Battle Chemistry Flasks"
	elif keyword == "Chest":
		plural = "Chest Armor"
	elif keyword == "ChestAugment":
		plural = "Chest Augments"
	elif keyword == "Chicken":
		plural = "Chickens"
	elif keyword == "Cinnabar":
		plural = "Cinnabars"
	elif keyword == "Citrine":
		plural = "Citrines"
	elif keyword == "Citrus":
		plural = "Citrus Foods and Drinks"
	elif keyword == "Clay":
		plural = "Clay Items"
	elif keyword == "Cloth":
		plural = "Cloth"
	elif keyword == "ClothArmor":
		plural = "Cloth Armor"
	elif keyword == "ClothBoots":
		plural = "Cloth Boots"
	elif keyword == "ClothDyeableArmor":
		plural = "Dyeable Cloth Armor"
	elif keyword == "ClothGloves":
		plural = "Cloth Gloves"
	elif keyword == "ClothHelm":
		plural = "Cloth Helms"
	elif keyword == "ClothPants":
		plural = "Cloth Pants"
	elif keyword == "ClothShirt":
		plural = "Cloth Shirts"
	elif keyword == "Clothing":
		plural = "Clothing"
	elif keyword == "Clownfish":
		plural = "Clownfish"
	elif keyword == "Club":
		plural = "Clubs"
	elif keyword == "Coin":
		plural = "Coins"
	elif keyword == "ColdIron":
		plural = "Cold Iron Items"
	elif keyword == "ConsumableKit":
		plural = "Consumable Kits"
	elif keyword == "Contraption":
		plural = "Contraptions"
	elif keyword == "CookingIngredient":
		plural = "Cooking Ingredients"
	elif keyword == "CookingRecipe":
		plural = "Cooking Recipes"
	elif keyword == "CookingRelated":
		plural = "Cooking-Related Items"
	elif keyword == "Copper":
		plural = "Copper"
	elif keyword == "Corn":
		plural = "Corn"
	elif keyword == "CorpseFlesh":
		plural = "Corpse Flesh"
	elif keyword == "CorpseLimb":
		plural = "Corpse Limbs"
	elif keyword == "CorpseTrophy":
		plural = "Corpse Trophies"
	elif keyword == "CottonPlant":
		plural = "Cotton Plants"
	elif keyword == "CouncilCertificate":
		plural = "Council Certificates"
	elif keyword == "CowMalachite":
		plural = "Cow Malachites"
	elif keyword == "CowMeat":
		plural = "Cow Meat"
	elif keyword == "CowSkin":
		plural = "Cow Skins"
	elif keyword == "Crab":
		plural = "Crabs"
	elif keyword == "Crafted":
		plural = "Crafted Items"
	elif keyword == "CraftersGuild":
		plural = "Crafters' Guild Items"
	elif keyword == "Cranberries":
		plural = "Cranberries"
	elif keyword == "Craniometer":
		plural = "Craniometers"
	elif keyword == "CraniumGel":
		plural = "Cranium Gel"
	elif keyword == "CraniumPowder":
		plural = "Cranium Powder"
	elif keyword == "Crossbow":
		plural = "Crossbows"
	elif keyword == "CrossingOil":
		plural = "Crossing Oil"
	elif keyword == "Crystal":
		plural = "Crystals"
	elif keyword == "CrystalIce":
		plural = "Crystal Ice"
	elif keyword == "Dagger":
		plural = "Daggers"
	elif keyword == "Dahlia":
		plural = "Dahlias"
	elif keyword == "DairyDish":
		plural = "Dairy Dishes"
	elif keyword == "Danburite":
		plural = "Danburites"
	elif keyword == "Darkcaster":
		plural = "Darkcaster Projectile Weapons"
	elif keyword == "DeathTrooper":
		plural = "Death Trooper Equipment"
	elif keyword == "Decoction":
		plural = "Decoctions"
	elif keyword == "DeerMalachite":
		plural = "Deer Malachites"
	elif keyword == "DeerMeat":
		plural = "Deer Meat"
	elif keyword == "DeerSkin":
		plural = "Deer Skins"
	elif keyword == "DeinonychusSkin":
		plural = "Deinonychus Skins"
	elif keyword == "DelicateTackHammer":
		plural = "Delicate Tack Hammers"
	elif keyword == "Dessert":
		plural = "Desserts"
	elif keyword == "Diamond":
		plural = "Diamonds"
	elif keyword == "DinosaurMeat":
		plural = "Dinosaur Meat"
	elif keyword == "Dirk":
		plural = "Dirks"
	elif keyword == "Dirt":
		plural = "Dirt"
	elif keyword == "DiseaseCure":
		plural = "Disease Cures"
	elif keyword == "Document":
		plural = "Documents"
	elif keyword == "DogMeat":
		plural = "Dog Meat"
	elif keyword == "DragonScale":
		plural = "Dragon Scales"
	elif keyword == "Drink":
		plural = "Drinks"
	elif keyword == "DrinkableRumBarrel":
		plural = "Drinkable Rum Barrels"
	elif keyword == "DroachSkin":
		plural = "Droach Skins"
	elif keyword == "Drug":
		plural = "Drugs"
	elif keyword == "Drum":
		plural = "Drums"
	elif keyword == "Dulcimer":
		plural = "Dulcimers"
	elif keyword == "DwarfMeat":
		plural = "Dwarf Meat"
	elif keyword == "DwarvenJewelry":
		plural = "Dwarven Jewelry"
	elif keyword == "Dye":
		plural = "Dye"
	elif keyword == "EAmuletOfTheRuggedTraveler":
		plural = "Enhanced Amulets of the Rugged Traveler"
	elif keyword == "EWindstepShoes":
		plural = "Enhanced Windstep Shoes"
	elif keyword == "Ectoplasm":
		plural = "Ectoplasm"
	elif keyword == "Edible":
		plural = "Edible Items"
	elif keyword == "Eel":
		plural = "Eels"
	elif keyword == "Egg":
		plural = "Eggs"
	elif keyword == "EggDish":
		plural = "Egg Dishes"
	elif keyword == "ElfMeat":
		plural = "Elf Meat"
	elif keyword == "EltibulesSignetRing":
		plural = "Eltibule's Signet Ring"
	elif keyword == "ElvishJewelry":
		plural = "Elvish Jewelry"
	elif keyword == "ElvishStyle":
		plural = "Elvish-Style Items"
	elif keyword == "Emerald":
		plural = "Emeralds"
	elif keyword == "EmptyBottle":
		plural = "Empty Bottles"
	elif keyword == "EmptyHand":
		plural = "Empty Hand Items"
	elif keyword == "EnchantedMistletoe":
		plural = "Enchanted Mistletoe"
	elif keyword == "EnergyBow":
		plural = "Energy Bows"
	elif keyword == "Ensouled":
		plural = "Ensouled Items"
	elif keyword == "Equipment":
		plural = "Pieces of Equipment"
	elif keyword == "Escarole":
		plural = "Escarole"
	elif keyword == "EvilPumpkin":
		plural = "Evil Pumpkins"
	elif keyword == "ExoticFood":
		plural = "Exotic Foods"
	elif keyword == "ExoticPotion":
		plural = "Exotic Potions"
	elif keyword == "ExpertInk":
		plural = "Expert Ink"
	elif keyword == "Eye":
		plural = "Eyes"
	elif keyword == "FaeDPImmunity":
		plural = "Items Granting Fae Death Penalty Immunity"
	elif keyword == "FaeFelt":
		plural = "Fae Felt"
	elif keyword == "FaeMetalArmor":
		plural = "Fae Metal Armor"
	elif keyword == "FaeNavy":
		plural = "Fae Navy Equipment"
	elif keyword == "FaeSilk":
		plural = "Fae Silk"
	elif keyword == "FairyChime":
		plural = "Fairy Charms"
	elif keyword == "FairyMagicTopaz":
		plural = "Fairy Magic Topaz"
	elif keyword == "FairyWing":
		plural = "Fairy Wings"
	elif keyword == "FamiliarRecallCollar":
		plural = "Familiar Recall Collar"
	elif keyword == "Fashionable":
		plural = "Fashionable Items"
	elif keyword == "FearOil":
		plural = "Fear Oil"
	elif keyword == "Feather":
		plural = "Feathers"
	elif keyword == "Feet":
		plural = "Foot gear"
	elif keyword == "FeetAugment":
		plural = "Augments for Footgear"
	elif keyword == "Femur":
		plural = "Femurs"
	elif keyword == "FetishBag":
		plural = "Fetish Bags"
	elif keyword == "Figurine":
		plural = "Figurines"
	elif keyword == "FireDust":
		plural = "Fire Dust"
	elif keyword == "FireStaff":
		plural = "Fire Staves"
	elif keyword == "FirstAidBomb":
		plural = "First Aid Bombs"
	elif keyword == "FirstAidGarnet":
		plural = "First Aid Garnet"
	elif keyword == "FirstAidKit":
		plural = "First Aid Kits"
	elif keyword == "Fish":
		plural = "Fish"
	elif keyword == "FishDish":
		plural = "Fish Dishes"
	elif keyword == "FishScales":
		plural = "Fish Scales"
	elif keyword == "FlawlessBarghestSkin":
		plural = "Trophy Barghest Skins"
	elif keyword == "FlawlessBearSkin":
		plural = "Trophy Bear Skins"
	elif keyword == "FlawlessCowSkin":
		plural = "Trophy Cow Skins"
	elif keyword == "FlawlessDeerSkin":
		plural = "Trophy Deer Skins"
	elif keyword == "FlawlessDeinonychusSkin":
		plural = "Trophy Deinonychus Skins"
	elif keyword == "FlawlessDroachSkin":
		plural = "Trophy Droach Skins"
	elif keyword == "FlawlessGoatSkin":
		plural = "Trophy Goat Hides"
	elif keyword == "FlawlessHippoSkin":
		plural = "Trophy Hippo Hides"
	elif keyword == "FlawlessPantherSkin":
		plural = "Trophy Panther Skins"
	elif keyword == "FlawlessPigSkin":
		plural = "Trophy Pig Skins"
	elif keyword == "FlawlessRabbitSkin":
		plural = "Trophy Rabbit Skins"
	elif keyword == "FlawlessRatSkin":
		plural = "Trophy Rat Skins"
	elif keyword == "FlawlessRhinoHide":
		plural = "Trophy Rhino Hides"
	elif keyword == "FlawlessSharkSkin":
		plural = "Trophy Shark Skins"
	elif keyword == "FlawlessSheepSkin":
		plural = "Trophy Sheep Skins"
	elif keyword == "FlawlessSkin":
		plural = "Trophy Skins"
	elif keyword == "FlawlessSnakeSkin":
		plural = "Trophy Snake Skins"
	elif keyword == "FlawlessTigerSkin":
		plural = "Trophy Tiger Skins"
	elif keyword == "FlawlessWolfSkin":
		plural = "Trophy Wolf Skins"
	elif keyword == "Fletching":
		plural = "Fletching Items"
	elif keyword == "FletchingBox":
		plural = "Fletching Boxes"
	elif keyword == "Flounder":
		plural = "Flounders"
	elif keyword == "Flower":
		plural = "Flowers"
	elif keyword == "FlowerArrangement":
		plural = "Flower Arrangements"
	elif keyword == "FlowerArrangementRecipe":
		plural = "Flower Arrangement Recipes"
	elif keyword == "Fluorite":
		plural = "Fluorites"
	elif keyword == "FlyAmanita":
		plural = "Fly Amanitas"
	elif keyword == "Food":
		plural = "Food Items"
	elif keyword == "FoodOrCookingIngredient":
		plural = "Food or Cooking Ingredients"
	elif keyword == "Fruit":
		plural = "Fruits"
	elif keyword == "FruitCocktail":
		plural = "Fruit Cocktails"
	elif keyword == "FruitDish":
		plural = "Fruit Dishes"
	elif keyword == "FuelOil":
		plural = "Fuel Oils"
	elif keyword == "Fur":
		plural = "Furs"
	elif keyword == "Furniture":
		plural = "Furniture Items"
	elif keyword == "Gadgeteering":
		plural = "Gadgeteering Items"
	elif keyword == "GameChip":
		plural = "Game Chips"
	elif keyword == "GardeningRecipe":
		plural = "Gardening Recipes"
	elif keyword == "GardeningRelated":
		plural = "Gardening-Related Items"
	elif keyword == "Garnet":
		plural = "Garnets"
	elif keyword == "GazlukOfficer":
		plural = "Gazluk Officer Equipment"
	elif keyword == "GazlukOfficersRing":
		plural = "Gazluk Officer's Rings"
	elif keyword == "GazlukWarWizard":
		plural = "Gazluk War Wizard Equipment"
	elif keyword == "Gear":
		plural = "Gears"
	elif keyword == "Gem":
		plural = "Gems"
	elif keyword == "GemCrusher":
		plural = "Gem Crushers"
	elif keyword == "GeneAnalyzer_Arthropods":
		plural = "Gene Analyzers for Arthropods"
	elif keyword == "GeneAnalyzer_Cats":
		plural = "Gene Analyzers for Cats"
	elif keyword == "GeneAnalyzer_Ruminants":
		plural = "Gene Analyzers for Ruminants"
	elif keyword == "Genealogy":
		plural = "Genealogy Items"
	elif keyword == "GeneticsRelated":
		plural = "Genetics-Related Items"
	elif keyword == "GiantBatMalachite":
		plural = "Giant Bat Malachites"
	elif keyword == "GiantBatRecipe":
		plural = "Giant Bat Recipes"
	elif keyword == "GiantHairball":
		plural = "Giant Hairballs"
	elif keyword == "GingerbreadHuman":
		plural = "Gingerbread Humans"
	elif keyword == "Gizmo":
		plural = "Gizmos"
	elif keyword == "Glass":
		plural = "Glass"
	elif keyword == "GlassChunk":
		plural = "Chunks of Glass"
	elif keyword == "GloveAugment":
		plural = "Glove Augments"
	elif keyword == "GlowyYellowCrystal":
		plural = "Glowy Yellow Crystals"
	elif keyword == "GoatSkin":
		plural = "Goat Skins"
	elif keyword == "GoblinCallingCard":
		plural = "Goblin Calling Cards"
	elif keyword == "GoblinHairpin":
		plural = "Goblin Hairpins"
	elif keyword == "GoblinTrash":
		plural = "Goblin Trash"
	elif keyword == "Gold":
		plural = "Gold Items"
	elif keyword == "GoldenAcorn":
		plural = "Golden Acorns"
	elif keyword == "GoldenRodDye":
		plural = "Goldenrod Dyes"
	elif keyword == "GolemClay":
		plural = "Golem Clay"
	elif keyword == "GolfSprint":
		plural = "Items Granting Golf-Related Sprint Bonuses"
	elif keyword == "Goshenite":
		plural = "Goshenites"
	elif keyword == "Grapefish":
		plural = "Grapefish"
	elif keyword == "Grapes":
		plural = "Grapes"
	elif keyword == "Grass":
		plural = "Grass"
	elif keyword == "GreenCrystal":
		plural = "Green Crystals"
	elif keyword == "GreenVexfish":
		plural = "Green Vexfish"
	elif keyword == "GroxmaxMushroom":
		plural = "Groxmax Mushrooms"
	elif keyword == "GuardianLure":
		plural = "Guardian Lures"
	elif keyword == "GurHorta":
		plural = "Gur Horta"
	elif keyword == "Halberd":
		plural = "Halberds"
	elif keyword == "HalloweenCandy":
		plural = "Halloween Candy"
	elif keyword == "Hammer":
		plural = "Hammers"
	elif keyword == "Hands":
		plural = "Items Worn on the Hands"
	elif keyword == "HardLiquor":
		plural = "Hard Liquors"
	elif keyword == "HardLiquorBarrel":
		plural = "Barrels of Hard Liquor"
	elif keyword == "Harp":
		plural = "Harps"
	elif keyword == "HatredOil":
		plural = "Hatred Oil"
	elif keyword == "Head":
		plural = "Items Worn on the Head"
	elif keyword == "Heart":
		plural = "Hearts"
	elif keyword == "Heartshroom":
		plural = "Heartshrooms"
	elif keyword == "HelmAugment":
		plural = "Helm Augments"
	elif keyword == "Herb":
		plural = "Herbs"
	elif keyword == "Hideous":
		plural = "Hideous-Looking Equipment"
	elif keyword == "HippoSkin":
		plural = "Hippo Skins"
	elif keyword == "HippoTooth":
		plural = "Hippo Teeth"
	elif keyword == "HolySymbol":
		plural = "Holy Symbols"
	elif keyword == "Hoop":
		plural = "Hoops"
	elif keyword == "HopeOil":
		plural = "Hope Oil"
	elif keyword == "HumanMeat":
		plural = "Human Meat"
	elif keyword == "HumanoidSkull":
		plural = "Humanoid Skulls"
	elif keyword == "IceCore":
		plural = "Ice Cores"
	elif keyword == "IceStaff":
		plural = "Ice Staves"
	elif keyword == "IlmariWarCacheMap":
		plural = "Ilmari War Cache Maps"
	elif keyword == "ImpressiveHumanoidSkull":
		plural = "Impressive (and better) Humanoid Skulls"
	elif keyword == "Indestructible":
		plural = "Indestructible Items"
	elif keyword == "InfusionOil":
		plural = "Infusion Oils"
	elif keyword == "Ingredient":
		plural = "Ingredients"
	elif keyword == "IngredientOnly":
		plural = "Items which are Only Ingredients"
	elif keyword == "Ink":
		plural = "Inks"
	elif keyword == "InkRemover":
		plural = "Ink Removers"
	elif keyword == "InsectMeat":
		plural = "Insect Meat"
	elif keyword == "InsectWings":
		plural = "Insect Wings"
	elif keyword == "InstantSnack":
		plural = "Instant-Snacks"
	elif keyword == "Instrument":
		plural = "Instruments"
	elif keyword == "IocaineMushroom":
		plural = "Iocaine Mushrooms"
	elif keyword == "IocainePoison":
		plural = "Iocaine Poisons"
	elif keyword == "Iridium":
		plural = "Iridium"
	elif keyword == "IrradiatedCrystal":
		plural = "Irradiated Crystals"
	elif keyword == "Ivory":
		plural = "Ivory"
	elif keyword == "IvoryTrophy":
		plural = "Ivory Trophies"
	elif keyword == "Jewelry":
		plural = "Jewelry"
	elif keyword == "JewelryCraftingRecipe":
		plural = "Jewelry Crafting Recipes"
	elif keyword == "JuniperBerries":
		plural = "Juniper Berries"
	elif keyword == "KhyrulekLore":
		plural = "Items About Which the Pulsing Crystal has Knowledge"
	elif keyword == "Knife":
		plural = "Knives"
	elif keyword == "KrakenPart":
		plural = "Kraken Parts"
	elif keyword == "Lac":
		plural = "Lac"
	elif keyword == "LapisLazuli":
		plural = "Lapis Lazulis"
	elif keyword == "LawaraGift":
		plural = "Gifts from Lawara"
	elif keyword == "Lead":
		plural = "Lead Items"
	elif keyword == "LeadFigurine":
		plural = "Lead Figurines"
	elif keyword == "LeatherArmor":
		plural = "Pieces of Leather Armor"
	elif keyword == "LeatherBoots":
		plural = "Leather Boots"
	elif keyword == "LeatherDyeableArmor":
		plural = "Dyeable Leather Armor"
	elif keyword == "LeatherGloves":
		plural = "Leather Gloves"
	elif keyword == "LeatherHelm":
		plural = "Leather Helms"
	elif keyword == "LeatherPants":
		plural = "Leather Pants"
	elif keyword == "LeatherRoll":
		plural = "Leather Rolls"
	elif keyword == "LeatherShirt":
		plural = "Leather Shirts"
	elif keyword == "LeatherStrips":
		plural = "Leather Strips"
	elif keyword == "LeathercraftingRecipe":
		plural = "Leather Crafting Recipes"
	elif keyword == "Leatherworking":
		plural = "Leatherworking Items"
	elif keyword == "LeatherworkingRecipe":
		plural = "Leatherworking Recipes"
	elif keyword == "LegAugment":
		plural = "Leg Augments"
	elif keyword == "Legs":
		plural = "Items Worn on the Legs"
	elif keyword == "Lemon":
		plural = "Lemons"
	elif keyword == "LetterToYetta":
		plural = "Letters to Yetta"
	elif keyword == "Lint_AbilityIngredient":
		plural = "Lint Ability Ingredients"
	elif keyword == "Lint_AssumeObtainable":
		plural = "Lint Items Assumed to be Obtainable"
	elif keyword == "Lint_ImplicitKeywords":
		plural = "Lint Items with Implicit Keywords"
	elif keyword == "Lint_NotObtainable":
		plural = "Lint Items Which are Unobtainable"
	elif keyword == "Lint_RecipeIngredientKeywords":
		plural = "Lint Items with Recipe Ingredient Keywords"
	elif keyword == "Lockpicks":
		plural = "Lockpicks"
	elif keyword == "Loot":
		plural = "Loot"
	elif keyword == "LoreRecipe":
		plural = "Lore Recipes"
	elif keyword == "Lungfish":
		plural = "Lungfish"
	elif keyword == "Lute":
		plural = "Lutes"
	elif keyword == "LydiasSoul":
		plural = "Lydia's Souls"
	elif keyword == "MagicDust":
		plural = "Magic Dusts"
	elif keyword == "MagicOil":
		plural = "Magic Oil"
	elif keyword == "MagicTooth":
		plural = "Magic Teeth"
	elif keyword == "MainHand":
		plural = "Items Wielded in the Main Hand"
	elif keyword == "MainHandAugment":
		plural = "Main Hand Augments"
	elif keyword == "MaintenanceOil":
		plural = "Maintenance Oil"
	elif keyword == "Malachite":
		plural = "Malachites"
	elif keyword == "MandrakeRoot":
		plural = "Mandrake Root"
	elif keyword == "ManticoreTailTip":
		plural = "Manticore Tail Tips"
	elif keyword == "MantisClaw":
		plural = "Mantis Claws"
	elif keyword == "MapleWood":
		plural = "Maple Wood"
	elif keyword == "Marigold":
		plural = "Marigolds"
	elif keyword == "MasqueradeMask":
		plural = "Masquerade Masks"
	elif keyword == "MattedHair":
		plural = "Matted Hair"
	elif keyword == "MaxHealthPotion":
		plural = "Potions Which Boost Maximum Health"
	elif keyword == "Maximized":
		plural = "Maximized Gems"
	elif keyword == "Meat":
		plural = "Meat"
	elif keyword == "MeatDish":
		plural = "Meat Dishes"
	elif keyword == "MeditationRecipe":
		plural = "Meditation Recipes"
	elif keyword == "MeditationStool":
		plural = "Meditation Stools"
	elif keyword == "MeltOnGround":
		plural = "Items Which Melt when Left on the Ground"
	elif keyword == "Meltable":
		plural = "Meltable Items"
	elif keyword == "MemoryInhibitor":
		plural = "Memory Inhibitors"
	elif keyword == "Mercury":
		plural = "Mercury"
	elif keyword == "MeshGrate":
		plural = "Mesh Grates"
	elif keyword == "MetalArmor":
		plural = "Pieces of Metal Armor"
	elif keyword == "MetalBoots":
		plural = "Metal Boots"
	elif keyword == "MetalDyeableArmor":
		plural = "Dyeable Metal Armor"
	elif keyword == "MetalGloves":
		plural = "Metal Gloves"
	elif keyword == "MetalHelm":
		plural = "Metal Helms"
	elif keyword == "MetalPants":
		plural = "Metal Pants"
	elif keyword == "MetalShield":
		plural = "Metal Shields"
	elif keyword == "MetalShirt":
		plural = "Metal Shirts"
	elif keyword == "MetalSlab":
		plural = "Metal Slabs"
	elif keyword == "Milk":
		plural = "Milk"
	elif keyword == "MindGem":
		plural = "Mind Gems"
	elif keyword == "MineralSurvey":
		plural = "Mineral Surveys"
	elif keyword == "MiningSurvey":
		plural = "Mining Surveys"
	elif keyword == "MinotaurHammer":
		plural = "Minotaur Hammers"
	elif keyword == "MiseryTrooper":
		plural = "Misery Trooper Equipment"
	elif keyword == "MoldDirt":
		plural = "Mold and Dirt"
	elif keyword == "Molybdenum":
		plural = "Molybdenums"
	elif keyword == "Money":
		plural = "Money"
	elif keyword == "Moonstone":
		plural = "Moonstones"
	elif keyword == "Morganite":
		plural = "Morganites"
	elif keyword == "MossAgate":
		plural = "Moss Agates"
	elif keyword == "MotherlodeMap":
		plural = "Motherlode Maps"
	elif keyword == "MummyWrapping":
		plural = "Mummy Wrappings"
	elif keyword == "Mushroom":
		plural = "Mushrooms"
	elif keyword == "MushroomBox":
		plural = "Mushroom Boxes"
	elif keyword == "MushroomGrowBox":
		plural = "Mushroom Box Frames"
	elif keyword == "MushroomParts":
		plural = "Mushroom Flakes and Powders"
	elif keyword == "MushroomSubstrate":
		plural = "Mushroom Farming Substrates"
	elif keyword == "MushroomSubstrate_Bone":
		plural = "Bone Mushroom Substrates"
	elif keyword == "MushroomSubstrate_Dirt":
		plural = "Dirt Mushroom Substrates"
	elif keyword == "MushroomSubstrate_Exotic":
		plural = "Exotic Mushroom Substrates"
	elif keyword == "MushroomSubstrate_Limbs":
		plural = "Limb-based Mushroom Substrates"
	elif keyword == "MushroomSubstrate_Meat":
		plural = "Meat Mushroom Substrates"
	elif keyword == "MushroomSubstrate_Organs":
		plural = "Organ Mushroom Substrates"
	elif keyword == "MuttererCabalist":
		plural = "Mutterer Cabalist Equipment"
	elif keyword == "MuttererNecromancer":
		plural = "Mutterer Necromanceer Equipment"
	elif keyword == "MycologyRecipe":
		plural = "Mycology Recipes"
	elif keyword == "Nail":
		plural = "Nails"
	elif keyword == "Nature":
		plural = "Nature-Related Items"
	elif keyword == "Necklace":
		plural = "Necklaces"
	elif keyword == "NecklaceAugment":
		plural = "Necklace Augments"
	elif keyword == "NecromancyGem":
		plural = "Items Containing Necromancy Gems"
	elif keyword == "NecromancyRecipe":
		plural = "Necromancy Recipes"
	elif keyword == "NightmareFlesh":
		plural = "Nightmare Flesh"
	elif keyword == "NoGourmandBonus":
		plural = "Foods without Duration Bonuses from Gourmand"
	elif keyword == "NoWorkOrders":
		plural = "Items that should not have Work Orders"
	elif keyword == "NonFaeMetalArmor":
		plural = "Non-Fae Metal Armor"
	elif keyword == "NotDyeable":
		plural = "Items that Aren't Dyeable"
	elif keyword == "Nuts":
		plural = "Nuts"
	elif keyword == "OakWood":
		plural = "Oak Wood"
	elif keyword == "Obsidian":
		plural = "Obsidians"
	elif keyword == "Ocarina":
		plural = "Ocarinas"
	elif keyword == "OffHand":
		plural = "Items Wielded in the Off Hand"
	elif keyword == "OffHandAugment":
		plural = "Off Hand Augments"
	elif keyword == "OffHandShield":
		plural = "Off Hand Shields"
	elif keyword == "OgreStomach":
		plural = "Ogre Stomachs"
	elif keyword == "Oil":
		plural = "Oils"
	elif keyword == "Onion":
		plural = "Onions"
	elif keyword == "Onyx":
		plural = "Onyxes"
	elif keyword == "Opal":
		plural = "Opals"
	elif keyword == "OrangeCrystal":
		plural = "Orange Crystals"
	elif keyword == "Orb":
		plural = "Orbs"
	elif keyword == "OrcHairComb":
		plural = "Orcish Hair Combs"
	elif keyword == "OrcTrash":
		plural = "Orcish Trash"
	elif keyword == "OrcishCulture":
		plural = "Items Related to Orcish Culture"
	elif keyword == "OrcishLanguage":
		plural = "Items Written in the Orcish Language"
	elif keyword == "Ore":
		plural = "Ores"
	elif keyword == "OrganBonus":
		plural = "Knives Which Grant a Bonus to Finding Organs when Butchering"
	elif keyword == "OrganicArmor":
		plural = "Pieces of Organic Armor"
	elif keyword == "OrganicBoots":
		plural = "Organic Boots"
	elif keyword == "OrganicDyeableArmor":
		plural = "Dyeable Organic Armor"
	elif keyword == "OrganicGloves":
		plural = "Organic Gloves"
	elif keyword == "OrganicHelm":
		plural = "Organic Helms"
	elif keyword == "OrganicPants":
		plural = "Organic Pants"
	elif keyword == "OrganicShirt":
		plural = "Organic Shirts"
	elif keyword == "OversizedMandible":
		plural = "Oversized Mandibles"
	elif keyword == "OysterKnife":
		plural = "Oyster Knives"
	elif keyword == "Painting":
		plural = "Paintings"
	elif keyword == "Paladium":
		plural = "Paladia"
	elif keyword == "PantherSkin":
		plural = "Panther Skins"
	elif keyword == "Parchment":
		plural = "Parchment"
	elif keyword == "PathologyBonus":
		plural = "Autopsy Kits with Bonuses"
	elif keyword == "Peach":
		plural = "Peaches"
	elif keyword == "Pear":
		plural = "Pears"
	elif keyword == "Pearl":
		plural = "Pearls"
	elif keyword == "Peas":
		plural = "Peas"
	elif keyword == "PennocsPendant":
		plural = "Pennoc's Pendants"
	elif keyword == "Pepper":
		plural = "Peppers"
	elif keyword == "Perch":
		plural = "Perch"
	elif keyword == "PerfectCedarWood":
		plural = "Perfect Cedar Wood"
	elif keyword == "PerfectMapleWood":
		plural = "Perfect Maple Wood"
	elif keyword == "PerfectOakWood":
		plural = "Perfect Oak Wood"
	elif keyword == "PerfectSpruceWood":
		plural = "Perfect Spruce Wood"
	elif keyword == "PerfectWood":
		plural = "Perfect Wood"
	elif keyword == "Perfume":
		plural = "Perfumes"
	elif keyword == "Peridot":
		plural = "Peridots"
	elif keyword == "Phlogiston":
		plural = "Phlogiston"
	elif keyword == "PhrenologyRecipe":
		plural = "Phrenology Recipes"
	elif keyword == "PickledFish":
		plural = "Pickled Fish"
	elif keyword == "PigMalachite":
		plural = "Pig Malachites"
	elif keyword == "PigMeat":
		plural = "Pig Meat"
	elif keyword == "PigSkin":
		plural = "Pig Skins"
	elif keyword == "PigSnout":
		plural = "Pig Snouts"
	elif keyword == "PinealJuice":
		plural = "Pineal Juice"
	elif keyword == "PinkDye":
		plural = "Pink Dyes"
	elif keyword == "PixieAntler":
		plural = "Pixie Antlers"
	elif keyword == "PixiesParasol":
		plural = "Pixie's Parasols"
	elif keyword == "Plant":
		plural = "Plants"
	elif keyword == "Plate":
		plural = "Plates"
	elif keyword == "Platinum":
		plural = "Platinum Ores"
	elif keyword == "Poetry":
		plural = "Poetry"
	elif keyword == "PoetryStyle":
		plural = "Identified Poetry Books (Label A)"
	elif keyword == "PoetryTier":
		plural = "Identified Poetry Books (Label B)"
	elif keyword == "Poison":
		plural = "Poisons"
	elif keyword == "PoisonousDrink":
		plural = "Poisonous Drinks"
	elif keyword == "PoisonousFood":
		plural = "Poisonous Foods"
	elif keyword == "PorciniMushroom":
		plural = "Porcini Mushrooms"
	elif keyword == "PorkShoulder":
		plural = "Pork Shoulders"
	elif keyword == "Potato":
		plural = "Potatoes"
	elif keyword == "Potion":
		plural = "Potions"
	elif keyword == "PreparedFood":
		plural = "Prepared Foods"
	elif keyword == "Prism":
		plural = "Prisms"
	elif keyword == "PsychologyRecipe":
		plural = "Pyschology Recipes"
	elif keyword == "Pumpkin":
		plural = "Pumpkins"
	elif keyword == "PumpkinPie":
		plural = "Pumpkin Pies"
	elif keyword == "PumpkinSalad":
		plural = "Pumpkin Salads"
	elif keyword == "Pyrite":
		plural = "Pyrites"
	elif keyword == "Quartz":
		plural = "Quartzes"
	elif keyword == "RabbitFuel":
		plural = "Items Rabbits like to Eat"
	elif keyword == "RabbitMalachite":
		plural = "Rabbit Malachites"
	elif keyword == "RabbitSkin":
		plural = "Rabbit Skins"
	elif keyword == "Racial":
		plural = "Racial-Slot Items"
	elif keyword == "RacialJewelry":
		plural = "Jewelry Associated with a Specific Race"
	elif keyword == "RanalonGlassBracelet":
		plural = "Ranalon Glass Bracelets"
	elif keyword == "RareRecipe":
		plural = "Rare Recipes"
	elif keyword == "RatSkin":
		plural = "Rat Skins"
	elif keyword == "RatkinAparatif":
		plural = "Ratkin Aparatifs"
	elif keyword == "RatkinDigestif":
		plural = "Ratkin Digestifs"
	elif keyword == "RatkinNecroTalisman":
		plural = "Ratkin Necromancer's Talismans"
	elif keyword == "RawCotton":
		plural = "Raw Cotton"
	elif keyword == "RawDeerMeat":
		plural = "Raw Deer Meat"
	elif keyword == "RawGarnet":
		plural = "Raw Garnets"
	elif keyword == "RawLapisLazuli":
		plural = "Raw Lapis Lazulis"
	elif keyword == "RawMalachite":
		plural = "Raw Malachites"
	elif keyword == "RawMushroom":
		plural = "Raw Mushrooms"
	elif keyword == "RawOnyx":
		plural = "Raw Onyxes"
	elif keyword == "RawRabbitMeat":
		plural = "Raw Rabbit Meat"
	elif keyword == "RawTopaz":
		plural = "Raw Topazes"
	elif keyword == "Rawhide":
		plural = "Rawhide Items"
	elif keyword == "Recipe":
		plural = "Recipes"
	elif keyword == "RecitablePoetry":
		plural = "Recitable Poetry"
	elif keyword == "RedCrystal":
		plural = "Red Crystals"
	elif keyword == "RedGem":
		plural = "Red Gems"
	elif keyword == "RedWingToken":
		plural = "Redwing Tokens"
	elif keyword == "ResistancePotion":
		plural = "Resistance Potions "
	elif keyword == "RestorativePotion":
		plural = "Restorative Potions"
	elif keyword == "ReusableBeerKeg":
		plural = "Reusable Beer Kegs"
	elif keyword == "ReusableHardLiquorBarrel":
		plural = "Reusable Hard Liquor Barrels"
	elif keyword == "RhinoHide":
		plural = "Rhino Hides"
	elif keyword == "RhinoHorn":
		plural = "Rhino Horns"
	elif keyword == "RiShinPriestGarment":
		plural = "Ri-Shin Priest Garments"
	elif keyword == "Ring":
		plural = "Rings"
	elif keyword == "RingAugment":
		plural = "Ring Augments"
	elif keyword == "Rivet":
		plural = "Rivets"
	elif keyword == "Root":
		plural = "Roots"
	elif keyword == "RottenMeat":
		plural = "Rotten Meat"
	elif keyword == "Ruby":
		plural = "Rubies"
	elif keyword == "Rune":
		plural = "Runes"
	elif keyword == "Saltpeter":
		plural = "Saltpeter"
	elif keyword == "Sapphire":
		plural = "Sapphires"
	elif keyword == "Sardonyx":
		plural = "Sardonyxes"
	elif keyword == "Saw":
		plural = "Saws"
	elif keyword == "ScorpionStinger":
		plural = "Scorpion Stingers"
	elif keyword == "ScrayLung":
		plural = "Scray Lungs"
	elif keyword == "ScrayStinger":
		plural = "Scray Stingers"
	elif keyword == "Scroll":
		plural = "Scrolls"
	elif keyword == "Seashell":
		plural = "Seashells"
	elif keyword == "Seed":
		plural = "Seeds"
	elif keyword == "Seedling":
		plural = "Seedlings"
	elif keyword == "SemiRealHassium":
		plural = "Semi Real Hassium"
	elif keyword == "Serpentine":
		plural = "Serpentines"
	elif keyword == "SexyClothing":
		plural = "Sexy Clothing"
	elif keyword == "ShamanicInfusionRecipe":
		plural = "Shamanic Infusion Recipes"
	elif keyword == "Shark":
		plural = "Sharks"
	elif keyword == "SharkSkin":
		plural = "Shark Skins"
	elif keyword == "Sharpen":
		plural = "Tubes of Sharpen"
	elif keyword == "SheepSkin":
		plural = "Sheep Skins"
	elif keyword == "Shield":
		plural = "Shields"
	elif keyword == "Shovel":
		plural = "Shovels"
	elif keyword == "Shrimp":
		plural = "Shrimp"
	elif keyword == "Silver":
		plural = "Silver Items"
	elif keyword == "SirJohnsonBuck":
		plural = "Sir Johnson Bucks"
	elif keyword == "SirineCheese":
		plural = "Sirine Cheese"
	elif keyword == "SirinesBelt":
		plural = "Sirine's Belts"
	elif keyword == "Sittable":
		plural = "Items Upon Which One Can Sit"
	elif keyword == "SkillBoostPotion":
		plural = "Skill Boost Potions"
	elif keyword == "SkillIngredient":
		plural = "Skill Ingredients"
	elif keyword == "Skin":
		plural = "Skins"
	elif keyword == "Skinning":
		plural = "Skinning Related Items"
	elif keyword == "SkinningBonus":
		plural = "Knives Which Provide a Skinning Bonus"
	elif keyword == "SkinningKnife":
		plural = "Skinning Knives"
	elif keyword == "Skull":
		plural = "Skulls"
	elif keyword == "SkullExtractionBonus":
		plural = "Items Which Provide a Bonus to Skull Extraction"
	elif keyword == "SkullExtractor":
		plural = "Skull Extractor"
	elif keyword == "Slippers":
		plural = "Slippers"
	elif keyword == "Snack":
		plural = "Snacks"
	elif keyword == "SnackingBread":
		plural = "Snacking Bread"
	elif keyword == "SnailShell":
		plural = "Snail Shells"
	elif keyword == "SnakeScales":
		plural = "Snake Scales"
	elif keyword == "SnakeSkin":
		plural = "Snake Skins"
	elif keyword == "Soup":
		plural = "Soups"
	elif keyword == "SpiderLeg":
		plural = "Spider Legs"
	elif keyword == "SpiderMalachite":
		plural = "Spider Malachites"
	elif keyword == "SpiderMandible":
		plural = "Spider Mandibles"
	elif keyword == "SpiderMeat":
		plural = "Spider Meat"
	elif keyword == "SpiderSilk":
		plural = "Spider Silk"
	elif keyword == "SpiritFoxLapisLazuli":
		plural = "Spirit Fox Lapis Lazulis"
	elif keyword == "SpiritStone":
		plural = "Spirit Stones"
	elif keyword == "Spleen":
		plural = "Spleens"
	elif keyword == "Spoon":
		plural = "Spoons"
	elif keyword == "SpruceWood":
		plural = "Spruce Wood"
	elif keyword == "Squash":
		plural = "Squashes"
	elif keyword == "Staff":
		plural = "Staves"
	elif keyword == "StaffRecipe":
		plural = "Staff Recipes"
	elif keyword == "StandardShovel":
		plural = "Standard Shovels"
	elif keyword == "Starfish":
		plural = "Starfish"
	elif keyword == "Statue":
		plural = "Statues"
	elif keyword == "Stibnite":
		plural = "Stibnites"
	elif keyword == "Stinger":
		plural = "Stingers"
	elif keyword == "Stock":
		plural = "Stock Equipment"
	elif keyword == "Stomach":
		plural = "Stomachs"
	elif keyword == "Stool":
		plural = "Stools"
	elif keyword == "StorageCrate":
		plural = "Storage Crates "
	elif keyword == "String":
		plural = "Pieces of String"
	elif keyword == "Sugarcane":
		plural = "Sugarcane"
	elif keyword == "Sulfur":
		plural = "Sulfur"
	elif keyword == "SummerCourtArmor":
		plural = "Summer Court Armor"
	elif keyword == "SummonBox":
		plural = "Summonable Boxes"
	elif keyword == "Sunstone":
		plural = "Sunstones"
	elif keyword == "SweetRoastedPumpkin":
		plural = "Sweet Roasted Pumpkins"
	elif keyword == "Sword":
		plural = "Swords"
	elif keyword == "SwordRecipe":
		plural = "Sword Recipes"
	elif keyword == "Tail":
		plural = "Tails"
	elif keyword == "Tailoring":
		plural = "Tailoring-Related Items"
	elif keyword == "TailoringRecipe":
		plural = "Tailoring Recipes"
	elif keyword == "Tallow":
		plural = "Tallow"
	elif keyword == "Tannin":
		plural = "Tannin Powder"
	elif keyword == "Tea":
		plural = "Tea"
	elif keyword == "Tealight":
		plural = "Tealights"
	elif keyword == "TelkasTeeth":
		plural = "Telka's Teeth Potions"
	elif keyword == "Textiles":
		plural = "Textiles"
	elif keyword == "Thread":
		plural = "Thread"
	elif keyword == "ThrowingKnife":
		plural = "Throwing Knives "
	elif keyword == "TigerSkin":
		plural = "Tiger Skins"
	elif keyword == "TigersEye":
		plural = "Tiger's Eye Gens"
	elif keyword == "TitleScroll":
		plural = "Title Scrolls"
	elif keyword == "Tool":
		plural = "Tools"
	elif keyword == "ToolHammer":
		plural = "Hammers Used as Tools"
	elif keyword == "Tooth":
		plural = "Teeth"
	elif keyword == "Topaz":
		plural = "Topazes"
	elif keyword == "Tourmaline":
		plural = "Tourmalines"
	elif keyword == "ToxicSludge":
		plural = "Toxic Sludge"
	elif keyword == "TreacheryTrooper":
		plural = "Treachery Trooper Equipment"
	elif keyword == "TreantLeaves":
		plural = "Treant Leaves"
	elif keyword == "Treantwood":
		plural = "Treant Wood"
	elif keyword == "TreasureClueAccuracy":
		plural = "Treasure Clues (Accuracy)"
	elif keyword == "TreasureClues":
		plural = "Treasure Clues"
	elif keyword == "TreasureCluesEltibuleAmazing":
		plural = "Incredible Eltibule Treasure Clues "
	elif keyword == "TreasureCluesEltibuleGood":
		plural = "Large Eltibule Treasure Clues"
	elif keyword == "TreasureCluesEltibuleGreat":
		plural = "Vast Riches Eltibule Treasure Clues"
	elif keyword == "TreasureCluesEltibulePoor":
		plural = "Small Eltibule Treasure Clues"
	elif keyword == "TreasureCluesIlmariAmazing":
		plural = "Incredible Ilmari Treasure Clues"
	elif keyword == "TreasureCluesIlmariGood":
		plural = "Large Ilmari Treasure Clues"
	elif keyword == "TreasureCluesIlmariGreat":
		plural = "Vast Riches Ilmari Treasure Clues"
	elif keyword == "TreasureCluesIlmariPoor":
		plural = "Small Ilmari Treasure Clues"
	elif keyword == "TreasureCluesSunValeAmazing":
		plural = "Incredible Sun Vale Treasure Clues"
	elif keyword == "TreasureCluesSunValeGood":
		plural = "Large Sun Vale Treasure Clues"
	elif keyword == "TreasureCluesSunValeGreat":
		plural = "Vast Riches Sun Vale Treasure Clues"
	elif keyword == "TreasureCluesSunValePoor":
		plural = "Small Sun Vale Treasure Clues"
	elif keyword == "TreasureMap":
		plural = "Treasure Maps"
	elif keyword == "Trident":
		plural = "Tridents"
	elif keyword == "TrollFlesh":
		plural = "Troll Flesh"
	elif keyword == "TrueSkinningKnife":
		plural = "True Skinning Knives"
	elif keyword == "Tsavorite":
		plural = "Tsavorites"
	elif keyword == "Tuba":
		plural = "Tubas"
	elif keyword == "TuftOfFur":
		plural = "Tufts of Fur"
	elif keyword == "TundraLichen":
		plural = "Tundra Lichens"
	elif keyword == "Tungsten":
		plural = "Tungsten"
	elif keyword == "Turquoise":
		plural = "Turquoises"
	elif keyword == "Ugly":
		plural = "Ugly Equipment"
	elif keyword == "UnarmedClaw":
		plural = "Unarmed Claw Weapons"
	elif keyword == "UnarmedMainHandWeapon":
		plural = "Unarmed Main Hand Weapons"
	elif keyword == "UnarmedWeapon":
		plural = "Unarmed Weapons"
	elif keyword == "UncrossingOil":
		plural = "Uncrossing Oils"
	elif keyword == "UnusedGem":
		plural = "Unused Gems"
	elif keyword == "ValuableMetalSlab":
		plural = "Valuable Metal Slabs"
	elif keyword == "VeganDish":
		plural = "Vegan Dishes"
	elif keyword == "Vegetable":
		plural = "Vegetables"
	elif keyword == "VegetableDish":
		plural = "Vegetable Dishes"
	elif keyword == "VegetarianDish":
		plural = "Vegetarian Dishes"
	elif keyword == "VendorTrash":
		plural = "Vendor Trash"
	elif keyword == "Vervadium":
		plural = "Vervadiums"
	elif keyword == "VipToken":
		plural = "VIP Tokens"
	elif keyword == "ViperFangs":
		plural = "Viper Fangs"
	elif keyword == "Vise":
		plural = "Vises"
	elif keyword == "Vitriol":
		plural = "Acidic Cleansers"
	elif keyword == "Waist":
		plural = "Items Worn on the Waist"
	elif keyword == "Wand":
		plural = "Wands"
	elif keyword == "Watercress":
		plural = "Watercress "
	elif keyword == "Weapon":
		plural = "Weapons"
	elif keyword == "WerewolfRecipe":
		plural = "Lycanthropy Recipes"
	elif keyword == "WhiteCrystal":
		plural = "White Crystals"
	elif keyword == "Wick":
		plural = "Wicks"
	elif keyword == "WindstepShoes":
		plural = "Windstep Shoes"
	elif keyword == "WineCask":
		plural = "Wine Casks"
	elif keyword == "WinterCourtArmor":
		plural = "Winter Court Armor"
	elif keyword == "Winterprize":
		plural = "Winterprize"
	elif keyword == "WolfSkin":
		plural = "Wolf Skins"
	elif keyword == "Wood":
		plural = "Wood"
	elif keyword == "WoodGlue":
		plural = "Wood Glue"
	elif keyword == "Wooden":
		plural = "Wooden Items"
	elif keyword == "WoodenArmor":
		plural = "Pieces of Wooden Armor"
	elif keyword == "WoodenBoots":
		plural = "Wooden Boots"
	elif keyword == "Wool":
		plural = "Wool"
	elif keyword == "WorkOrder":
		plural = "Work Orders "
	elif keyword == "WormSilk":
		plural = "Worm Silk"
	elif keyword == "WormTooth":
		plural = "Worm Teeth"
	elif keyword == "WritingRelated":
		plural = "Writing-Related Items"
	elif keyword == "Xedrite":
		plural = "Xedrite"
	elif keyword == "Xogrite":
		plural = "Xogrite"
	elif keyword == "Yarn":
		plural = "Yarn"
	elif keyword == "YellowCrystal":
		plural = "Yellow Crystals"
	if plural:
		return '[[:Category:Items/' + keyword + '|' + plural + ']]'
	else:
		return "Item Category " + keyword + " Not Found"
