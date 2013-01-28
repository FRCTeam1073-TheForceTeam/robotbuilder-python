#set($subsystem = $helper.getByName($subsystem-name, $robot))
#set($component = $subsystem.getProperty("Input").getValue())
#set($name = ${helper.getByName($component, $robot).name})
#if($name)        return self.#variable($name).PIDGet()
#end
