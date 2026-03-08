"""Thingery CLI Entry Point"""
import click


@click.group()
@click.version_option(version="0.1.0")
def thingery_entry():
    """Thingery - Physical/Chemical Data Library
    
    A comprehensive library of physical and chemical data including
    elements, materials, food nutrition, scales, protocols, and more.
    """
    pass


@thingery_entry.command("list-elements")
def list_elements():
    """List all elements in the periodic table"""
    from thingery import elements
    for el in sorted(elements.ELEMENTS.values(), key=lambda x: x.number):
        click.echo(f"{el.symbol:>3} {el.name:<12} #{el.number}")


@thingery_entry.command("list-materials")
def list_materials():
    """List all available materials"""
    from thingery import materials
    for name in sorted(materials.MATERIALS.keys()):
        click.echo(f"  - {name}")


@thingery_entry.command("search")
@click.argument("query")
def search(query):
    """Search thingery data"""
    from thingery import elements, materials
    
    query_lower = query.lower()
    results = []
    
    # Search elements
    for symbol, el in elements.ELEMENTS.items():
        if query_lower in el.name.lower() or query_lower in symbol.lower():
            results.append(f"Element: {el.name} ({symbol})")
    
    # Search materials
    for name, mat in materials.MATERIALS.items():
        if query_lower in name.lower():
            results.append(f"Material: {name}")
    
    if results:
        for r in results:
            click.echo(r)
    else:
        click.echo(f"No results found for '{query}'")


@thingery_entry.command("element")
@click.argument("symbol")
def element_info(symbol):
    """Get detailed element information"""
    from thingery import elements
    
    symbol = symbol.capitalize()
    if symbol in elements.ELEMENTS:
        el = elements.ELEMENTS[symbol]
        click.echo(f"Element: {el.name}")
        click.echo(f"Symbol: {el.symbol}")
        click.echo(f"Atomic Number: {el.number}")
        click.echo(f"Atomic Mass: {el.atomic_mass}")
        if el.category:
            click.echo(f"Category: {el.category}")
    else:
        click.echo(f"Element '{symbol}' not found")


@thingery_entry.command("scale")
@click.argument("scale_name")
def scale_info(scale_name):
    """Get scale information"""
    from thingery import scales
    
    if scale_name in scales.SCALES:
        s = scales.SCALES[scale_name]
        click.echo(f"Scale: {s.name}")
        click.echo(f"Type: {s.scale_type}")
        click.echo(f"Min: {s.min_value}")
        click.echo(f"Max: {s.max_value}")
    else:
        click.echo(f"Scale '{scale_name}' not found")


if __name__ == "__main__":
    thingery_entry()
